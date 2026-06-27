# MCP Servers Examples

## Purpose
These examples show how mcp servers applies to real MCP engineering work.

## Practical example
A support MCP server exposes article resources, a read-only search tool, and an escalation-draft prompt. It authenticates with an internal service token, filters tenant data by user identity, and logs every article lookup without storing customer messages.

## OpenAI-oriented example
An OpenAI agent workflow connects to an MCP server only after the server is registered, authenticated, and scoped to the current task. The host logs discovered capabilities, constrains tool use through policy, and stores provenance for any result that influences the final answer.

## Claude-oriented example
A Claude Code workflow uses an explicit MCP server configuration for a workspace. Read-only resources are available during analysis, write tools require confirmation, and server output is treated as context that can inform work but cannot override developer instructions.

## JSON-RPC sketch
```json
{
  "jsonrpc": "2.0",
  "id": "example-1",
  "method": "tools/call",
  "params": {
    "name": "example_capability",
    "arguments": {
      "scope": "current-workspace"
    }
  }
}
```

## Comparison with alternatives
- Direct API integration can be simpler for one application, but MCP provides reusable discovery and capability boundaries across hosts.
- RAG-only retrieval is useful for context, but MCP resources and tools can combine retrieval with controlled actions.
- A conventional backend API may still be the right choice for product traffic; MCP is most useful at the AI assistant boundary.

## Related frameworks and skills
- [Agents](../../agents/README.md)
- [AI skills](../../skills/ai/README.md)
- [Security skills](../../skills/security/README.md)
- [Architecture skills](../../skills/architecture/README.md)
- [ReAct framework](../../frameworks/react/README.md)
- [Plan and Solve framework](../../frameworks/plan-and-solve/README.md)
- [Microservice template](../../templates/microservice/README.md)
