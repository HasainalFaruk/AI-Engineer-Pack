# CrewAI Prompt Patterns

## Build prompt
Use CrewAI to build an agent that achieves a specific goal. List allowed tools, forbidden actions, approval requirements, output contract, and verification steps.

## Review prompt
Review this CrewAI design for tool permissions, state handling, prompt injection risk, failure recovery, observability, and deployment readiness. Return severity-ranked findings and concrete fixes.

## Debug prompt
Debug this CrewAI run. Use traces, tool logs, prompts, state, and final output to identify the first bad decision. Recommend the smallest fix and a regression test.

## Production hardening prompt
Harden this CrewAI workflow for production. Add validation, least-privilege tools, human approval points, retries, timeouts, observability, and rollback guidance.

## Prompt pattern notes
Give each agent a narrow role, concrete goal, tool boundary, expected output, and collaboration rule with the rest of the crew.
