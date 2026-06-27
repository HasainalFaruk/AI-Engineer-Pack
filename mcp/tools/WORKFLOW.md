# MCP Tools Workflow

## Purpose
Use this workflow to design, implement, test, and release mcp tools with production discipline.

## Inputs
- User workflow and success criteria.
- Host, client, server, and external-system boundaries.
- Required tools, resources, prompts, sampling behavior, and transport.
- Authentication, authorization, approval, logging, and deployment constraints.

## Outputs
- Reviewed MCP design notes.
- Implemented and tested capability set.
- Security and operations checklist results.
- Usage examples for OpenAI, Claude, and generic MCP clients where applicable.

## Step-by-step workflow
1. Define the user workflow, host boundary, and success criteria.
2. Identify the MCP responsibilities: input schemas, side effects, approval policy, structured results, audit records.
3. Separate resources for context from tools for actions and prompts for reusable workflows.
4. Choose stdio for local trusted integrations or Streamable HTTP for remote shared services.
5. Specify authentication, authorization, consent, logging, and error behavior before implementation.
6. Build contract tests for initialization, discovery, JSON-RPC calls, errors, cancellation, and timeout paths.
7. Document OpenAI, Claude, debugging, deployment, and operational assumptions before release.

## Debugging workflow
1. Reproduce with a minimal JSON-RPC request and capture the request identifier.
2. Confirm initialization and capability discovery succeeded before debugging domain behavior.
3. Compare client-side validation errors with server-side authorization and execution logs.
4. Inspect sanitized payload size, schema validation, timeout, cancellation, and retry behavior.
5. Record the fix as a test fixture so the failure does not return.

## Testing workflow
- Unit test schema validation and permission decisions.
- Contract test JSON-RPC request, response, notification, and error fixtures.
- Integration test the real transport and external-system boundary.
- Security test prompt-injection content, over-broad permissions, replay, and tenant isolation.
- Performance test latency, payload size, concurrency, and timeout behavior.

## Deployment workflow
- Version the capability contract and document migration behavior.
- Configure secrets, identity, and network policy outside source-controlled documentation.
- Enable health checks, structured logs, metrics, alerts, and rollback steps.
- Run the repository validation toolkit before publishing module changes.
