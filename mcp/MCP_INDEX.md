# MCP Index

## Purpose
This index maps the Model Context Protocol module so readers can move from protocol fundamentals to implementation, security, examples, and production readiness.

| Module | Purpose |
|---|---|
| [Clients](clients/README.md) | Build MCP clients inside AI hosts, IDEs, agent runtimes, desktop apps, and service backends that need controlled access to external context and actions. |
| [Servers](servers/README.md) | Build MCP servers that expose reliable tools, resources, prompts, and optional sampling workflows to AI clients through a stable protocol interface. |
| [Resources](resources/README.md) | Model contextual data that AI clients can read through stable URI-based interfaces without treating every lookup as an executable action. |
| [Tools](tools/README.md) | Design executable MCP actions that models can request safely, with explicit schemas, permissions, observability, and result contracts. |
| [Transport](transport/README.md) | Implement the message layer that carries JSON-RPC 2.0 requests, responses, notifications, cancellation, and session state between MCP clients and servers. |
| [Security](security/README.md) | Protect MCP systems from unauthorized access, excessive tool power, prompt injection, data leakage, confused-deputy failures, and unsafe automation. |
| [Examples](examples/README.md) | Show practical MCP architectures that combine clients, servers, tools, resources, prompts, transport, security, OpenAI integration, and Claude integration. |
| [Templates](templates/README.md) | Provide reusable document structures for MCP server specs, client specs, tool definitions, resource catalogs, security reviews, test plans, and deployment runbooks. |
| [Best Practices](best-practices/README.md) | Collect production engineering guidance for designing, testing, deploying, observing, and governing MCP systems across clients and servers. |

## Suggested reading paths
- New to MCP: [README](README.md), [Transport](transport/README.md), [Resources](resources/README.md), and [Tools](tools/README.md).
- Building a server: [Servers](servers/README.md), [Tools](tools/README.md), [Resources](resources/README.md), [Security](security/README.md), and [Templates](templates/README.md).
- Building a host or client: [Clients](clients/README.md), [Transport](transport/README.md), [Security](security/README.md), and [Best Practices](best-practices/README.md).
- Preparing production release: [Security](security/README.md), [Best Practices](best-practices/README.md), [Examples](examples/README.md), and [Templates](templates/README.md).

## Related repository indexes
- [Agent Index](../docs/AGENT_INDEX.md)
- [Skill Index](../docs/SKILL_INDEX.md)
- [Framework Index](../docs/FRAMEWORK_INDEX.md)
- [Template Index](../docs/TEMPLATE_INDEX.md)
- [Checklist Index](../docs/CHECKLIST_INDEX.md)
