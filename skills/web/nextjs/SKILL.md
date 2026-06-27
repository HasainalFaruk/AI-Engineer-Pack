# Next.js Skill Definition

## Capability
Use this skill for routing, server and client components, data fetching, caching, middleware, API routes, and deployment behavior. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with build checks, route smoke tests, server/client boundary checks, metadata validation, and cache behavior tests.

## Best for
- Designing or modifying Next.js-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Next.js tooling or runtime behavior.
- Creating prompts or workflows that require accurate Next.js terminology.

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
Avoid misplaced client components, stale caches, secret leakage to the browser, and dynamic routes without loading or error states.

