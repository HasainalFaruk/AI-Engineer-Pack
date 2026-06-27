# PostgreSQL Skill Definition

## Capability
Use this skill for schema design, migrations, indexes, query plans, transactions, constraints, and JSONB usage. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with migration dry runs, EXPLAIN analysis, constraint tests, rollback review, and query regression checks.

## Best for
- Designing or modifying PostgreSQL-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on PostgreSQL tooling or runtime behavior.
- Creating prompts or workflows that require accurate PostgreSQL terminology.

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
Avoid missing indexes, unsafe locks, unbounded queries, weak constraints, and irreversible migrations.

