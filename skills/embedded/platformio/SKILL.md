# PlatformIO Skill Definition

## Capability
Use this skill for multi-board embedded projects, library dependencies, build environments, upload targets, and test automation. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with pio run, environment matrix builds, library lock review, upload smoke tests, and unit tests where available.

## Best for
- Designing or modifying PlatformIO-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on PlatformIO tooling or runtime behavior.
- Creating prompts or workflows that require accurate PlatformIO terminology.

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
Avoid environment drift, board mismatch, unpinned libraries, hidden upload settings, and missing serial diagnostics.

