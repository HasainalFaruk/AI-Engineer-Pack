# Drupal Skill Definition

## Capability
Use this skill for modules, entities, fields, routes, permissions, configuration export, and content modeling. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with cache rebuilds, config import/export checks, permission tests, and module install smoke tests.

## Best for
- Designing or modifying Drupal-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Drupal tooling or runtime behavior.
- Creating prompts or workflows that require accurate Drupal terminology.

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
Avoid hard-coded config, missing access callbacks, cache metadata mistakes, and update hooks without rollback thinking.

