# Multi-Agent Systems Troubleshooting

## Agent does not stop
Check turn limits, termination rules, approval gates, and whether the task is too open-ended.

## Tool use is incorrect
Review schemas, permission checks, tool descriptions, credentials, environment variables, and examples.

## Output quality is poor
Tighten the output contract, reduce irrelevant context, add examples, and evaluate against known good runs.

## Runs are slow or expensive
Parallelize independent work, collapse unnecessary agents, summarize messages, cache shared context, and route only when value exceeds cost.

## Security review fails
Scope tools per role, isolate memory, validate inter-agent messages, require approval for high-impact actions, and audit all communication. Review secrets, logs, traces, permissions, memory, and external tool access.
