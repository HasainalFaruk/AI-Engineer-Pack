# Docker Skill Definition

## Capability
Use this skill for Dockerfiles, compose environments, image size, build caching, runtime users, and local reproducibility. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with docker build, compose smoke tests, image inspection, health checks, and dependency cache validation.

## Best for
- Designing or modifying Docker-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Docker tooling or runtime behavior.
- Creating prompts or workflows that require accurate Docker terminology.

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
Avoid running as root, copying secrets, bloated layers, missing health checks, and dev-only settings in production images.

