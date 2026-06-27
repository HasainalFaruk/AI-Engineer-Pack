# GitHub Copilot Troubleshooting

## Agent does not stop
Check turn limits, termination rules, approval gates, and whether the task is too open-ended.

## Tool use is incorrect
Review schemas, permission checks, tool descriptions, environment variables, and examples.

## Output quality is poor
Tighten the output contract, reduce irrelevant context, add examples, and evaluate against known good runs.

## Runs are slow or expensive
Keep issues scoped, provide repository-specific instructions, use indexed context, and split large tasks across smaller PRs.

## Security review fails
Enforce organization policies, restrict agent environments, manage MCP and secrets carefully, and review generated code for supply-chain risk. Review secrets, logs, traces, permissions, memory, and external tool access.
