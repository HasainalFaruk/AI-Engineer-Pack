# GitHub Copilot Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Tools and permissions are explicit.
- [ ] Stop conditions and escalation paths are defined.
- [ ] State, memory, and retention are documented.

## Testing readiness
- [ ] Use CI, required checks, Copilot custom-agent tests, review comments, and security scanning before accepting agent changes.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.

## Deployment readiness
- [ ] Deploy through GitHub Actions or existing pipelines with branch protections, environment approvals, secrets policies, and audit trails.
- [ ] Logs or traces are available.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A disable or rollback path exists.

## Security readiness
- [ ] Enforce organization policies, restrict agent environments, manage MCP and secrets carefully, and review generated code for supply-chain risk.
- [ ] Secrets are protected.
- [ ] Human approval is required for high-impact writes.
