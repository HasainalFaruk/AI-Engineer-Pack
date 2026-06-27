# Claude Code Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Tools and permissions are explicit.
- [ ] Stop conditions and escalation paths are defined.
- [ ] State, memory, and retention are documented.

## Testing readiness
- [ ] Run project test suites, lint, type checks, and task-specific smoke tests; verify that hooks and CI reproduce local results.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.

## Deployment readiness
- [ ] Use CI/CD integrations for review and automation, never deploy directly without human approval, and use scheduled tasks only with scoped permissions.
- [ ] Logs or traces are available.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A disable or rollback path exists.

## Security readiness
- [ ] Protect secrets, restrict shell/network actions, use MCP servers deliberately, review generated commands, and avoid pasting sensitive customer data.
- [ ] Secrets are protected.
- [ ] Human approval is required for high-impact writes.
