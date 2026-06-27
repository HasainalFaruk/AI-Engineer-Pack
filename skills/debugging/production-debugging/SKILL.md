# Production Debugging Skill Definition

## Capability
Use this skill for live incident diagnosis using logs, metrics, traces, feature flags, rollbacks, and customer impact analysis. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with timeline reconstruction, metric correlation, safe probes, rollback validation, and post-incident regression checks.

## Best for
- Designing or modifying Production Debugging-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Production Debugging tooling or runtime behavior.
- Creating prompts or workflows that require accurate Production Debugging terminology.

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
Avoid making risky live changes, trusting one signal, no incident timeline, missing customer impact, and no follow-up prevention.

