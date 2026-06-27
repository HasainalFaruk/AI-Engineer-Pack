# Redis Examples

## Implementation example
Request: Use the Redis skill to add a small feature in the current repository, follow existing conventions, and verify with TTL tests, concurrency checks, cache invalidation tests, memory review, and fallback behavior checks.

Expected output: A focused implementation summary, changed files, verification results, and notes about Redis-specific risks.

## Review example
Request: Use the Redis skill to review a pull request for correctness and risks.

Expected output: Severity-ranked findings that call out issues such as cache stampedes, missing expirations, unsafe distributed locks, key collisions, and treating cache as source of truth.

## Debugging example
Request: Use the Redis skill to investigate a failure involving caching, queues, rate limits, locks, session stores, TTL strategy, and memory-sensitive data structures.

Expected output: Root cause, focused fix or recommendation, verification evidence, and remaining uncertainty.

