# Azure Skill Definition

## Capability
Use this skill for Azure App Service, Functions, Entra ID, Storage, Key Vault, Monitor, networking, and resource groups. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with role assignment review, deployment plan checks, Key Vault access tests, logs, metrics, and health probes.

## Best for
- Designing or modifying Azure-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Azure tooling or runtime behavior.
- Creating prompts or workflows that require accurate Azure terminology.

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
Avoid overbroad roles, secrets in app settings, missing managed identities, and unclear resource ownership.

