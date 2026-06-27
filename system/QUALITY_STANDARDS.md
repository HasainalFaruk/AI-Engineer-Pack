# Quality Standards

This document defines quality expectations for AI-assisted engineering work.

Use it with [CODING_STANDARDS.md](CODING_STANDARDS.md), [SECURITY_RULES.md](SECURITY_RULES.md), [VERSIONING.md](VERSIONING.md), and [DOCUMENTATION_STYLE.md](DOCUMENTATION_STYLE.md).

## Definition Of Quality

High-quality engineering work is correct, maintainable, secure, observable, and validated.

A change is not production-quality merely because it compiles. It should behave correctly under realistic conditions and fit the system around it.

## Quality Dimensions

Evaluate changes across:

- Correctness.
- Reliability.
- Maintainability.
- Security.
- Performance.
- Usability.
- Accessibility.
- Observability.
- Testability.
- Compatibility.

Not every task needs equal depth in every dimension, but every task should consider them.

## Correctness

Correct work satisfies the user's requested behavior and preserves existing behavior unless intentionally changed.

Check:

- Happy path behavior.
- Empty, missing, malformed, and boundary inputs.
- Error cases.
- Permission and role differences.
- Time zone and date behavior.
- Concurrency and retry behavior when relevant.

## Reliability

Reliable systems fail predictably.

Prefer:

- Idempotent operations where possible.
- Safe retries.
- Timeouts for external calls.
- Clear fallback behavior.
- Durable state transitions.
- Explicit transaction boundaries.

Avoid:

- Partial writes without recovery.
- Infinite retries.
- Silent failure.
- Unbounded queues or memory growth.

## Maintainability

Maintainable changes are easy for future engineers to understand and modify.

Check:

- Is the design simpler than the problem requires?
- Are responsibilities clear?
- Is logic duplicated?
- Are names domain-appropriate?
- Are comments useful and sparse?
- Does the change respect module boundaries?

## Test Strategy

Use the smallest test that proves the behavior, then expand based on risk.

Recommended layers:

- Unit tests for pure logic.
- Integration tests for component boundaries.
- Contract tests for external interfaces.
- End-to-end tests for critical user flows.
- Manual verification for visual or operational behavior when automation is unavailable.

Tests should be deterministic, isolated, and meaningful.

## Review Checklist

Before considering a change complete:

- The requested behavior is implemented.
- Existing behavior remains compatible or changes are documented.
- Important edge cases are tested.
- Error paths are handled.
- Security implications are reviewed.
- Observability is adequate for production debugging.
- Documentation is updated when the user or future maintainer needs it.
- Validation commands have been run or limitations are stated.

## Observability

Production systems should make important behavior visible without leaking sensitive data.

Consider:

- Structured logs.
- Metrics.
- Tracing.
- Audit events.
- Error reporting.
- User-safe diagnostics.

Logs should identify what happened, where, and why it matters. They should not include secrets, tokens, passwords, full payment data, or unnecessary personal data.

## Compatibility

Protect compatibility for:

- Public APIs.
- Database schemas.
- Serialized formats.
- Configuration files.
- CLI arguments.
- Environment variables.
- Webhooks.
- Message queues.

Breaking changes should be versioned and documented according to [VERSIONING.md](VERSIONING.md).

## Performance Quality

Performance changes should be evidence-based.

Check:

- Avoiding obvious N+1 queries.
- Reducing unnecessary network calls.
- Bounding expensive loops.
- Using indexes and pagination for large data.
- Avoiding blocking work on critical paths.
- Measuring before complex optimization.

## Production Readiness Checklist

- Behavior is implemented and tested.
- Error handling is intentional.
- Security review is complete for touched areas.
- Performance risk is acceptable.
- Observability is sufficient.
- Documentation and release notes are updated if needed.
- Rollback or mitigation path is understood for risky changes.
