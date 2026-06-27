# Microsoft AutoGen Best Practices

## Design
- Pin package versions, isolate code execution, define agent termination rules, use typed messages, and keep team topology small.
- Keep work scoped to one clear outcome.
- Define stop conditions and escalation rules.

## Reliability
- Test failure paths and tool errors.
- Keep run logs or traces for review.
- Use small tasks before long-running automations.

## Security
- Sandbox code execution, authenticate local control planes, restrict file/network access, and never let browser-derived content issue privileged commands.
- Avoid exposing secrets in prompts, logs, traces, or memory.
- Require human approval for high-impact actions.

## Operations
- Track latency, cost, tool errors, and human override rate.
- Version instructions and evaluation examples.
- Maintain rollback or disable paths.
