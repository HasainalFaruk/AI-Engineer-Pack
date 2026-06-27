# LangGraph Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Agent responsibilities are narrow and testable.
- [ ] Tool permissions follow least privilege.
- [ ] State, memory, and retention are documented.

## Testing readiness
- [ ] Unit-test nodes, integration-test graph paths, test checkpoint resume, test interrupts, and replay traces for regressions.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.
- [ ] Regression examples exist for known failures.

## Deployment readiness
- [ ] Deploy with persistent storage, versioned state schemas, observability, backpressure, and safe migration plans for active runs.
- [ ] Logs or traces are available for review.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A rollback or disable path exists.

## Security readiness
- [ ] Sanitize state, protect checkpoint stores, restrict tools per node, review human-interrupt surfaces, and redact trace payloads.
- [ ] Secrets are not exposed to prompts, memory, traces, or logs.
- [ ] Human approval is required for high-impact writes.
