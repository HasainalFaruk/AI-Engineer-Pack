# Production Debugging Workflow

## 1. Identify the Production Debugging surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Production Debugging and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for live incident diagnosis using logs, metrics, traces, feature flags, rollbacks, and customer impact analysis.

## 5. Verify with the right tools
Use timeline reconstruction, metric correlation, safe probes, rollback validation, and post-incident regression checks. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Production Debugging.

