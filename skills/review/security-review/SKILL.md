# Security Review Skill Definition

## Capability
Use this skill for threats, sensitive data, access control, secrets, dependency risk, input validation, and abuse cases. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with threat model pass, secret scan review, dependency checks, auth tests, and exploit-oriented test cases.

## Best for
- Designing or modifying Security Review-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Security Review tooling or runtime behavior.
- Creating prompts or workflows that require accurate Security Review terminology.

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
Avoid checking only dependencies, missing authorization paths, ignoring logs, and treating authentication as complete security.

