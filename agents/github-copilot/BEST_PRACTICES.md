# GitHub Copilot Best Practices

## Design
- Maintain repository instructions, configure content exclusions, enforce branch protections, use automatic review carefully, and monitor usage metrics.
- Keep work scoped to one clear outcome.
- Define stop conditions and escalation rules.

## Reliability
- Test failure paths and tool errors.
- Keep run logs or traces for review.
- Use small tasks before long-running automations.

## Security
- Enforce organization policies, restrict agent environments, manage MCP and secrets carefully, and review generated code for supply-chain risk.
- Avoid exposing secrets in prompts, logs, traces, or memory.
- Require human approval for high-impact actions.

## Operations
- Track latency, cost, tool errors, and human override rate.
- Version instructions and evaluation examples.
- Maintain rollback or disable paths.
