# Gemini CLI Checklist

## Design readiness
- [ ] Purpose and non-goals are documented.
- [ ] Roles, tools, and permissions are explicit.
- [ ] Stop conditions and escalation paths are defined.
- [ ] State and memory rules are documented.

## Testing readiness
- [ ] Run project tests, validate shell output, compare checkpoints, test MCP integrations, and review GitHub Action behavior on pull requests.
- [ ] Unsafe requests are rejected or escalated.
- [ ] Tool failures and timeouts are covered.

## Deployment readiness
- [ ] Use through CI or terminal workflows with explicit secrets, restricted permissions, and human approval for merges or production changes.
- [ ] Logs or traces are available.
- [ ] Cost, latency, and error budgets are defined.
- [ ] A disable or rollback path exists.

## Security readiness
- [ ] Protect OAuth or API credentials, restrict shell and file access, vet MCP servers, redact sensitive prompts, and avoid command execution from untrusted content.
- [ ] Secrets are protected.
- [ ] Human approval is required for high-impact writes.
