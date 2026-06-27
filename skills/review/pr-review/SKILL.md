# Pull Request Review Skill Definition

## Capability
Use this skill for PR scope, changed files, linked issues, CI status, reviewer guidance, rollout risk, and merge readiness. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with CI review, diff review, acceptance criteria checks, documentation review, and release risk review.

## Best for
- Designing or modifying Pull Request Review-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Pull Request Review tooling or runtime behavior.
- Creating prompts or workflows that require accurate Pull Request Review terminology.

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
Avoid approving without reading related code, ignoring failing checks, scope creep, and no rollback thinking.

