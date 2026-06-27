# CrewAI Troubleshooting

## Agent loops or never stops
Check termination criteria, max turns, tool error handling, and whether the prompt asks for open-ended exploration. Add explicit stop conditions.

## Tool calls are wrong
Review tool schemas, descriptions, permission checks, and examples. Add validation and reject ambiguous arguments.

## Output is low quality
Tighten the output contract, add examples, reduce irrelevant context, and evaluate against known successful runs.

## Runs are slow or expensive
Reduce crew size, cache knowledge, constrain delegation, parallelize independent tasks, and cap iterations.

## Security review fails
Scope tools by role, protect trigger payloads, audit automation runs, avoid sensitive data in memory, and enforce human approval for external writes. Confirm secrets, logs, memory, traces, and tool scopes are safe.

## Production behavior differs from local tests
Compare model settings, environment variables, tool credentials, network permissions, state storage, and dependency versions.
