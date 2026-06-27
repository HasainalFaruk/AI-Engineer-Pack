# CrewAI Best Practices

## Design
- Write measurable task outputs, keep agent roles non-overlapping, prefer flows for controlled automation, and use guardrails for final artifacts.
- Define ownership, state, and stop conditions before adding tools.
- Keep prompts modular: role, context, policy, task, and output contract.

## Reliability
- Test tool failures, malformed outputs, timeout paths, and retry behavior.
- Record traces that show model inputs, tool calls, outputs, and final decisions.
- Prefer deterministic code for business rules.

## Security
- Scope tools by role, protect trigger payloads, audit automation runs, avoid sensitive data in memory, and enforce human approval for external writes.
- Use least privilege for every tool and integration.
- Redact secrets from prompts, logs, traces, memory, and artifacts.

## Operations
- Track cost, latency, tool error rate, handoff rate, and human override rate.
- Version prompts and evaluation sets with the same care as code.
- Require rollback or disable switches for production automations.
