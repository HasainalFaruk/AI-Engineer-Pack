# MCP Resources

## Purpose
Model contextual data that AI clients can read through stable URI-based interfaces without treating every lookup as an executable action.

## Contents
- README.md
- ARCHITECTURE.md
- WORKFLOW.md
- CHECKLIST.md
- PROMPTS.md
- EXAMPLES.md

## When to use
Use resources for files, records, documentation pages, schemas, logs, metrics, knowledge-base entries, repository metadata, and other attributable context.

## When not to use
Do not use resources for operations that mutate state, trigger external side effects, or require complex user confirmation; represent those as tools.

## MCP topics covered
- URI design
- metadata
- freshness
- subscriptions
- read-time authorization
- JSON-RPC request and response flow
- Debugging, testing, deployment, and performance review
- OpenAI integration and Claude integration

## Practical workflow
1. Define the user workflow, host boundary, and success criteria.
2. Identify the MCP responsibilities: URI design, metadata, freshness, subscriptions, read-time authorization.
3. Separate resources for context from tools for actions and prompts for reusable workflows.
4. Choose stdio for local trusted integrations or Streamable HTTP for remote shared services.
5. Specify authentication, authorization, consent, logging, and error behavior before implementation.
6. Build contract tests for initialization, discovery, JSON-RPC calls, errors, cancellation, and timeout paths.
7. Document OpenAI, Claude, debugging, deployment, and operational assumptions before release.

## OpenAI integration
In OpenAI agent or tool workflows, expose only the capabilities required for the task, validate server identity, review tool and resource descriptions, require approval for side effects, and preserve provenance for every MCP result used in a final answer.

## Claude integration
In Claude and Claude Code workflows, keep server configuration explicit, apply least privilege to local and remote servers, document reachable workspace or account data, and require confirmation before writes, deployments, or external notifications.

## Related MCP modules
- [Clients](../clients/README.md)
- [Servers](../servers/README.md)
- [Resources](../resources/README.md)
- [Tools](../tools/README.md)
- [Transport](../transport/README.md)
- [Security](../security/README.md)
- [Examples](../examples/README.md)
- [Templates](../templates/README.md)
- [Best Practices](../best-practices/README.md)

## Related repository modules
- [Agents](../../agents/README.md)
- [AI skills](../../skills/ai/README.md)
- [Security skills](../../skills/security/README.md)
- [Architecture skills](../../skills/architecture/README.md)
- [ReAct framework](../../frameworks/react/README.md)
- [Plan and Solve framework](../../frameworks/plan-and-solve/README.md)
- [Microservice template](../../templates/microservice/README.md)
