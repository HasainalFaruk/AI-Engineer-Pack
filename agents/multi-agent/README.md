# Multi-Agent Systems

## Purpose
Multi-Agent Systems helps teams design, govern, test, and operate systems where multiple specialized agents coordinate toward a shared outcome.


## Folder contents
- [Architecture](ARCHITECTURE.md)
- [Workflow](WORKFLOW.md)
- [Best Practices](BEST_PRACTICES.md)
- [Prompts](PROMPTS.md)
- [Checklist](CHECKLIST.md)
- [Examples](EXAMPLES.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Resources](RESOURCES.md)

## Architecture
A multi-agent system defines roles, communication channels, shared or partitioned state, tools, memory, routing rules, human checkpoints, and recovery behavior across multiple agents.

## Installation
Use the runtime that matches your stack: OpenAI Agents SDK, LangGraph, CrewAI, AutoGen, Claude Code, GitHub Copilot, or Gemini CLI.

## When to use
Use when work naturally decomposes into specialist roles, independent subtasks, review loops, or human-governed execution stages.

## When NOT to use
Avoid when one well-instructed agent or deterministic workflow is simpler, cheaper, safer, and easier to test.

## Capabilities
Supervision, planning, execution, review, memory, routing, human-in-the-loop, tool calling, agent communication, state management, and failure recovery.

## Limitations
Coordination overhead, higher latency and cost, emergent failures, difficult debugging, and risk of agents amplifying each other mistakes.

## Best Practices
Start with two or three roles, make contracts explicit, centralize risk decisions, log all messages, and measure whether extra agents improve outcomes.

## Prompt Patterns
Give each agent a role, authority boundary, input contract, output contract, escalation rule, and communication protocol.

## Development Workflow
Decompose the task, define patterns, wire communication, add shared state, test failure paths, add human checkpoints, and deploy gradually

## Testing Workflow
Run scenario evals for each role, test handoffs, replay failed conversations, check state consistency, and red-team collusion or tool misuse.

## Deployment
Deploy with observability, queues, timeouts, budget caps, role-level permissions, and a kill switch for runaway coordination.

## Common Mistakes
Too many agents, no supervisor, vague handoffs, shared mutable memory, missing reviewer role, and unbounded retries.

## Performance Tips
Parallelize independent work, collapse unnecessary agents, summarize messages, cache shared context, and route only when value exceeds cost.

## Security
Scope tools per role, isolate memory, validate inter-agent messages, require approval for high-impact actions, and audit all communication.

## Real-world Examples
Planner-executor-reviewer software task; supervisor-routed support triage; research team with source verifier; incident response team with human approval.

## Comparison with alternatives
Use a single-agent runtime for simpler tasks; use LangGraph for explicit state orchestration; use CrewAI for role/task crew ergonomics; use AutoGen for evented multi-agent runtimes.

## Related Skills
- [AI skill](../../skills/ai/README.md)
- [Agents skill](../../skills/ai/agents/README.md)
- [Architecture skill](../../skills/architecture/README.md)
- [Security skill](../../skills/security/README.md)

## Related Frameworks
- [ReAct](../../frameworks/react/README.md)
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [Tree of Thought](../../frameworks/tree-of-thought/README.md)
- [Reflection](../../frameworks/reflection/README.md)

## Related Templates
- [CLI Application](../../templates/cli-application/README.md)
- [Microservice](../../templates/microservice/README.md)
- [GitHub Action](../../templates/github-action/README.md)

## Supervisor Pattern
A supervisor owns routing, risk decisions, stop conditions, and final synthesis. Use it when multiple agents can work independently but need one accountable coordinator.

## Planner Pattern
A planner decomposes the task into ordered work packages. The planner should not execute risky tools; it should produce tasks, dependencies, acceptance criteria, and routing hints.

## Executor Pattern
Executors perform bounded tasks with specific tools. They should return evidence, artifacts, and status rather than broad opinions.

## Reviewer Pattern
Reviewers critique outputs for correctness, safety, tests, and policy compliance. Reviewers should have different instructions from executors to avoid rubber-stamping.

## Memory Pattern
Memory stores durable facts, preferences, and work history. Separate short-term task state from long-term memory, and define retention and deletion rules.

## Routing Pattern
Routers classify input and send it to the right specialist. Use deterministic routing where possible and model-based routing only when categories are ambiguous.

## Human-in-the-loop
Humans approve risky actions, resolve ambiguity, inspect state, and handle policy exceptions. Human checkpoints should be explicit, not improvised at failure time.

## Tool Calling
Tools must be scoped per role, schema-validated, observable, and reversible where possible. Treat every tool call as a privileged operation.

## Agent Communication
Use structured messages with sender, recipient, task id, assumptions, evidence, requested action, and completion status. Avoid free-form chat for critical handoffs.

## State Management
Version state schemas, define ownership, checkpoint long tasks, and avoid shared mutable memory unless the consistency model is clear.

## Failure Recovery
Define retry limits, fallback agents, human escalation, state rollback, and incident logging. Recovery behavior should be tested before deployment.

