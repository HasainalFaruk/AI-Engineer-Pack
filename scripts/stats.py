"""Generate repository statistics for the AI Engineer Pack.

Usage examples:
    python scripts/stats.py
    python scripts/stats.py --json
    python scripts/stats.py --top 15

Exit codes:
    0: statistics generated successfully
    1: execution error
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

LOGGER = logging.getLogger("stats")
EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "upstream", "archive"}


@dataclass(frozen=True)
class SizeEntry:
    """Size information for a file or folder."""

    path: str
    bytes: int


@dataclass(frozen=True)
class RepositoryStats:
    """Computed repository statistics."""

    markdown_files: int
    agents: int
    mcp_modules: int
    skills: int
    frameworks: int
    commands: int
    templates: int
    checklists: int
    examples: int
    python_scripts: int
    repository_size_bytes: int
    largest_folders: list[SizeEntry]
    largest_files: list[SizeEntry]


def repository_root(start: Path | None = None) -> Path:
    """Return the repository root inferred from this script location."""

    if start is None:
        start = Path(__file__).resolve()
    return start.parents[1]


def should_skip(path: Path, root: Path) -> bool:
    """Return True when a path belongs to an excluded folder."""

    return any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts)


def folder_size(path: Path, root: Path) -> int:
    """Return recursive size for a folder, excluding external/cache folders."""

    total = 0
    for child in path.rglob("*"):
        if child.is_file() and not should_skip(child, root):
            total += child.stat().st_size
    return total


def count_dirs(path: Path) -> int:
    """Count immediate child directories for a pack module."""

    return len([item for item in path.iterdir() if item.is_dir()]) if path.exists() else 0


def count_files(path: Path, pattern: str) -> int:
    """Count files matching a pattern below a path."""

    return len(list(path.rglob(pattern))) if path.exists() else 0


def collect_stats(root: Path, top: int = 10) -> RepositoryStats:
    """Collect repository statistics."""

    files = [path for path in root.rglob("*") if path.is_file() and not should_skip(path, root)]
    markdown_files = len([path for path in files if path.suffix.lower() == ".md"])
    python_scripts = len([path for path in (root / "scripts").glob("*.py")]) if (root / "scripts").exists() else 0
    repo_size = sum(path.stat().st_size for path in files)

    folder_entries = [
        SizeEntry(path=folder.relative_to(root).as_posix(), bytes=folder_size(folder, root))
        for folder in root.iterdir()
        if folder.is_dir() and not should_skip(folder, root)
    ]
    file_entries = [SizeEntry(path=file.relative_to(root).as_posix(), bytes=file.stat().st_size) for file in files]

    return RepositoryStats(
        markdown_files=markdown_files,
        agents=count_dirs(root / "agents"),
        mcp_modules=count_dirs(root / "mcp"),
        skills=count_files(root / "skills", "SKILL.md"),
        frameworks=count_dirs(root / "frameworks"),
        commands=count_dirs(root / "commands"),
        templates=count_dirs(root / "templates"),
        checklists=count_dirs(root / "checklists"),
        examples=markdown_files_in(root / "examples"),
        python_scripts=python_scripts,
        repository_size_bytes=repo_size,
        largest_folders=sorted(folder_entries, key=lambda item: item.bytes, reverse=True)[:top],
        largest_files=sorted(file_entries, key=lambda item: item.bytes, reverse=True)[:top],
    )


def markdown_files_in(path: Path) -> int:
    """Count Markdown files in a folder."""

    return len(list(path.rglob("*.md"))) if path.exists() else 0


def human_size(size: int) -> str:
    """Format bytes as a readable size."""

    units = ["B", "KB", "MB", "GB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} B"
        value /= 1024
    return f"{size} B"


def print_stats(stats: RepositoryStats) -> None:
    """Print formatted repository statistics."""

    print("AI Engineer Pack Repository Statistics")
    print("=" * 38)
    print(f"Markdown files:      {stats.markdown_files}")
    print(f"Agents:              {stats.agents}")
    print(f"MCP modules:         {stats.mcp_modules}")
    print(f"Skills:              {stats.skills}")
    print(f"Frameworks:          {stats.frameworks}")
    print(f"Commands:            {stats.commands}")
    print(f"Templates:           {stats.templates}")
    print(f"Checklists:          {stats.checklists}")
    print(f"Examples:            {stats.examples}")
    print(f"Python scripts:      {stats.python_scripts}")
    print(f"Repository size:     {human_size(stats.repository_size_bytes)}")
    print("\nLargest folders:")
    for entry in stats.largest_folders:
        print(f"- {entry.path:<24} {human_size(entry.bytes)}")
    print("\nLargest files:")
    for entry in stats.largest_files:
        print(f"- {entry.path:<48} {human_size(entry.bytes)}")


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""

    parser = argparse.ArgumentParser(description="Generate AI Engineer Pack repository statistics.")
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root to inspect.")
    parser.add_argument("--top", type=int, default=10, help="Number of largest files and folders to show.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run statistics reporting and return an exit code."""

    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s: %(message)s")
    root = args.root.resolve()
    if not root.exists():
        LOGGER.error("Repository root does not exist: %s", root)
        return 1
    stats = collect_stats(root, top=args.top)
    if args.json:
        print(json.dumps(asdict(stats), indent=2))
    else:
        print_stats(stats)
    return 0


if __name__ == "__main__":
    sys.exit(main())



