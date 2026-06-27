# LangGraph

## Purpose
LangGraph helps teams build long-running, stateful, graph-orchestrated agents with durable execution, explicit state transitions, streaming, persistence, memory, and human-in-the-loop control.


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
A graph defines state, nodes, edges, conditional routing, checkpoints, persistence, and runtime behavior; nodes can call models, tools, retrievers, services, or subgraphs.

## Installation
pip install -U langgraph

## When to use
Use for complex workflows that need explicit state, resumability, branching, retries, human inspection, or production-grade orchestration beyond a simple agent loop.

## When NOT to use
Avoid for small chatbots, one-shot tool calls, or teams that want high-level agent abstractions without designing graph state and transitions.

## Capabilities
State graphs, conditional edges, persistence, interrupts, streaming, memory, subgraphs, durable execution, LangSmith tracing, and deployable agent runtimes.

## Limitations
More design responsibility, more state modeling, less hand-holding for prompt architecture, and potential complexity for small projects.

## Best Practices
Define state schemas first, keep nodes pure where possible, make routing explicit, checkpoint long work, and trace every graph path.

## Prompt Patterns
Prompt each node for one responsibility and make routing decisions inspectable; avoid one giant system prompt that hides the graph design.

## Development Workflow
Design state, draw graph paths, implement nodes, add conditional routing, configure persistence, test branches, add tracing, and deploy with state migration discipline

## Testing Workflow
Unit-test nodes, integration-test graph paths, test checkpoint resume, test interrupts, and replay traces for regressions.

## Deployment
Deploy with persistent storage, versioned state schemas, observability, backpressure, and safe migration plans for active runs.

## Common Mistakes
Unclear state ownership, giant nodes, hidden side effects, missing checkpointers, and no tests for alternate branches.

## Performance Tips
Minimize state size, stream outputs, split slow nodes, avoid repeated retrieval, and checkpoint only useful state.

## Security
Sanitize state, protect checkpoint stores, restrict tools per node, review human-interrupt surfaces, and redact trace payloads.

## Real-world Examples
Loan review workflow with human approval; research pipeline with planner, retriever, writer, and verifier; incident response graph with rollback branch.

## Comparison with alternatives
Use OpenAI Agents SDK for OpenAI-native loops, CrewAI for role/task crew composition, AutoGen Core for distributed evented agents, and multi-agent patterns for framework-neutral architecture.

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

