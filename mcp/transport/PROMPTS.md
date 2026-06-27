# MCP Transport Prompts

## Purpose
These prompts help architects and AI assistants design, review, and improve mcp transport.

## Design prompt
Design mcp transport for a production AI engineering workflow. Cover JSON-RPC 2.0, stdio, Streamable HTTP, sessions, cancellation, JSON-RPC flow, authentication, authorization, testing, debugging, deployment, OpenAI integration, and Claude integration.

## ChatGPT example
You are designing an MCP integration for a product team. Explain the capability boundaries, JSON-RPC flow, security controls, testing strategy, and user approval experience for mcp transport. Prefer concrete schemas, URI patterns, and operational checks over broad advice.

## Codex example
Review the repository MCP module for mcp transport. Preserve existing filenames and folder structure. Improve inaccurate protocol descriptions, broken cross-links, missing testing notes, and unclear security guidance. Run the validation scripts after editing.

## Security review prompt
Act as an MCP security reviewer. Identify authorization gaps, prompt-injection risks, excessive tool power, weak transport assumptions, logging leaks, and unsafe retry or approval behavior for this design.

## Debugging prompt
Given an MCP failure report with request id, method, transport, server version, and sanitized payload, isolate whether the issue is initialization, capability discovery, schema validation, authorization, execution, transport, or client rendering.

## Documentation prompt
Rewrite this mcp transport document so it clearly separates MCP fundamentals, practical workflow, OpenAI integration, Claude integration, limitations, and related repository modules without repeating boilerplate.
