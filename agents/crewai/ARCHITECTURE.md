# CrewAI Architecture

## Runtime model
Agents have roles, goals, backstories, tools, and memory; tasks describe work and outputs; crews coordinate agents; flows provide more controlled event-driven orchestration.

## Core components
- Model layer: model selection, context limits, cost profile, and provider configuration.
- Instruction layer: stable system instructions, task prompts, memory policy, and output contracts.
- Tool layer: typed functions, MCP servers, shell access, browser or file tools, and external services.
- State layer: sessions, checkpoints, memory, traces, artifacts, and run metadata.
- Control layer: routing, handoffs, termination rules, retries, and human approval gates.

## Production boundaries
Keep deterministic business rules in code and use the agent for judgment-heavy work. Treat model output as untrusted until validated by schemas, tests, policies, or human review.

## Integration points
Integrate with repository instructions, CI checks, observability, secrets management, evaluation datasets, and deployment rollback controls.

## Architecture checklist
- [ ] Agent responsibilities are narrow and reviewable.
- [ ] Tool permissions are explicit and least-privilege.
- [ ] State and memory ownership are documented.
- [ ] Human review exists for high-impact actions.
- [ ] Traces or logs explain every tool call and final decision.
