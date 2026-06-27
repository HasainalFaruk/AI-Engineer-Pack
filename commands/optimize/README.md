# Optimize Command

## Purpose
The optimize command improves performance, cost, reliability, accessibility, developer workflow, or operational efficiency while preserving required behavior. It is evidence-driven and focuses on measurable bottlenecks.

## Inputs
- Optimization target and success metric.
- Baseline measurements, logs, profiling data, traces, or user reports.
- Relevant code, infrastructure, queries, assets, or workflows.
- Constraints such as cost, compatibility, security, and maintainability.

## Outputs
- Diagnosis of the bottleneck or inefficiency.
- Focused optimization plan or implementation.
- Before-and-after measurements where possible.
- Risks, tradeoffs, and follow-up monitoring recommendations.

## Step-by-step workflow
1. Define what should improve and how it will be measured.
2. Establish a baseline using existing metrics, tests, profiling, or reproducible scenarios.
3. Identify the highest-impact bottleneck rather than guessing.
4. Choose the least risky optimization that addresses the measured problem.
5. Implement the change with behavior-preserving tests.
6. Measure again and compare against the baseline.
7. Document tradeoffs, monitoring needs, and remaining opportunities.

## Best practices
- Measure before and after changes.
- Optimize the bottleneck, not the most visible code.
- Protect correctness with tests before changing performance-sensitive paths.
- Prefer simple improvements over complex cleverness.
- Consider operational cost and maintainability, not only speed.

## Common mistakes
- Optimizing without a baseline.
- Making code harder to maintain for a tiny gain.
- Improving one metric while harming reliability or accessibility.
- Ignoring database, network, or asset bottlenecks.
- Claiming success without measurement.

## Example prompt
```text
Use the optimize command to improve slow product search. Establish a baseline, inspect query and indexing patterns, propose the safest improvement, implement it if clear, and report before-and-after evidence.
```

## Example output
```text
Optimized product search query.

Baseline:
- Median query time: 820 ms on seeded local data.

Change:
- Added composite index for tenant_id and normalized_name.
- Updated query to use normalized prefix search.

After:
- Median query time: 110 ms on the same dataset.

Risk:
- Migration adds an index and should be scheduled during low traffic.
```

## Related skills
- [Database](../../skills/database/README.md)
- [DevOps](../../skills/devops/README.md)
- [Cloud](../../skills/cloud/README.md)
- [Testing](../../skills/testing/README.md)

## Related frameworks
- [ReAct](../../frameworks/react/README.md)
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [Tree of Thought](../../frameworks/tree-of-thought/README.md)
- [Reflection](../../frameworks/reflection/README.md)
