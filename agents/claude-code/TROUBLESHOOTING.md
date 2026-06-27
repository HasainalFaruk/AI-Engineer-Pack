# Claude Code Troubleshooting

## Agent does not stop
Check turn limits, termination rules, approval gates, and whether the task is too open-ended.

## Tool use is incorrect
Review schemas, permission checks, tool descriptions, environment variables, and examples.

## Output quality is poor
Tighten the output contract, reduce irrelevant context, add examples, and evaluate against known good runs.

## Runs are slow or expensive
Provide focused context, split large tasks, use background agents for independent work, and summarize long sessions before continuing.

## Security review fails
Protect secrets, restrict shell/network actions, use MCP servers deliberately, review generated commands, and avoid pasting sensitive customer data. Review secrets, logs, traces, permissions, memory, and external tool access.
