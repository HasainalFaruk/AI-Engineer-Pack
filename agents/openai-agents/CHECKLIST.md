# OpenAI Agents SDK Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Agent responsibilities are narrow and testable.
- [ ] Tool permissions follow least privilege.
- [ ] State, memory, and retention are documented.

## Testing readiness
- [ ] Unit-test tools, run trace-backed scenario evals, test guardrail failures, simulate tool errors, and verify handoff paths with deterministic fixtures.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.
- [ ] Regression examples exist for known failures.

## Deployment readiness
- [ ] Ship behind an API or worker with secret management, tracing export, rate limits, retry policies, and approval gates for high-impact tools.
- [ ] Logs or traces are available for review.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A rollback or disable path exists.

## Security readiness
- [ ] Apply least privilege to tools, isolate sandbox workspaces, redact secrets in traces, validate MCP servers, and require human approval for writes or external actions.
- [ ] Secrets are not exposed to prompts, memory, traces, or logs.
- [ ] Human approval is required for high-impact writes.
