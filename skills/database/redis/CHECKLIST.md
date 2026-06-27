# Redis Checklist

- [ ] The affected Redis files, configuration, and runtime path are identified.
- [ ] Existing repository conventions and dependency versions are respected.
- [ ] The solution avoids cache stampedes, missing expirations, unsafe distributed locks, key collisions, and treating cache as source of truth.
- [ ] Security, reliability, and maintainability concerns are reviewed.
- [ ] Verification includes TTL tests, concurrency checks, cache invalidation tests, memory review, and fallback behavior checks.
- [ ] Documentation or examples are updated when setup, behavior, or usage changes.
- [ ] The final summary names residual risks and any checks not run.

