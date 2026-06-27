"""Run the AI Engineer Pack repository validation suite.

Usage examples:
    python scripts/validate.py
    python scripts/validate.py --json
    python scripts/validate.py --verbose

Exit codes:
    0: every validation passed
    1: one or more validations failed
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Sequence

LOGGER = logging.getLogger("validate")
REQUIRED_TOP_LEVEL_DIRS = [
    "system",
    "routers",
    "frameworks",
    "commands",
    "chatgpt",
    "codex",
    "mcp",
    "skills",
    "templates",
    "checklists",
    "examples",
    "docs",
    "scripts",
    ".github",
]
REQUIRED_SKILL_FILES = ["README.md", "SKILL.md", "WORKFLOW.md", "PROMPTS.md", "CHECKLIST.md", "EXAMPLES.md"]
REQUIRED_AGENT_FILES = ["README.md", "ARCHITECTURE.md", "WORKFLOW.md", "BEST_PRACTICES.md", "PROMPTS.md", "CHECKLIST.md", "EXAMPLES.md", "TROUBLESHOOTING.md", "RESOURCES.md"]
REQUIRED_MCP_FILES = ["README.md", "ARCHITECTURE.md", "WORKFLOW.md", "PROMPTS.md", "CHECKLIST.md", "EXAMPLES.md"]
REQUIRED_SCRIPTS = [
    "validate.py",
    "check_links.py",
    "check_placeholders.py",
    "stats.py",
    "generate_index.py",
    "search.py",
    "build_docs.py",
]
EXCLUDED_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", "upstream", "archive"}
CONTENT_DIRS = {"agents", "mcp", "frameworks", "commands", "skills", "templates", "checklists"}


@dataclass(frozen=True)
class ValidationResult:
    """Result for one validation group."""

    name: str
    passed: bool
    details: list[str]


def repository_root(start: Path | None = None) -> Path:
    """Return the repository root inferred from this script location."""

    if start is None:
        start = Path(__file__).resolve()
    return start.parents[1]


def iter_repo_files(root: Path) -> list[Path]:
    """Return repository files excluding external and cache folders."""

    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts):
            continue
        files.append(path)
    return files


def run_command(root: Path, command: list[str]) -> tuple[int, str]:
    """Run a validation command and return exit code plus combined output."""

    LOGGER.debug("Running command: %s", " ".join(command))
    completed = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    output = "\n".join(part for part in [completed.stdout.strip(), completed.stderr.strip()] if part)
    return completed.returncode, output


def validate_markdown_files(root: Path) -> ValidationResult:
    """Validate Markdown file readability and basic code-fence balance."""

    details: list[str] = []
    markdown_files = [path for path in iter_repo_files(root) if path.suffix.lower() == ".md"]
    for path in markdown_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            details.append(f"Non-UTF-8 Markdown file: {path.relative_to(root).as_posix()}")
            continue
        fence_count = text.count("```")
        if fence_count % 2 != 0:
            details.append(f"Unbalanced code fences: {path.relative_to(root).as_posix()}")
    if not markdown_files:
        details.append("No Markdown files found.")
    return ValidationResult("Markdown Files", not details, details or [f"Checked {len(markdown_files)} Markdown files."])


def validate_links(root: Path) -> ValidationResult:
    """Run the Markdown link checker."""

    code, output = run_command(root, [sys.executable, "scripts/check_links.py", "--root", str(root)])
    details = output.splitlines()[-20:] if output else []
    return ValidationResult("Links", code == 0, details or ["Link checker completed."])


def validate_placeholders(root: Path) -> ValidationResult:
    """Run the placeholder checker."""

    code, output = run_command(root, [sys.executable, "scripts/check_placeholders.py", "--root", str(root)])
    details = output.splitlines()[-20:] if output else []
    return ValidationResult("Placeholders", code == 0, details or ["Placeholder checker completed."])


def validate_missing_readme(root: Path) -> ValidationResult:
    """Ensure required folders include README.md files."""

    details: list[str] = []
    for folder in REQUIRED_TOP_LEVEL_DIRS:
        if not (root / folder / "README.md").exists():
            details.append(f"Missing README: {folder}/README.md")
    for parent in ["frameworks", "commands", "templates", "checklists"]:
        base = root / parent
        if base.exists():
            for child in base.iterdir():
                if child.is_dir() and not (child / "README.md").exists():
                    details.append(f"Missing README: {child.relative_to(root).as_posix()}/README.md")
    return ValidationResult("Missing README", not details, details or ["Required README files are present."])


def validate_required_files(root: Path) -> ValidationResult:
    """Ensure required script and skill files are present."""

    details: list[str] = []
    for script in REQUIRED_SCRIPTS:
        if not (root / "scripts" / script).exists():
            details.append(f"Missing script: scripts/{script}")
    skills_dir = root / "skills"
    if skills_dir.exists():
        for category in [path for path in skills_dir.iterdir() if path.is_dir()]:
            for required in REQUIRED_SKILL_FILES:
                if not (category / required).exists():
                    details.append(f"Missing category skill file: {category.relative_to(root).as_posix()}/{required}")
            for technology in [path for path in category.iterdir() if path.is_dir()]:
                for required in REQUIRED_SKILL_FILES:
                    if not (technology / required).exists():
                        details.append(f"Missing technology skill file: {technology.relative_to(root).as_posix()}/{required}")
    agent_dir = root / "agents"
    if agent_dir.exists():
        if not (agent_dir / "AGENT_INDEX.md").exists():
            details.append("Missing agent index: agents/AGENT_INDEX.md")
        for agent in [path for path in agent_dir.iterdir() if path.is_dir()]:
            for required in REQUIRED_AGENT_FILES:
                if not (agent / required).exists():
                    details.append(f"Missing agent file: {agent.relative_to(root).as_posix()}/{required}")
    mcp_dir = root / "mcp"
    if mcp_dir.exists():
        if not (mcp_dir / "MCP_INDEX.md").exists():
            details.append("Missing MCP index: mcp/MCP_INDEX.md")
        for module in [path for path in mcp_dir.iterdir() if path.is_dir()]:
            for required in REQUIRED_MCP_FILES:
                if not (module / required).exists():
                    details.append(f"Missing MCP file: {module.relative_to(root).as_posix()}/{required}")
    return ValidationResult("Missing Required Files", not details, details or ["Required scripts, skill files, and agent files are present."])


def validate_repository_structure(root: Path) -> ValidationResult:
    """Validate required top-level folders and generated docs."""

    details: list[str] = []
    for folder in REQUIRED_TOP_LEVEL_DIRS:
        if not (root / folder).is_dir():
            details.append(f"Missing top-level folder: {folder}/")
    generated_docs = ["AGENT_INDEX.md", "MCP_INDEX.md", "SKILL_INDEX.md", "FRAMEWORK_INDEX.md", "COMMAND_INDEX.md", "TEMPLATE_INDEX.md", "CHECKLIST_INDEX.md", "EXAMPLE_INDEX.md", "SYSTEM_INDEX.md", "SUMMARY.md"]
    for name in generated_docs:
        if not (root / "docs" / name).exists():
            details.append(f"Missing generated doc: docs/{name}")
    code, output = run_command(root, [sys.executable, "scripts/generate_index.py", "--root", str(root), "--check"])
    if code != 0:
        details.append("Generated indexes are stale or missing.")
        details.extend(output.splitlines()[-10:])
    code, output = run_command(root, [sys.executable, "scripts/build_docs.py", "--root", str(root), "--check"])
    if code != 0:
        details.append("Documentation summary is stale or incomplete.")
        details.extend(output.splitlines()[-10:])
    return ValidationResult("Repository Structure", not details, details or ["Repository structure and generated docs are valid."])


def validate_duplicate_files(root: Path) -> ValidationResult:
    """Detect duplicate file content among non-empty repository files."""

    hashes: dict[str, list[str]] = {}
    for path in iter_repo_files(root):
        if path.stat().st_size == 0:
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes.setdefault(digest, []).append(path.relative_to(root).as_posix())
    duplicates = [paths for paths in hashes.values() if len(paths) > 1]
    details = ["Duplicate content: " + ", ".join(paths) for paths in duplicates]
    return ValidationResult("Duplicate Files", not details, details or ["No duplicate file content detected."])


def validate_empty_files(root: Path) -> ValidationResult:
    """Detect empty files in the repository."""

    empty = [path.relative_to(root).as_posix() for path in iter_repo_files(root) if path.stat().st_size == 0]
    return ValidationResult("Empty Files", not empty, empty or ["No empty files detected."])


def validate_naming(root: Path) -> ValidationResult:
    """Validate lowercase hyphen naming for content module directories."""

    details: list[str] = []
    for base_name in CONTENT_DIRS:
        base = root / base_name
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_dir():
                continue
            name = path.name
            if not all(char.islower() or char.isdigit() or char == "-" for char in name):
                details.append(f"Directory should use lowercase hyphen naming: {path.relative_to(root).as_posix()}")
    return ValidationResult("Naming Convention", not details, details or ["Content directory names follow lowercase hyphen conventions."])


def validate_script_imports(root: Path) -> ValidationResult:
    """Compile Python scripts to verify imports and syntax."""

    code, output = run_command(root, [sys.executable, "-m", "compileall", "-q", "scripts"])
    return ValidationResult("Python Imports", code == 0, output.splitlines() or ["Python scripts compiled successfully."])


def validate_stats(root: Path) -> ValidationResult:
    """Run stats.py to confirm reporting works."""

    code, output = run_command(root, [sys.executable, "scripts/stats.py", "--root", str(root), "--json"])
    return ValidationResult("Repository Stats", code == 0, output.splitlines()[:3] if output else ["Repository stats generated."])


def run_validations(root: Path) -> list[ValidationResult]:
    """Run every validation group."""

    checks: list[Callable[[Path], ValidationResult]] = [
        validate_markdown_files,
        validate_links,
        validate_placeholders,
        validate_missing_readme,
        validate_required_files,
        validate_repository_structure,
        validate_duplicate_files,
        validate_empty_files,
        validate_naming,
        validate_script_imports,
        validate_stats,
    ]
    return [check(root) for check in checks]


def print_summary(results: list[ValidationResult]) -> None:
    """Print a human-readable validation summary."""

    for result in results:
        marker = "✓" if result.passed else "✗"
        print(f"{marker} {result.name}")
        if not result.passed:
            for detail in result.details[:20]:
                print(f"  - {detail}")
            if len(result.details) > 20:
                print(f"  - ... {len(result.details) - 20} more")
    print()
    print("PASS" if all(result.passed for result in results) else "FAIL")


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""

    parser = argparse.ArgumentParser(description="Run the AI Engineer Pack validation suite.")
    parser.add_argument("--root", type=Path, default=repository_root(), help="Repository root to validate.")
    parser.add_argument("--json", action="store_true", help="Print JSON output.")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run repository validation and return an exit code."""

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s: %(message)s")
    root = args.root.resolve()
    if not root.exists():
        LOGGER.error("Repository root does not exist: %s", root)
        return 1
    results = run_validations(root)
    if args.json:
        print(json.dumps([asdict(result) for result in results], indent=2))
    else:
        print_summary(results)
    return 0 if all(result.passed for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())



