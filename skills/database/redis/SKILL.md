# Redis Skill Definition

## Capability
Use this skill for caching, queues, rate limits, locks, session stores, TTL strategy, and memory-sensitive data structures. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with TTL tests, concurrency checks, cache invalidation tests, memory review, and fallback behavior checks.

## Best for
- Designing or modifying Redis-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Redis tooling or runtime behavior.
- Creating prompts or workflows that require accurate Redis terminology.

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
Avoid cache stampedes, missing expirations, unsafe distributed locks, key collisions, and treating cache as source of truth.

