# LangGraph Troubleshooting

## Agent loops or never stops
Check termination criteria, max turns, tool error handling, and whether the prompt asks for open-ended exploration. Add explicit stop conditions.

## Tool calls are wrong
Review tool schemas, descriptions, permission checks, and examples. Add validation and reject ambiguous arguments.

## Output is low quality
Tighten the output contract, add examples, reduce irrelevant context, and evaluate against known successful runs.

## Runs are slow or expensive
Minimize state size, stream outputs, split slow nodes, avoid repeated retrieval, and checkpoint only useful state.

## Security review fails
Sanitize state, protect checkpoint stores, restrict tools per node, review human-interrupt surfaces, and redact trace payloads. Confirm secrets, logs, memory, traces, and tool scopes are safe.

## Production behavior differs from local tests
Compare model settings, environment variables, tool credentials, network permissions, state storage, and dependency versions.
