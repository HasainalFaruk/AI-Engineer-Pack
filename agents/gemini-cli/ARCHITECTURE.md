# Gemini CLI Architecture

## Runtime model
A terminal agent session combines Gemini models, project context files such as GEMINI.md, built-in tools, MCP servers, authentication, checkpointing, and optional GitHub Action integration.

## Core components
- Model and instruction layer.
- Tool and integration layer.
- State, memory, and trace layer.
- Routing, approval, retry, and termination layer.
- Evaluation and deployment layer.

## Production boundaries
Keep privileged actions behind explicit approval and deterministic policy checks. Record enough state and trace information to explain a run after the fact.

## Architecture checklist
- [ ] Agent roles and responsibilities are narrow.
- [ ] Tool permissions are explicit.
- [ ] State and memory rules are documented.
- [ ] Human approval exists for risky actions.
- [ ] Observability exists for decisions and tool calls.
