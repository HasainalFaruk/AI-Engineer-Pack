# MCP Resources Checklist

## Purpose
Use this checklist before merging or releasing mcp resources documentation or implementation work.

## Readiness checklist
- [ ] The design explicitly covers URI design, metadata, freshness, subscriptions, read-time authorization.
- [ ] Capability descriptions are narrow, accurate, and reviewed as model-facing API surfaces.
- [ ] JSON-RPC request, response, notification, and error behavior is represented in tests.
- [ ] Authentication and authorization are enforced at the server boundary where external systems are reached.
- [ ] Side-effecting operations require host policy, user consent, dry-run mode, or an equivalent control.
- [ ] Logs include request identifiers, method names, latency, status, and sanitized errors.

## Security checklist
- [ ] Authentication and authorization behavior is documented.
- [ ] Sensitive data is filtered, minimized, and redacted from logs.
- [ ] Tool descriptions, resource content, and prompt text are reviewed for injection risk.
- [ ] Human approval or host policy covers expensive, privileged, or mutating operations.
- [ ] Error messages are useful without exposing secrets or internal-only details.

## Testing checklist
- [ ] JSON-RPC initialization, discovery, success, error, cancellation, and timeout paths are tested.
- [ ] OpenAI and Claude usage assumptions are represented in examples or fixtures where relevant.
- [ ] Performance budgets exist for latency, payload size, and concurrency.
- [ ] Documentation links resolve and examples match the current module structure.

## Release checklist
- [ ] Owners, support path, deployment target, and rollback plan are known.
- [ ] Observability includes request identifiers, method names, duration, status, and sanitized failure details.
- [ ] Versioning and compatibility expectations are clear to clients and server operators.
