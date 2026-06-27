# Claude Code Prompt Patterns

## Build prompt
Use Claude Code to complete a scoped engineering task. Inspect context first, list assumptions, request approval before risky actions, and return changed files plus verification.

## Review prompt
Review this Claude Code workflow for permissions, state handling, prompt injection risk, observability, and deployment readiness. Return severity-ranked findings.

## Debug prompt
Debug this failed Claude Code run. Inspect prompts, tool logs, state, traces, and final output. Identify the first bad decision and propose a regression check.

## Hardening prompt
Harden this Claude Code setup for production by adding least-privilege permissions, approval gates, tests, monitoring, and rollback guidance.

## Prompt pattern notes
State repository goal, files in scope, constraints, verification commands, commit policy, and whether the agent may edit or only propose.
