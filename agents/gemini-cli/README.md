# Gemini CLI

## Purpose
Gemini CLI helps teams bring Gemini-powered agentic coding and research workflows directly into the terminal with file operations, shell commands, web fetching, Google Search grounding, checkpointing, and MCP extensions.


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
A terminal agent session combines Gemini models, project context files such as GEMINI.md, built-in tools, MCP servers, authentication, checkpointing, and optional GitHub Action integration.

## Installation
npx @google/gemini-cli, npm install -g @google/gemini-cli, or brew install gemini-cli.

## When to use
Use for terminal-first codebase work, scripts, research grounded with Google Search, large-context analysis, automation, and GitHub workflow assistance.

## When NOT to use
Avoid for teams that cannot install Node tooling, tasks needing a different model provider, or privileged shell work without review.

## Capabilities
File operations, shell commands, web fetching, Google Search grounding, MCP support, non-interactive scripts, checkpointing, GitHub Action integration, and large-context model access.

## Limitations
Requires Node-based CLI installation, quotas and model availability depend on auth mode, and terminal tool access must be constrained carefully.

## Best Practices
Use GEMINI.md for project guidance, checkpoint long sessions, keep shell commands reviewable, configure MCP deliberately, and run validation before accepting changes.

## Prompt Patterns
Give a concrete terminal task, scope, files, command policy, desired verification, and whether the agent can edit files or only inspect.

## Development Workflow
Install CLI, authenticate, add GEMINI.md, run scoped prompts, inspect diffs, run tests, checkpoint progress, and use GitHub Action for repeatable automation

## Testing Workflow
Run project tests, validate shell output, compare checkpoints, test MCP integrations, and review GitHub Action behavior on pull requests.

## Deployment
Use through CI or terminal workflows with explicit secrets, restricted permissions, and human approval for merges or production changes.

## Common Mistakes
Running broad shell commands, skipping diff review, relying on live search without citations, ignoring quotas, and using untrusted MCP servers.

## Performance Tips
Use large context selectively, summarize long sessions, checkpoint milestones, scope file operations, and avoid unnecessary web fetches.

## Security
Protect OAuth or API credentials, restrict shell and file access, vet MCP servers, redact sensitive prompts, and avoid command execution from untrusted content.

## Real-world Examples
Analyze a large codebase; debug failing tests; ground a research answer with Search; automate PR review with Gemini CLI GitHub Action.

## Comparison with alternatives
Use Claude Code for Anthropic coding surfaces, GitHub Copilot for GitHub-native governance, and OpenAI Agents SDK for custom app agents.

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

