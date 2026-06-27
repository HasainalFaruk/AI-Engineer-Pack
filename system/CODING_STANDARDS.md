# Coding Standards

This document defines coding standards for AI engineering agents. It is language-agnostic by default and should be adapted to the conventions of the current repository.

Use it with [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md), [SECURITY_RULES.md](SECURITY_RULES.md), and [VERSIONING.md](VERSIONING.md).

## Core Principles

Code should be:

- Correct.
- Readable.
- Maintainable.
- Testable.
- Secure by default.
- Consistent with the surrounding codebase.

Prefer boring, well-understood patterns over cleverness.

## Local Consistency

Before writing code, inspect nearby files for:

- Naming conventions.
- Error handling style.
- Dependency injection patterns.
- Logging conventions.
- Test structure.
- Formatting rules.
- Data validation boundaries.

Match the project unless there is a clear reason not to.

## Simplicity

Choose the smallest design that solves the actual problem.

Prefer:

- Straight-line code for simple workflows.
- Standard library features where adequate.
- Existing project utilities.
- Explicit data flow.
- Small functions with clear names.

Avoid:

- Premature frameworks.
- Hidden global state.
- Deep inheritance for ordinary composition.
- Over-generalized helpers.
- Large rewrites for narrow fixes.

## Naming

Names should describe intent and domain meaning.

Good:

```text
calculateInvoiceTotal
refreshAccessToken
isPasswordResetExpired
```

Poor:

```text
doStuff
handleData
newThing
```

Use abbreviations only when common in the project or domain.

## Error Handling

Errors should be actionable and safe.

- Validate input at boundaries.
- Preserve useful context.
- Avoid swallowing exceptions silently.
- Do not expose secrets or sensitive internals in user-facing errors.
- Use typed or structured errors when the project supports them.
- Prefer explicit failure paths over ambiguous return values.

## Data Validation

Validate data from:

- Users.
- Network calls.
- Files.
- Environment variables.
- Databases when schema guarantees are insufficient.
- Third-party services.

Validation should happen at trust boundaries and should be covered by tests where behavior matters.

## State Management

Keep state:

- Minimal.
- Explicit.
- Scoped to the smallest reasonable owner.
- Safe under concurrency when applicable.

Avoid mutable shared state unless it is protected, documented, and tested.

## Dependencies

Before adding a dependency, check:

- The project may already provide the capability.
- The dependency is actively maintained.
- The license is acceptable.
- The package size and transitive risk are reasonable.
- The security posture is acceptable.

Do not add dependencies for trivial utilities.

## Comments

Comments should explain why, not restate what.

Good:

```text
// Keep this retry count below the provider's burst limit.
```

Poor:

```text
// Increment i by one.
```

Use comments for business rules, non-obvious constraints, compatibility decisions, and security-sensitive behavior.

## Tests

Add or update tests for:

- New behavior.
- Bug fixes.
- Edge cases.
- Security-sensitive logic.
- Public API changes.
- Data migrations and parsers.

See [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md) for broader validation expectations.

## Performance

Write efficient code where performance matters, but do not obscure simple logic without evidence.

Consider:

- Algorithmic complexity.
- Database query count.
- Network round trips.
- Memory use.
- Caching invalidation.
- Startup cost.

## Accessibility And Internationalization

For user interfaces:

- Use semantic markup where possible.
- Maintain keyboard navigation.
- Provide accessible labels.
- Preserve focus behavior.
- Do not encode user-facing strings in ways that prevent translation.
- Handle dates, numbers, time zones, and pluralization carefully.

## Coding Checklist

- The code follows local style.
- The change is scoped to the request.
- Inputs are validated.
- Errors are handled intentionally.
- Tests cover important behavior.
- Security rules were considered.
- Documentation was updated when needed.
