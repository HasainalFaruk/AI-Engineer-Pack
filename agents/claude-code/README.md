# Claude Code

## Purpose
Claude Code helps teams use Anthropic agentic coding surfaces across terminal, IDE, desktop, web, CI, and automation to read code, edit files, run commands, and coordinate development tasks.


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
Claude Code sessions combine repository context, persistent instructions, permissions, tool access, memories, MCP connectors, hooks, skills, and surfaces such as CLI, IDE, desktop, browser, and CI.

## Installation
curl -fsSL https://claude.ai/install.sh | bash, winget install Anthropic.ClaudeCode, or brew install --cask claude-code

## When to use
Use for codebase exploration, feature work, bug fixes, tests, refactors, PRs, recurring coding tasks, and multi-agent coding sessions with human review.

## When NOT to use
Avoid for changes that cannot be reviewed, regulated workflows without approved data handling, or tasks requiring unsupported local permissions.

## Capabilities
File edits, shell commands, diff review, git operations, MCP, repository instructions, memories, hooks, skills, background agents, scheduling, and CI integrations.

## Limitations
Requires careful permission configuration, may need paid subscription depending on surface, and outputs still require review and test verification.

## Best Practices
Write strong repository instructions, keep permission modes conservative, require tests, review diffs, and use hooks for formatting and validation.

## Prompt Patterns
State repository goal, files in scope, constraints, verification commands, commit policy, and whether the agent may edit or only propose.

## Development Workflow
Start in a clean worktree, ask for a plan, let Claude inspect, approve scoped edits, run tests, review diffs, then commit or open PR after human approval

## Testing Workflow
Run project test suites, lint, type checks, and task-specific smoke tests; verify that hooks and CI reproduce local results.

## Deployment
Use CI/CD integrations for review and automation, never deploy directly without human approval, and use scheduled tasks only with scoped permissions.

## Common Mistakes
Vague prompts, unrestricted tool permissions, skipping diff review, letting sessions drift, and missing repository instructions.

## Performance Tips
Provide focused context, split large tasks, use background agents for independent work, and summarize long sessions before continuing.

## Security
Protect secrets, restrict shell/network actions, use MCP servers deliberately, review generated commands, and avoid pasting sensitive customer data.

## Real-world Examples
Write tests for an auth module; fix failing CI; generate release notes; run parallel agents for docs and tests; automate weekly dependency audit.

## Comparison with alternatives
Use GitHub Copilot for GitHub-native workflows, Gemini CLI for terminal Gemini access, OpenAI Agents SDK for custom Python agents, and LangGraph for stateful custom orchestration.

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

