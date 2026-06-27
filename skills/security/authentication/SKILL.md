# Authentication Skill Definition

## Capability
Use this skill for login flows, sessions, tokens, password reset, MFA, identity providers, and account recovery. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with token expiry tests, session invalidation checks, rate limit tests, MFA flows, and replay protection review.

## Best for
- Designing or modifying Authentication-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Authentication tooling or runtime behavior.
- Creating prompts or workflows that require accurate Authentication terminology.

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
Avoid long-lived tokens, weak reset flows, missing lockout, insecure cookies, and confusing authentication with authorization.

