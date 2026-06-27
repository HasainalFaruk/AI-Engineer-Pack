# Code Review Skill Definition

## Capability
Use this skill for source changes, behavior risk, maintainability, test coverage, security implications, and actionable feedback. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with diff inspection, requirement comparison, targeted test review, and severity-ranked findings.

## Best for
- Designing or modifying Code Review-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Code Review tooling or runtime behavior.
- Creating prompts or workflows that require accurate Code Review terminology.

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
Avoid style-only reviews, vague comments, missed edge cases, no line references, and ignoring tests.

