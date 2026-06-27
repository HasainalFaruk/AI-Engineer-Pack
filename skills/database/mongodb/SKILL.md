# MongoDB Skill Definition

## Capability
Use this skill for document modeling, indexes, aggregation pipelines, schema validation, and operational query patterns. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with index explain plans, aggregation tests, fixture-backed queries, and migration sampling.

## Best for
- Designing or modifying MongoDB-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on MongoDB tooling or runtime behavior.
- Creating prompts or workflows that require accurate MongoDB terminology.

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
Avoid unbounded collections scans, inconsistent document shapes, oversized documents, and missing compound indexes.

