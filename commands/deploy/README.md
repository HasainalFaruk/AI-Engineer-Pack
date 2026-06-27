# Deploy Command

## Purpose
The deploy command prepares, executes, or documents the release of software to an environment. It emphasizes repeatability, safety, rollback, observability, and communication.

## Inputs
- Target environment and release scope.
- Build artifacts, configuration, migrations, secrets, and infrastructure requirements.
- Deployment procedure, approvals, and rollback expectations.
- Health checks, monitoring, and post-deploy validation criteria.

## Outputs
- Deployment plan, runbook, or automation changes.
- Preflight checklist and rollback strategy.
- Environment-specific verification steps.
- Release summary with status, checks, and follow-up items.

## Step-by-step workflow
1. Identify what is being released, where, and why.
2. Review dependencies, migrations, configuration, and operational risks.
3. Define preflight checks, deployment steps, validation checks, and rollback actions.
4. Confirm observability: logs, metrics, alerts, dashboards, and ownership.
5. Execute or document the deployment path according to repository conventions.
6. Validate the environment after release with health checks and user-facing smoke tests.
7. Record outcome, incidents, rollback readiness, and follow-up tasks.

## Best practices
- Make rollback explicit before deployment begins.
- Separate build, release, and runtime configuration concerns.
- Validate database migrations and backward compatibility.
- Use environment approvals for risky production changes.
- Communicate release status to affected stakeholders.

## Common mistakes
- Deploying without a rollback plan.
- Forgetting configuration, secrets, or migration order.
- Treating successful build as successful deployment.
- Skipping post-deploy monitoring.
- Making manual steps that are not documented for the next release.

## Example prompt
```text
Use the deploy command to prepare a production release plan for the billing API. Include preflight checks, migration safety, deployment steps, health checks, rollback, and communication notes.
```

## Example output
```text
Deployment plan ready for billing API.

Preflight:
- Confirm migration is backward compatible.
- Verify payment provider credentials in production.
- Run smoke tests against staging.

Rollback:
- Revert application image to previous tag.
- Leave additive database migration in place.

Post-deploy:
- Check billing job metrics and error logs for 30 minutes.
```

## Related skills
- [DevOps](../../skills/devops/README.md)
- [Cloud](../../skills/cloud/README.md)
- [Security](../../skills/security/README.md)
- [Testing](../../skills/testing/README.md)

## Related frameworks
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [BAB](../../frameworks/bab/README.md)
- [Reflection](../../frameworks/reflection/README.md)
- [ReAct](../../frameworks/react/README.md)
