# CrewAI

## Purpose
CrewAI helps teams coordinate role-based agents, crews, tasks, processes, flows, memory, knowledge, tools, and enterprise automations.


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
Agents have roles, goals, backstories, tools, and memory; tasks describe work and outputs; crews coordinate agents; flows provide more controlled event-driven orchestration.

## Installation
uv tool install crewai or pip install crewai

## When to use
Use when the mental model is a team of specialists completing business tasks, content operations, research, sales workflows, or repeatable automations.

## When NOT to use
Avoid when you need low-level graph state control, custom distributed runtimes, or a single deterministic workflow without role-based delegation.

## Capabilities
Agents, crews, flows, tasks, processes, tools, knowledge sources, memory, guardrails, callbacks, human-in-the-loop, and enterprise deployment features.

## Limitations
Role prompts can drift, task delegation can overrun budgets, and production control requires careful process design and observability.

## Best Practices
Write measurable task outputs, keep agent roles non-overlapping, prefer flows for controlled automation, and use guardrails for final artifacts.

## Prompt Patterns
Give each agent a narrow role, concrete goal, tool boundary, expected output, and collaboration rule with the rest of the crew.

## Development Workflow
Define business outcome, design agents and tasks, choose crew or flow, wire tools and knowledge, run locally, add guardrails, then deploy automations with monitoring

## Testing Workflow
Test task outputs, mock tools, validate flow state, run golden examples, and review token/cost budgets per crew.

## Deployment
Deploy as scheduled or triggered automations with environment separation, secrets, observability, RBAC, and rollback plans.

## Common Mistakes
Too many agents, vague roles, no task acceptance criteria, tool access shared too broadly, and no cost controls.

## Performance Tips
Reduce crew size, cache knowledge, constrain delegation, parallelize independent tasks, and cap iterations.

## Security
Scope tools by role, protect trigger payloads, audit automation runs, avoid sensitive data in memory, and enforce human approval for external writes.

## Real-world Examples
Market research crew; sales email automation; compliance document review flow; support triage with human escalation.

## Comparison with alternatives
Use LangGraph for explicit state graphs, OpenAI Agents SDK for OpenAI-native guardrails and tracing, and AutoGen for event-driven Microsoft agent stacks.

## Related Skills
- [AI skill](../../skills/ai/README.md)
- [Agents skill](../../skills/ai/agents/README.md)
- [RAG skill](../../skills/ai/rag/README.md)
- [Architecture skill](../../skills/architecture/README.md)
- [Security skill](../../skills/security/README.md)

## Related Frameworks
- [ReAct](../../frameworks/react/README.md)
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [Tree of Thought](../../frameworks/tree-of-thought/README.md)
- [Reflection](../../frameworks/reflection/README.md)

## Related Templates
- [RAG Project](../../templates/rag-project/README.md)
- [CLI Application](../../templates/cli-application/README.md)
- [Microservice](../../templates/microservice/README.md)
- [GitHub Action](../../templates/github-action/README.md)

