# WordPress Skill Definition

## Capability
Use this skill for themes, plugins, hooks, shortcodes, Gutenberg blocks, custom post types, and secure admin workflows. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with local WordPress smoke tests, PHP linting, nonce checks, role checks, and plugin activation tests.

## Best for
- Designing or modifying WordPress-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on WordPress tooling or runtime behavior.
- Creating prompts or workflows that require accurate WordPress terminology.

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
Avoid missing escaping, missing nonces, direct database queries, global state surprises, and update-unsafe customizations.

