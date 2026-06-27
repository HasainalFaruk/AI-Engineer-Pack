# Browser DevTools Skill Definition

## Capability
Use this skill for frontend runtime debugging with console, network, performance, accessibility, storage, and layout tooling. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with console error review, network trace inspection, performance profiles, DOM checks, and device emulation.

## Best for
- Designing or modifying Browser DevTools-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Browser DevTools tooling or runtime behavior.
- Creating prompts or workflows that require accurate Browser DevTools terminology.

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
Avoid debugging minified output only, ignoring network failures, changing CSS blindly, and not reproducing on target viewport.

