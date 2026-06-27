# Versioning

This document defines versioning and change-management guidance for the AI Engineer Pack and software projects maintained with it.

Use it with [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md), [DOCUMENTATION_STYLE.md](DOCUMENTATION_STYLE.md), and [CODING_STANDARDS.md](CODING_STANDARDS.md).

## Purpose

Versioning helps users understand compatibility, upgrade risk, and release history.

AI engineering agents should treat version changes as communication with future maintainers.

## Semantic Versioning

When a project follows semantic versioning, use:

- Major version for breaking changes.
- Minor version for backward-compatible features.
- Patch version for backward-compatible fixes.

Example:

```text
1.4.2
```

In this example:

- `1` is the major version.
- `4` is the minor version.
- `2` is the patch version.

## Breaking Changes

A breaking change may include:

- Removing or renaming public APIs.
- Changing API response shapes.
- Changing configuration keys.
- Changing required environment variables.
- Altering database schemas without backward compatibility.
- Removing CLI flags.
- Changing authentication or authorization requirements.
- Changing documented behavior that consumers rely on.

Breaking changes must be documented clearly and should include migration guidance.

## Changelog Entries

Use changelogs to summarize user-visible changes.

Recommended categories:

- Added.
- Changed.
- Deprecated.
- Removed.
- Fixed.
- Security.

Example:

```text
## 2.3.0

### Added
- Added CSV export for invoice reports.

### Fixed
- Fixed incorrect totals for invoices with multiple discounts.
```

## Deprecation Policy

When removing or replacing behavior:

1. Mark it deprecated.
2. Provide the replacement.
3. State when removal will occur if known.
4. Add warnings where appropriate.
5. Document migration steps.

Avoid silent removal of behavior that users or integrations may depend on.

## Database And Data Versions

For schema changes:

- Use migrations rather than manual instructions when possible.
- Make migrations reversible when practical.
- Consider backfill cost and locking behavior.
- Preserve data during rollbacks where possible.
- Test migration and rollback paths for high-risk changes.

## API Versions

For APIs:

- Document request and response changes.
- Preserve backward compatibility where possible.
- Use explicit versioning when supported.
- Include examples for new or changed fields.
- Avoid reusing fields with changed meaning.

## Agent Responsibilities

When making changes, the agent should:

- Detect whether version files, changelogs, release notes, or package manifests need updates.
- Avoid changing versions unless requested or clearly part of the task.
- Document compatibility impact.
- Flag breaking changes.
- Follow repository release conventions.

## Versioning Checklist

- Does this change affect public behavior?
- Is the change backward-compatible?
- Does the changelog need an entry?
- Do docs mention the correct version?
- Are migrations required?
- Are API examples updated?
- Is rollback behavior understood?
