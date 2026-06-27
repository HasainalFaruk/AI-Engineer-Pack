# Event-Driven Architecture Skill Definition

## Capability
Use this skill for events, producers, consumers, schemas, idempotency, ordering, retries, and eventual consistency. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with schema compatibility checks, replay tests, idempotency tests, dead-letter handling, and observability review.

## Best for
- Designing or modifying Event-Driven Architecture-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Event-Driven Architecture tooling or runtime behavior.
- Creating prompts or workflows that require accurate Event-Driven Architecture terminology.

## Inputs
- User goal, acceptance criteria, and affected environment.
- Relevant source files, config files, dependencies, logs, or test output.
- Version constraints and deployment context.
- Security, performance, accessibility, reliability, or maintenance requirements.

## Outputs
- Focused plan, implementation, review, or debugging guidance.
- Technology-specific risks, tradeoffs, and verification steps.
- Updated docs or examples when behavior or usage changes.

## Watch for
Avoid ambiguous event names, no idempotency, hidden ordering assumptions, unbounded retries, and missing event ownership.

