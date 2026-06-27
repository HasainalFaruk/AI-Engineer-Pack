# LangGraph Prompt Patterns

## Build prompt
Use LangGraph to build an agent that achieves a specific goal. List allowed tools, forbidden actions, approval requirements, output contract, and verification steps.

## Review prompt
Review this LangGraph design for tool permissions, state handling, prompt injection risk, failure recovery, observability, and deployment readiness. Return severity-ranked findings and concrete fixes.

## Debug prompt
Debug this LangGraph run. Use traces, tool logs, prompts, state, and final output to identify the first bad decision. Recommend the smallest fix and a regression test.

## Production hardening prompt
Harden this LangGraph workflow for production. Add validation, least-privilege tools, human approval points, retries, timeouts, observability, and rollback guidance.

## Prompt pattern notes
Prompt each node for one responsibility and make routing decisions inspectable; avoid one giant system prompt that hides the graph design.
