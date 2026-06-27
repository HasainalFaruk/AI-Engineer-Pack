# Multi-Agent Systems Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Roles, tools, and permissions are explicit.
- [ ] Stop conditions and escalation paths are defined.
- [ ] State and memory rules are documented.

## Testing readiness
- [ ] Run scenario evals for each role, test handoffs, replay failed conversations, check state consistency, and red-team collusion or tool misuse.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.

## Deployment readiness
- [ ] Deploy with observability, queues, timeouts, budget caps, role-level permissions, and a kill switch for runaway coordination.
- [ ] Logs or traces are available.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A disable or rollback path exists.

## Security readiness
- [ ] Scope tools per role, isolate memory, validate inter-agent messages, require approval for high-impact actions, and audit all communication.
- [ ] Secrets are protected.
- [ ] Human approval is required for high-impact writes.
