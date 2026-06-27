# Microsoft AutoGen

## Purpose
Microsoft AutoGen helps teams build conversational single-agent and multi-agent applications with AgentChat, event-driven Core runtimes, extensions, and optional AutoGen Studio prototyping.


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
AgentChat provides conversational agents and teams; Core provides event-driven multi-agent runtime primitives; Extensions connect tools, models, MCP workbenches, code executors, and distributed runtimes.

## Installation
pip install -U autogen-agentchat autogen-ext[openai]

## When to use
Use for research prototypes, conversational multi-agent teams, Microsoft ecosystem projects, distributed agent experiments, or Studio-assisted workflow design.

## When NOT to use
Avoid when you need a tiny OpenAI-native loop, a simple deterministic script, or a framework with less architectural surface area.

## Capabilities
AssistantAgent, teams, tool use, MCP workbenches, Docker code execution, Studio UI, distributed runtimes, extensions, and .NET support.

## Limitations
API generations changed significantly, production designs need careful version control, and conversation teams can become hard to debug without tracing discipline.

## Best Practices
Pin package versions, isolate code execution, define agent termination rules, use typed messages, and keep team topology small.

## Prompt Patterns
Specify each agent persona, allowed tools, collaboration protocol, turn budget, termination signal, and review responsibilities.

## Development Workflow
Prototype in AgentChat or Studio, extract stable agent definitions, add tools and executors, test team conversations, then harden runtime and deployment

## Testing Workflow
Test tools, simulate team transcripts, assert termination, test Docker executor isolation, and replay failed conversations.

## Deployment
Deploy with pinned versions, isolated execution containers, model configuration management, logs, metrics, and human fallback for non-terminating runs.

## Common Mistakes
Using outdated patterns, missing termination criteria, unsafe code executors, and broad tool access.

## Performance Tips
Limit agent turns, summarize long conversations, reduce team size, stream outputs, and avoid unnecessary manager-agent chatter.

## Security
Sandbox code execution, authenticate local control planes, restrict file/network access, and never let browser-derived content issue privileged commands.

## Real-world Examples
Two-agent code review; distributed research team; AutoGen Studio prototype for support workflow; Docker-backed code execution evaluator.

## Comparison with alternatives
Use CrewAI for business crews, LangGraph for state graphs, OpenAI Agents SDK for OpenAI-native guardrails, and multi-agent patterns for framework-neutral design.

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

