"""Search AI Engineer Pack documentation with ranked results.

Usage examples:
    python scripts/search.py wordpress
    python scripts/search.py "GitHub Actions" --limit 20
    python scripts/search.py security --json

Exit codes:
    0: search completed
    1: invalid input or execution error
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

LOGGER = logging.getLogger("search")
EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "upstream", "archive"}
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
TAG_PATTERN = re.compile(r"(?:tags|labels):\s*\[?([^\]\n]+)\]?", re.IGNORECASE)


@dataclass(frozen=True)
class SearchResult:
    """A ranked search result."""

    score: int
    path: str
    title: str
    matches: list[str]


def repository_root(start: Path | None = None) -> Path:
    """Return the repository root inferred from this script location."""

    if start is None:
        start = Path(__file__).resolve()
    return start.parents[1]


def iter_markdown(root: Path) -> Iterable[Path]:
    """Yield searchable Markdown files."""

    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def title_for(text: str, path: Path) -> str:
    """Return the first Markdown heading or the filename stem."""

    clean_text = text.lstrip("\ufeff")
    match = HEADING_PATTERN.search(clean_text)
    return match.group(2).strip() if match else path.stem.replace("-", " ").title()


def tokenize(query: str) -> list[str]:
    """Tokenize a search query."""

    return [token.lower() for token in re.findall(r"[a-zA-Z0-9_.-]+", query) if token.strip()]


def score_file(path: Path, root: Path, terms: list[str]) -> SearchResult | None:
    """Score one Markdown file for the query terms."""

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        LOGGER.debug("Could not read %s: %s", path, exc)
        return None

    rel = path.relative_to(root).as_posix()
    title = title_for(text, path)
    search_text = text.lstrip("\ufeff")
    headings = [match.group(2).strip() for match in HEADING_PATTERN.finditer(search_text)]
    tags = " ".join(match.group(1) for match in TAG_PATTERN.finditer(text))
    filename = path.name
    searchable = {
        "title": title.lower(),
        "headings": "\n".join(headings).lower(),
        "filename": filename.lower(),
        "path": rel.lower(),
        "tags": tags.lower(),
        "body": text.lower(),
    }

    score = 0
    matches: list[str] = []
    for term in terms:
        if term in searchable["title"]:
            score += 50
            matches.append(f"title:{term}")
        if term in searchable["filename"]:
            score += 35
            matches.append(f"filename:{term}")
        if term in searchable["path"]:
            score += 25
            matches.append(f"path:{term}")
        if term in searchable["headings"]:
            score += 20
            matches.append(f"heading:{term}")
        if term in searchable["tags"]:
            score += 15
            matches.append(f"tag:{term}")
        body_hits = searchable["body"].count(term)
        if body_hits:
            score += min(body_hits, 10)
            matches.append(f"body:{term} x{body_hits}")

    if score == 0:
        return None
    return SearchResult(score=score, path=rel, title=title, matches=matches)


def search(root: Path, query: str, limit: int) -> list[SearchResult]:
    """Search repository Markdown files and return ranked results."""

    terms = tokenize(query)
    if not terms:
        raise ValueError("Search query must contain at least one searchable term.")
    results = [result for path in iter_markdown(root) if (result := score_file(path, root, terms))]
    return sorted(results, key=lambda item: (-item.score, item.path))[:limit]


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""

    parser = argparse.ArgumentParser(description="Search AI Engineer Pack documentation.")
    parser.add_argument("query", help="Search query, such as 'wordpress' or 'GitHub Actions'.")
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root to search.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of results.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run repository search and return an exit code."""

    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s: %(message)s")
    root = args.root.resolve()
    try:
        results = search(root, args.query, args.limit)
    except ValueError as exc:
        LOGGER.error("%s", exc)
        return 1
    if args.json:
        print(json.dumps([asdict(item) for item in results], indent=2))
    else:
        if not results:
            print("No results found.")
        for index, result in enumerate(results, start=1):
            print(f"{index}. {result.title} [{result.score}]")
            print(f"   {result.path}")
            print(f"   matches: {', '.join(result.matches[:6])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

