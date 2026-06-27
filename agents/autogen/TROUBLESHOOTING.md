# Microsoft AutoGen Troubleshooting

## Agent does not stop
Check turn limits, termination rules, approval gates, and whether the task is too open-ended.

## Tool use is incorrect
Review schemas, permission checks, tool descriptions, environment variables, and examples.

## Output quality is poor
Tighten the output contract, reduce irrelevant context, add examples, and evaluate against known good runs.

## Runs are slow or expensive
Limit agent turns, summarize long conversations, reduce team size, stream outputs, and avoid unnecessary manager-agent chatter.

## Security review fails
Sandbox code execution, authenticate local control planes, restrict file/network access, and never let browser-derived content issue privileged commands. Review secrets, logs, traces, permissions, memory, and external tool access.
