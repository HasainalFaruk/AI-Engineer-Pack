# Multi-Agent Systems Architecture

## Runtime model
A multi-agent system defines roles, communication channels, shared or partitioned state, tools, memory, routing rules, human checkpoints, and recovery behavior across multiple agents.

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

## Multi-Agent Patterns

### Supervisor Pattern
Centralizes routing, risk decisions, final synthesis, and stop conditions.

### Planner Pattern
Creates task decomposition, dependencies, acceptance criteria, and work packages.

### Executor Pattern
Runs bounded tasks with specific tools and returns evidence-backed outputs.

### Reviewer Pattern
Checks outputs for correctness, safety, completeness, and policy compliance.

### Memory Pattern
Separates short-term task state from durable memory and defines retention rules.

### Routing Pattern
Classifies work and sends it to the right specialist with observable rationale.

### Human-in-the-loop
Adds explicit approval gates for ambiguity, policy exceptions, and high-impact actions.

### Tool Calling
Scopes tools per role, validates arguments, records tool calls, and handles rollback.

### Agent Communication
Uses structured messages instead of informal chat for critical handoffs.

### State Management
Versions state schemas, checkpoints long tasks, and protects shared state.

### Failure Recovery
Defines retry limits, fallback agents, human escalation, rollback, and incident review.
