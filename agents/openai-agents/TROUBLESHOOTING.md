# OpenAI Agents SDK Troubleshooting

## Agent loops or never stops
Check termination criteria, max turns, tool error handling, and whether the prompt asks for open-ended exploration. Add explicit stop conditions.

## Tool calls are wrong
Review tool schemas, descriptions, permission checks, and examples. Add validation and reject ambiguous arguments.

## Output is low quality
Tighten the output contract, add examples, reduce irrelevant context, and evaluate against known successful runs.

## Runs are slow or expensive
Trim context, cache stable instructions, stream long outputs, parallelize safe independent tools, and set explicit max turns.

## Security review fails
Apply least privilege to tools, isolate sandbox workspaces, redact secrets in traces, validate MCP servers, and require human approval for writes or external actions. Confirm secrets, logs, memory, traces, and tool scopes are safe.

## Production behavior differs from local tests
Compare model settings, environment variables, tool credentials, network permissions, state storage, and dependency versions.
