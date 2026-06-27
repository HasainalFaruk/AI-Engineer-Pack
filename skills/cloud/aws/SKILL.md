# AWS Skill Definition

## Capability
Use this skill for IAM, Lambda, ECS, S3, RDS, CloudWatch, networking, cost controls, and deployment architecture. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with IAM policy review, infrastructure plan checks, log and metric validation, least privilege review, and cost estimation.

## Best for
- Designing or modifying AWS-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on AWS tooling or runtime behavior.
- Creating prompts or workflows that require accurate AWS terminology.

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
Avoid wildcard IAM, public buckets, missing alarms, region drift, and untagged cost centers.

