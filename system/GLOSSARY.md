# Glossary

This glossary defines common terms used in the AI Engineer Pack.

Use it with all system documents, especially [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md), [THINKING_MODEL.md](THINKING_MODEL.md), and [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md).

## Agent

An AI system that can reason about a task, use tools, edit files, run commands, and communicate with the user.

## AI Engineer Pack

A set of system documents that define how an AI coding agent should behave, reason, communicate, write code, test work, handle security, and maintain documentation.

## Boundary

A point where data, control, or responsibility crosses from one context to another. Examples include API endpoints, file inputs, user forms, database calls, service calls, and command-line arguments.

## Breaking Change

A change that can cause existing users, integrations, tests, workflows, or documented behavior to fail unless they adapt. See [VERSIONING.md](VERSIONING.md).

## Contract

An expected interface or behavior between systems, modules, or users. Contracts may be formal, such as API schemas, or informal, such as documented CLI behavior.

## Done

The state where the requested outcome is implemented, validated, documented when needed, and communicated clearly to the user.

## Idempotent

Safe to run more than once with the same intended effect. Idempotency is important for retries, migrations, scripts, and distributed systems.

## Invariant

A condition that should always remain true. For example, an order total should not be negative, and a user should not access another tenant's private data.

## Observability

The ability to understand system behavior from outputs such as logs, metrics, traces, audit records, and error reports.

## Production-Quality

Work that is suitable for real users or maintainers because it is correct, maintainable, secure, tested appropriately, and documented where needed.

## Regression

A bug where previously working behavior stops working after a change.

## Regression Test

A test added or updated to prove that a fixed bug does not return.

## Risk

The possibility that a change may cause harm, failure, data loss, security exposure, user confusion, or operational cost.

## Scope

The intended boundary of a task or change. Good scope is narrow enough to complete safely and broad enough to solve the actual problem.

## Trust Boundary

A boundary where data crosses from an untrusted or less trusted source into a trusted system. Trust boundaries require validation and security review. See [SECURITY_RULES.md](SECURITY_RULES.md).

## Validation

The act of checking that work behaves as intended. Validation may include tests, builds, linting, type checks, manual inspection, or runtime verification.

## Verification

Evidence that the completed work satisfies the requested outcome. Verification should be reported in the final response according to [OUTPUT_FORMAT.md](OUTPUT_FORMAT.md).
