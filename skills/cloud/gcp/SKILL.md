# Google Cloud Skill Definition

## Capability
Use this skill for Cloud Run, Cloud Functions, IAM, Pub/Sub, Cloud SQL, storage, logging, and project-level governance. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with IAM review, deployment smoke tests, service account checks, log-based metrics, and budget alert review.

## Best for
- Designing or modifying Google Cloud-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Google Cloud tooling or runtime behavior.
- Creating prompts or workflows that require accurate Google Cloud terminology.

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
Avoid default service account misuse, public storage, missing concurrency limits, and project sprawl.

