# Microsoft AutoGen Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Tools and permissions are explicit.
- [ ] Stop conditions and escalation paths are defined.
- [ ] State, memory, and retention are documented.

## Testing readiness
- [ ] Test tools, simulate team transcripts, assert termination, test Docker executor isolation, and replay failed conversations.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.

## Deployment readiness
- [ ] Deploy with pinned versions, isolated execution containers, model configuration management, logs, metrics, and human fallback for non-terminating runs.
- [ ] Logs or traces are available.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A disable or rollback path exists.

## Security readiness
- [ ] Sandbox code execution, authenticate local control planes, restrict file/network access, and never let browser-derived content issue privileged commands.
- [ ] Secrets are protected.
- [ ] Human approval is required for high-impact writes.
