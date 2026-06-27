# Node.js Debugging Skill Definition

## Capability
Use this skill for Node services, async call stacks, memory leaks, event loop delay, package issues, and server logs. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with targeted reproduction, log correlation, inspector sessions, heap snapshots, and integration tests.

## Best for
- Designing or modifying Node.js Debugging-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Node.js Debugging tooling or runtime behavior.
- Creating prompts or workflows that require accurate Node.js Debugging terminology.

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
Avoid swallowing promise rejections, ignoring event loop blocking, broad dependency upgrades, and missing env parity.

