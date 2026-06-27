# Secrets Management Skill Definition

## Capability
Use this skill for secret storage, rotation, environment configuration, vault integration, CI/CD secrets, and leak prevention. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with secret scanning, least-privilege access review, rotation runbooks, local env checks, and CI log review.

## Best for
- Designing or modifying Secrets Management-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Secrets Management tooling or runtime behavior.
- Creating prompts or workflows that require accurate Secrets Management terminology.

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
Avoid committed secrets, broad secret access, no rotation path, secrets in logs, and mixing dev and prod credentials.

