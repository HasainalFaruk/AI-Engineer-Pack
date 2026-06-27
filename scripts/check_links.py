"""Validate Markdown links in the AI Engineer Pack repository.

Usage examples:
    python scripts/check_links.py
    python scripts/check_links.py --json
    python scripts/check_links.py --root G:/AI-Engineer-Pack

Exit codes:
    0: no broken links found
    1: broken links found or execution error
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence
from urllib.parse import unquote, urlparse

LOGGER = logging.getLogger("check_links")
EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "upstream", "archive"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_PATTERN = re.compile(r"^\s*\[[^\]]+\]:\s+(\S+)", re.MULTILINE)
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class LinkIssue:
    """A Markdown link validation issue."""

    kind: str
    file: str
    line: int
    target: str
    message: str


@dataclass(frozen=True)
class LinkStats:
    """Summary counts for link validation."""

    markdown_files: int
    links_checked: int
    broken_links: int
    missing_files: int
    unused_links: int


def repository_root(start: Path | None = None) -> Path:
    """Return the repository root inferred from this script location."""

    if start is None:
        start = Path(__file__).resolve()
    return start.parents[1]


def iter_markdown(root: Path) -> Iterable[Path]:
    """Yield Markdown files in the repository."""

    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def slugify_heading(text: str) -> str:
    """Return the GitHub-style heading anchor for a Markdown heading."""

    text = re.sub(r"<[^>]+>", "", text.strip().lower())
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def anchors_for(path: Path) -> set[str]:
    """Return heading anchors available in a Markdown file."""

    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return set()
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for match in HEADING_PATTERN.finditer(text):
        base = slugify_heading(match.group(2))
        if not base:
            continue
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


def line_for_offset(text: str, offset: int) -> int:
    """Return a 1-based line number for a character offset."""

    return text.count("\n", 0, offset) + 1


def is_external(target: str) -> bool:
    """Return True for links that do not resolve inside the repository."""

    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto", "tel"}


def clean_target(raw_target: str) -> str:
    """Remove Markdown title text and angle brackets from a link target."""

    target = raw_target.strip().strip("<>")
    if " " in target and not target.startswith("#"):
        first = target.split(" ", 1)[0]
        if first.startswith(("http://", "https://", "mailto:", "tel:")) or "/" in first or first.endswith(".md"):
            target = first
    return unquote(target)


def validate_links(root: Path) -> tuple[list[LinkIssue], LinkStats]:
    """Validate relative links and anchors in Markdown files."""

    issues: list[LinkIssue] = []
    markdown_files = list(iter_markdown(root))
    links_checked = 0
    missing_files = 0

    anchor_cache: dict[Path, set[str]] = {}
    linked_files: set[Path] = set()

    for md_file in markdown_files:
        try:
            text = md_file.read_text(encoding="utf-8")
        except OSError as exc:
            issues.append(LinkIssue("read-error", md_file.relative_to(root).as_posix(), 1, "", str(exc)))
            continue

        raw_targets = [m.group(1) for m in LINK_PATTERN.finditer(text)] + [m.group(1) for m in REFERENCE_PATTERN.finditer(text)]
        for match in LINK_PATTERN.finditer(text):
            pass
        for raw_target in raw_targets:
            target = clean_target(raw_target)
            if not target or is_external(target):
                continue
            links_checked += 1

            target_path_text, _, anchor = target.partition("#")
            if target_path_text:
                candidate = (md_file.parent / target_path_text).resolve()
            else:
                candidate = md_file.resolve()

            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                line = line_for_offset(text, text.find(raw_target))
                missing_files += 1
                issues.append(LinkIssue("missing-file", md_file.relative_to(root).as_posix(), line, target, "Link points outside the repository."))
                continue

            if not candidate.exists():
                line = line_for_offset(text, text.find(raw_target))
                missing_files += 1
                issues.append(LinkIssue("missing-file", md_file.relative_to(root).as_posix(), line, target, "Linked file does not exist."))
                continue

            linked_files.add(candidate)
            if anchor:
                if candidate.is_dir():
                    line = line_for_offset(text, text.find(raw_target))
                    issues.append(LinkIssue("broken-anchor", md_file.relative_to(root).as_posix(), line, target, "Anchor points to a directory."))
                    continue
                anchors = anchor_cache.setdefault(candidate, anchors_for(candidate))
                normalized_anchor = anchor.lower().lstrip("#")
                if normalized_anchor not in anchors:
                    line = line_for_offset(text, text.find(raw_target))
                    issues.append(LinkIssue("broken-anchor", md_file.relative_to(root).as_posix(), line, target, "Anchor not found in linked Markdown file."))

    unused_links = 0
    # Report Markdown files that are not linked by any other Markdown file, excluding common entry points.
    entry_points = {root / "README.md", root / "docs" / "SUMMARY.md"}
    for md_file in markdown_files:
        resolved = md_file.resolve()
        if resolved in {p.resolve() for p in entry_points if p.exists()}:
            continue
        if resolved not in linked_files and md_file.name != "README.md":
            unused_links += 1
            issues.append(LinkIssue("unused-link", md_file.relative_to(root).as_posix(), 1, "", "Markdown file is not linked by other Markdown files."))

    broken = len([issue for issue in issues if issue.kind != "unused-link"])
    stats = LinkStats(len(markdown_files), links_checked, broken, missing_files, unused_links)
    return sorted(issues, key=lambda item: (item.kind, item.file, item.line, item.target)), stats


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""

    parser = argparse.ArgumentParser(description="Validate Markdown links in the AI Engineer Pack.")
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root to scan.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON output.")
    parser.add_argument("--strict-unused", action="store_true", help="Fail when unused Markdown files are found.")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run link validation and return a process exit code."""

    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s: %(message)s")
    root = args.root.resolve()
    if not root.exists():
        LOGGER.error("Repository root does not exist: %s", root)
        return 1

    issues, stats = validate_links(root)
    failing_issues = [issue for issue in issues if args.strict_unused or issue.kind != "unused-link"]
    if args.json:
        print(json.dumps({"stats": asdict(stats), "issues": [asdict(issue) for issue in issues]}, indent=2))
    else:
        print(f"Markdown files: {stats.markdown_files}")
        print(f"Links checked: {stats.links_checked}")
        if issues:
            print("Link issues:")
            for issue in issues:
                print(f"- {issue.kind}: {issue.file}:{issue.line} {issue.target} - {issue.message}")
        else:
            print("No link issues found.")
    return 1 if failing_issues else 0


if __name__ == "__main__":
    sys.exit(main())
