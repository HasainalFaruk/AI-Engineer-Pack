# Claude Code Best Practices

## Design
- Write strong repository instructions, keep permission modes conservative, require tests, review diffs, and use hooks for formatting and validation.
- Keep work scoped to one clear outcome.
- Define stop conditions and escalation rules.

## Reliability
- Test failure paths and tool errors.
- Keep run logs or traces for review.
- Use small tasks before long-running automations.

## Security
- Protect secrets, restrict shell/network actions, use MCP servers deliberately, review generated commands, and avoid pasting sensitive customer data.
- Avoid exposing secrets in prompts, logs, traces, or memory.
- Require human approval for high-impact actions.

## Operations
- Track latency, cost, tool errors, and human override rate.
- Version instructions and evaluation examples.
- Maintain rollback or disable paths.
