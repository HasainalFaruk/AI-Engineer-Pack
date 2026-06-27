# GitHub Copilot

## Purpose
GitHub Copilot helps teams augment software engineering inside GitHub and developer environments with completions, chat, code review, cloud agents, CLI workflows, MCP, custom instructions, and enterprise controls.


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
Copilot spans IDE suggestions, chat, GitHub web features, code review, cloud agents, custom agents, hooks, MCP servers, repository instructions, spaces, policies, metrics, and enterprise governance.

## Installation
Enable Copilot for the user, organization, or enterprise; install IDE extensions or use GitHub web, CLI, and cloud agent surfaces.

## When to use
Use for GitHub-centric coding, PR summaries, code review, issue work, repository-aware chat, enterprise governance, and cloud-agent task execution.

## When NOT to use
Avoid for workflows outside GitHub governance, tasks needing custom low-level runtime control, or privileged production changes without review.

## Capabilities
Code suggestions, chat, PR summaries, code review, cloud agents, custom agents, agent skills, MCP, Copilot CLI, policies, metrics, and enterprise administration.

## Limitations
Feature availability varies by plan and policy, context depends on indexing and permissions, and agent work must be reviewed like any contributor output.

## Best Practices
Maintain repository instructions, configure content exclusions, enforce branch protections, use automatic review carefully, and monitor usage metrics.

## Prompt Patterns
Reference issue or PR context, desired files, coding standards, tests, and review expectations; ask for a PR-ready change with verification evidence.

## Development Workflow
Configure access, add repo instructions, select Copilot surface, ask for scoped work, review generated changes, run CI, and merge through normal branch protections

## Testing Workflow
Use CI, required checks, Copilot custom-agent tests, review comments, and security scanning before accepting agent changes.

## Deployment
Deploy through GitHub Actions or existing pipelines with branch protections, environment approvals, secrets policies, and audit trails.

## Common Mistakes
Relying on suggestions without review, weak repository instructions, ignoring content exclusions, over-permissive custom agents, and bypassing CI.

## Performance Tips
Keep issues scoped, provide repository-specific instructions, use indexed context, and split large tasks across smaller PRs.

## Security
Enforce organization policies, restrict agent environments, manage MCP and secrets carefully, and review generated code for supply-chain risk.

## Real-world Examples
Generate PR summary; triage issues; run cloud agent for a bug fix; configure custom repository agent; review a security-sensitive PR.

## Comparison with alternatives
Use Claude Code or Gemini CLI for terminal-first local coding, OpenAI Agents SDK for custom applications, and LangGraph for stateful orchestration.

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

