# Kubernetes Skill Definition

## Capability
Use this skill for deployments, services, ingress, config maps, secrets, probes, resources, autoscaling, and rollout safety. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with manifest validation, dry runs, probe checks, resource review, rollout status, and rollback plans.

## Best for
- Designing or modifying Kubernetes-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on Kubernetes tooling or runtime behavior.
- Creating prompts or workflows that require accurate Kubernetes terminology.

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
Avoid missing resource limits, weak probes, mutable latest tags, namespace confusion, and secret leakage.

