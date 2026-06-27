# MCP Servers

## Purpose
Build MCP servers that expose reliable tools, resources, prompts, and optional sampling workflows to AI clients through a stable protocol interface.

## Contents
- README.md
- ARCHITECTURE.md
- WORKFLOW.md
- CHECKLIST.md
- PROMPTS.md
- EXAMPLES.md

## When to use
Use this module when wrapping a database, API, filesystem, developer tool, enterprise service, or workflow engine for AI-assisted use.

## When not to use
Do not use a server when static documentation or a one-off script is enough; MCP is best when discovery, repeatability, and controlled execution matter.

## MCP topics covered
- capability boundaries
- tool schemas
- resource URIs
- prompt discovery
- server-side authorization
- JSON-RPC request and response flow
- Debugging, testing, deployment, and performance review
- OpenAI integration and Claude integration

## Practical workflow
1. Define the user workflow, host boundary, and success criteria.
2. Identify the MCP responsibilities: capability boundaries, tool schemas, resource URIs, prompt discovery, server-side authorization.
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
