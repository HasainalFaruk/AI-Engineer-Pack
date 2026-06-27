# OpenAI Agents SDK Examples

## Example 1: Safe code review agent
Goal: inspect a pull request, summarize risk, and suggest fixes without writing to the repository.

Expected behavior:
- Reads only changed files and relevant tests.
- Reports severity-ranked findings.
- Refuses to merge, deploy, or modify secrets.

## Example 2: Tool-using support agent
Goal: triage customer issues using a ticket search tool and a read-only account lookup tool.

Expected behavior:
- Retrieves only the minimum data needed.
- Explains uncertainty.
- Escalates billing, security, or account deletion requests to a human.

## Example 3: Production workflow
Customer-support triage agent with guarded CRM tools; code-review agent with sandboxed repository access; research agent that hands off citation checking to a verifier.

## Example output contract
- Summary: what the agent did.
- Evidence: files, tools, traces, or records consulted.
- Decision: final recommendation or artifact.
- Risks: unresolved uncertainty and escalation needs.
- Verification: tests, evals, or human checks completed.
