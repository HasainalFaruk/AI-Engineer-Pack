"""Find placeholder text in the AI Engineer Pack repository.

Usage examples:
    python scripts/check_placeholders.py
    python scripts/check_placeholders.py --json
    python scripts/check_placeholders.py --include-empty

Exit codes:
    0: no placeholder text found
    1: placeholder text found or execution error
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

LOGGER = logging.getLogger("check_placeholders")
DEFAULT_EXCLUDES = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "node_modules", "upstream", "archive"}
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".ps1",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".txt",
    ".gitignore",
}
PLACEHOLDER_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("$name", re.compile(r"\$name", re.IGNORECASE)),
    ("$cmd", re.compile(r"\$cmd", re.IGNORECASE)),
    ("template variable", re.compile(r"\$\([^)]+\)|\$\{[^}]+\}")),
    ("TODO", re.compile(r"\bTODO\b", re.IGNORECASE)),
    ("FIXME", re.compile(r"\bFIXME\b", re.IGNORECASE)),
    ("Lorem Ipsum", re.compile(r"lorem\s+ipsum", re.IGNORECASE)),
    ("Replace Me", re.compile(r"replace\s+me", re.IGNORECASE)),
    ("Your Name", re.compile(r"your\s+name", re.IGNORECASE)),
    ("TBD", re.compile(r"\bTBD\b", re.IGNORECASE)),
    ("INSERT", re.compile(r"\bINSERT\b", re.IGNORECASE)),
)


@dataclass(frozen=True)
class PlaceholderOccurrence:
    """A placeholder match found in a repository file."""

    file: str
    line: int
    column: int
    label: str
    excerpt: str


def repository_root(start: Path | None = None) -> Path:
    """Return the repository root inferred from this script location."""

    if start is None:
        start = Path(__file__).resolve()
    return start.parents[1]


def is_text_file(path: Path) -> bool:
    """Return True when a file should be scanned as text."""

    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"CODEOWNERS", "LICENSE"}


def iter_files(root: Path, include_empty: bool = False) -> Iterable[Path]:
    """Yield text files under root while skipping generated or external folders."""

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in DEFAULT_EXCLUDES for part in path.relative_to(root).parts):
            continue
        if not include_empty and path.stat().st_size == 0:
            continue
        if is_text_file(path):
            yield path


def scan_file(path: Path, root: Path) -> list[PlaceholderOccurrence]:
    """Scan one file for placeholder patterns."""

    occurrences: list[PlaceholderOccurrence] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        LOGGER.debug("Skipping non-UTF-8 file: %s", path)
        return occurrences
    except OSError as exc:
        LOGGER.warning("Could not read %s: %s", path, exc)
        return occurrences

    for line_no, line in enumerate(text.splitlines(), start=1):
        for label, pattern in PLACEHOLDER_PATTERNS:
            for match in pattern.finditer(line):
                occurrences.append(
                    PlaceholderOccurrence(
                        file=path.relative_to(root).as_posix(),
                        line=line_no,
                        column=match.start() + 1,
                        label=label,
                        excerpt=line.strip(),
                    )
                )
    return occurrences


def scan_repository(root: Path) -> list[PlaceholderOccurrence]:
    """Scan the repository for placeholder text."""

    results: list[PlaceholderOccurrence] = []
    for file_path in iter_files(root):
        if file_path.resolve() == Path(__file__).resolve():
            continue
        results.extend(scan_file(file_path, root))
    return sorted(results, key=lambda item: (item.file, item.line, item.column, item.label))


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""

    parser = argparse.ArgumentParser(description="Search the AI Engineer Pack for placeholder text.")
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root to scan.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON output.")
    parser.add_argument("--include-empty", action="store_true", help="Accepted for compatibility; empty files are not meaningful for placeholder scanning.")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run placeholder validation and return a process exit code."""

    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s: %(message)s")
    root = args.root.resolve()
    if not root.exists():
        LOGGER.error("Repository root does not exist: %s", root)
        return 1

    occurrences = scan_repository(root)
    if args.json:
        print(json.dumps([asdict(item) for item in occurrences], indent=2))
    elif occurrences:
        print("Placeholder occurrences found:")
        for item in occurrences:
            print(f"- {item.file}:{item.line}:{item.column} [{item.label}] {item.excerpt}")
    else:
        print("No placeholder text found.")
    return 1 if occurrences else 0


if __name__ == "__main__":
    sys.exit(main())

