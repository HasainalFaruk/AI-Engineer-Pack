# Java Skill Definition

## Capability
Use this skill for JVM services, Spring-style applications, Maven or Gradle builds, concurrency, and typed domain models. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with unit tests, integration tests, static analysis, build lifecycle checks, and JVM runtime smoke tests.

## Best for
- Designing or modifying Java-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Java tooling or runtime behavior.
- Creating prompts or workflows that require accurate Java terminology.

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
Avoid over-abstracted class hierarchies, unchecked nulls, blocking calls in async paths, and untested serialization.

