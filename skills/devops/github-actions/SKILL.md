# GitHub Actions Skill Definition

## Capability
Use this skill for CI workflows, job permissions, caching, matrices, artifacts, environments, and release automation. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with workflow syntax checks, least-privilege permissions, cache key review, branch trigger checks, and dry-run reasoning.

## Best for
- Designing or modifying GitHub Actions-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on GitHub Actions tooling or runtime behavior.
- Creating prompts or workflows that require accurate GitHub Actions terminology.

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
Avoid overbroad tokens, flaky caches, unpinned actions, skipped required checks, and secrets exposed in logs.

