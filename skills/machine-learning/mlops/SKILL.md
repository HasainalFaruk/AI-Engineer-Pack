# MLOps Skill Definition

## Capability
Use this skill for model lifecycle, experiment tracking, data validation, deployment, monitoring, drift detection, and rollback. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with reproducible pipeline runs, model registry checks, data contracts, monitoring alerts, and rollback drills.

## Best for
- Designing or modifying MLOps-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on MLOps tooling or runtime behavior.
- Creating prompts or workflows that require accurate MLOps terminology.

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
Avoid training-serving skew, unversioned data, no model lineage, missing drift alerts, and manual promotion steps.

