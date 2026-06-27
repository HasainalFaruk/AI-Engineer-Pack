# Tree of Thought Framework

## Purpose
Tree of Thought explores multiple reasoning branches before selecting a solution. Instead of committing to the first plausible answer, the assistant generates alternatives, evaluates them, and chooses or combines the strongest path.

## When to use
- Architecture decisions with meaningful tradeoffs.
- Algorithm design, planning, strategy, or root-cause analysis.
- Problems where the first answer may be locally plausible but globally weak.
- Comparing implementation options before editing code.

## When not to use
- Straightforward tasks with an obvious solution.
- Time-sensitive work where exploration adds little value.
- Cases where there is no room to choose among alternatives.

## Advantages
- Surfaces tradeoffs and hidden assumptions.
- Reduces premature convergence on a weak idea.
- Useful for complex planning and design decisions.
- Can combine strengths from multiple branches.

## Limitations
- More expensive and verbose than direct prompting.
- Requires clear evaluation criteria.
- Can produce artificial alternatives if the problem is simple.
- Does not replace empirical verification.

## Prompt structure
```text
Problem: Define the decision or task.
Criteria: State how options will be evaluated.
Branches: Generate several plausible approaches.
Evaluate: Compare strengths, risks, and constraints.
Select: Recommend one approach or synthesize a hybrid.
Verify: Define how the choice will be tested or reviewed.
```

## Practical example
```text
Problem: Choose a caching strategy for a read-heavy API.
Criteria: Correctness, complexity, invalidation risk, latency, and operational cost.
Branches: In-memory cache, Redis cache, database materialized view.
Evaluate: Compare each option against the criteria.
Select: Recommend the simplest reliable strategy and tests.
```

## ChatGPT example
```text
Use Tree of Thought to compare three onboarding designs for a developer tool. Evaluate each for implementation effort, user clarity, maintainability, and measurable success. Recommend one path with tradeoffs.
```

## Codex example
```text
Use Tree of Thought before refactoring the data access layer. Inspect the current structure, propose three refactor paths, compare risk and test impact, then implement only the selected low-risk path after summarizing it.
```

## Related frameworks
- [Least-to-Most](../least-to-most/README.md) for dependency-ordered decomposition.
- [Plan and Solve](../plan-and-solve/README.md) for a single chosen plan.
- [Reflection](../reflection/README.md) for critique of the selected answer.
- [Self-Refine](../self-refine/README.md) for improving a draft solution.
