# Event-Driven Architecture Workflow

## 1. Identify the Event-Driven Architecture surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Event-Driven Architecture and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for events, producers, consumers, schemas, idempotency, ordering, retries, and eventual consistency.

## 5. Verify with the right tools
Use schema compatibility checks, replay tests, idempotency tests, dead-letter handling, and observability review. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Event-Driven Architecture.

