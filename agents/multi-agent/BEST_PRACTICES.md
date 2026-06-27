# Multi-Agent Systems Best Practices

## Design
- Start with two or three roles, make contracts explicit, centralize risk decisions, log all messages, and measure whether extra agents improve outcomes.
- Give each agent or workflow one accountable outcome.
- Keep prompts modular and testable.

## Reliability
- Test tool failures, timeouts, invalid outputs, and stop conditions.
- Preserve logs or traces for every production run.
- Use deterministic code for policy and schema validation.

## Security
- Scope tools per role, isolate memory, validate inter-agent messages, require approval for high-impact actions, and audit all communication.
- Protect credentials, memory, logs, traces, and generated artifacts.
- Require human approval for high-impact writes.

## Operations
- Track latency, cost, tool errors, routing accuracy, and escalation rates.
- Version prompts and evaluation sets.
- Maintain a disable path for production automation.
