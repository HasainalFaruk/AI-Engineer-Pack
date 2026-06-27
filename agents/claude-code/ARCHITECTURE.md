# Claude Code Architecture

## Runtime model
Claude Code sessions combine repository context, persistent instructions, permissions, tool access, memories, MCP connectors, hooks, skills, and surfaces such as CLI, IDE, desktop, browser, and CI.

## Components
- Model and context management.
- Instruction and policy layer.
- Tool, connector, or workspace layer.
- State, memory, trace, and artifact layer.
- Human review and escalation layer.

## Boundaries
Use deterministic code for rules, schemas, and policy enforcement. Let the agent handle reasoning, synthesis, triage, and tool selection only within explicit permissions.

## Integration points
Integrate with source control, CI, issue tracking, secrets management, observability, and evaluation suites.

## Architecture checklist
- [ ] Tool permissions are least-privilege.
- [ ] State and memory behavior are documented.
- [ ] Human approval exists for risky writes.
- [ ] Traces or logs support incident review.
