# OWASP Web Security Skill Definition

## Capability
Use this skill for web application risks including injection, XSS, CSRF, authentication, access control, and secure headers. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with threat checks, security tests, dependency scanning, header review, and abuse-case testing.

## Best for
- Designing or modifying OWASP Web Security-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on OWASP Web Security tooling or runtime behavior.
- Creating prompts or workflows that require accurate OWASP Web Security terminology.

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
Avoid trusting client input, missing authorization checks, weak session handling, and output without escaping.

