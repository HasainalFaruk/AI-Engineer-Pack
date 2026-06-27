# CrewAI Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Agent responsibilities are narrow and testable.
- [ ] Tool permissions follow least privilege.
- [ ] State, memory, and retention are documented.

## Testing readiness
- [ ] Test task outputs, mock tools, validate flow state, run golden examples, and review token/cost budgets per crew.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.
- [ ] Regression examples exist for known failures.

## Deployment readiness
- [ ] Deploy as scheduled or triggered automations with environment separation, secrets, observability, RBAC, and rollback plans.
- [ ] Logs or traces are available for review.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A rollback or disable path exists.

## Security readiness
- [ ] Scope tools by role, protect trigger payloads, audit automation runs, avoid sensitive data in memory, and enforce human approval for external writes.
- [ ] Secrets are not exposed to prompts, memory, traces, or logs.
- [ ] Human approval is required for high-impact writes.
