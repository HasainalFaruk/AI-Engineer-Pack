# Gemini CLI Troubleshooting

## Agent does not stop
Check turn limits, termination rules, approval gates, and whether the task is too open-ended.

## Tool use is incorrect
Review schemas, permission checks, tool descriptions, credentials, environment variables, and examples.

## Output quality is poor
Tighten the output contract, reduce irrelevant context, add examples, and evaluate against known good runs.

## Runs are slow or expensive
Use large context selectively, summarize long sessions, checkpoint milestones, scope file operations, and avoid unnecessary web fetches.

## Security review fails
Protect OAuth or API credentials, restrict shell and file access, vet MCP servers, redact sensitive prompts, and avoid command execution from untrusted content. Review secrets, logs, traces, permissions, memory, and external tool access.
