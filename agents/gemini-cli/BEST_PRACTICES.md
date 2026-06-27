# Gemini CLI Best Practices

## Design
- Use GEMINI.md for project guidance, checkpoint long sessions, keep shell commands reviewable, configure MCP deliberately, and run validation before accepting changes.
- Give each agent or workflow one accountable outcome.
- Keep prompts modular and testable.

## Reliability
- Test tool failures, timeouts, invalid outputs, and stop conditions.
- Preserve logs or traces for every production run.
- Use deterministic code for policy and schema validation.

## Security
- Protect OAuth or API credentials, restrict shell and file access, vet MCP servers, redact sensitive prompts, and avoid command execution from untrusted content.
- Protect credentials, memory, logs, traces, and generated artifacts.
- Require human approval for high-impact writes.

## Operations
- Track latency, cost, tool errors, routing accuracy, and escalation rates.
- Version prompts and evaluation sets.
- Maintain a disable path for production automation.
