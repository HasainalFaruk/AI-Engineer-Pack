# Redis Prompts

## Build
Use the Redis skill. Inspect existing project conventions, implement the requested change using idiomatic Redis patterns, verify with TTL tests, concurrency checks, cache invalidation tests, memory review, and fallback behavior checks, and summarize changed files and risks.

## Review
Use the Redis skill. Review the change for correctness, maintainability, security, performance, and Redis-specific pitfalls such as cache stampedes, missing expirations, unsafe distributed locks, key collisions, and treating cache as source of truth. Provide findings by severity.

## Debug
Use the Redis skill. Reproduce or reason through the issue, inspect relevant files and runtime signals, identify the likely cause, apply a focused fix if requested, and verify with TTL tests, concurrency checks, cache invalidation tests, memory review, and fallback behavior checks.

## Document
Use the Redis skill. Create documentation that explains setup, usage, configuration, limitations, and troubleshooting for this repository's Redis implementation.

