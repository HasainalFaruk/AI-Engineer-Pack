# OpenAI Agents SDK

## Purpose
OpenAI Agents SDK helps teams build Python-first agentic applications with OpenAI models, tools, guardrails, handoffs, sessions, tracing, and optional sandboxed workspaces.


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
Agent definitions combine instructions, models, tools, guardrails, context, and optional handoffs; Runner manages the loop, tool execution, results, tracing, sessions, and human-in-the-loop checkpoints.

## Installation
pip install openai-agents

## When to use
Use when you want a production-ready OpenAI-native runtime for tool-using agents, delegated specialist agents, guarded workflows, voice or realtime agents, or file/workspace-oriented sandbox agents.

## When NOT to use
Avoid when a single Responses API call is enough, when you need a model-neutral graph runtime, or when your team must own every loop and tool-dispatch detail manually.

## Capabilities
Function tools, MCP tools, handoffs, agents-as-tools, guardrails, sessions, tracing, streaming, realtime and voice agents, sandbox agents, and human review steps.

## Limitations
OpenAI-centric defaults, Python runtime expectations, guardrails still require domain-specific policy design, and tool permissions must be explicitly controlled.

## Best Practices
Keep tools narrow, validate tool inputs with schemas, trace every production run, add guardrails near user input and final output, and prefer explicit handoff contracts between agents.

## Prompt Patterns
Define the agent role, tool permissions, stop conditions, escalation path, and output contract; keep instructions stable and move volatile task data into user input or context.

## Development Workflow
Model the task, define tools and schemas, add guardrails, run locally with traces, add regression evals, configure session storage, then deploy behind clear rate limits and monitoring

## Testing Workflow
Unit-test tools, run trace-backed scenario evals, test guardrail failures, simulate tool errors, and verify handoff paths with deterministic fixtures.

## Deployment
Ship behind an API or worker with secret management, tracing export, rate limits, retry policies, and approval gates for high-impact tools.

## Common Mistakes
Overbroad shell or filesystem tools, no output validation, unbounded loops, hidden state dependencies, and missing trace review.

## Performance Tips
Trim context, cache stable instructions, stream long outputs, parallelize safe independent tools, and set explicit max turns.

## Security
Apply least privilege to tools, isolate sandbox workspaces, redact secrets in traces, validate MCP servers, and require human approval for writes or external actions.

## Real-world Examples
Customer-support triage agent with guarded CRM tools; code-review agent with sandboxed repository access; research agent that hands off citation checking to a verifier.

## Comparison with alternatives
Use LangGraph for lower-level state graphs, CrewAI for crew/task ergonomics, AutoGen for Microsoft-style evented multi-agent systems, and CLI agents for developer workstation automation.

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

