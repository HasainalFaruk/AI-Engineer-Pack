# LangGraph Best Practices

## Design
- Define state schemas first, keep nodes pure where possible, make routing explicit, checkpoint long work, and trace every graph path.
- Define ownership, state, and stop conditions before adding tools.
- Keep prompts modular: role, context, policy, task, and output contract.

## Reliability
- Test tool failures, malformed outputs, timeout paths, and retry behavior.
- Record traces that show model inputs, tool calls, outputs, and final decisions.
- Prefer deterministic code for business rules.

## Security
- Sanitize state, protect checkpoint stores, restrict tools per node, review human-interrupt surfaces, and redact trace payloads.
- Use least privilege for every tool and integration.
- Redact secrets from prompts, logs, traces, memory, and artifacts.

## Operations
- Track cost, latency, tool error rate, handoff rate, and human override rate.
- Version prompts and evaluation sets with the same care as code.
- Require rollback or disable switches for production automations.
