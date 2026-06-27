# Chain of Thought Framework

## Purpose
Chain of Thought encourages stepwise reasoning for problems that benefit from intermediate analysis. In practical assistant use, the goal is not to expose private reasoning in full, but to ask for a structured, concise explanation of the important steps and assumptions.

## When to use
- Multi-step analysis, math, logic, planning, or debugging explanations.
- Tasks where the final answer should include rationale.
- Teaching or documentation that benefits from visible reasoning checkpoints.
- Reviewing decisions where assumptions need to be inspectable.

## When not to use
- Simple factual answers.
- Sensitive tasks where verbose reasoning could reveal unnecessary details.
- Coding-agent work where tool observations are more important than speculative reasoning.

## Advantages
- Improves clarity on multi-step problems.
- Makes assumptions and intermediate conclusions easier to review.
- Helps users learn the reasoning path.
- Reduces unexplained leaps in final answers.

## Limitations
- Verbose reasoning can obscure the answer.
- Stepwise explanations can still be wrong if premises are wrong.
- For many AI systems, asking for a concise rationale is preferable to requesting hidden reasoning verbatim.

## Prompt structure
```text
Task: State the problem.
Known information: List facts and constraints.
Reasoning checkpoints: Ask for concise intermediate steps or rationale.
Answer: Provide the final result.
Verification: Explain how the answer can be checked.
```

## Practical example
```text
Task: Determine why a deployment plan is risky.
Known information: The release changes database schema, API responses, and client validation.
Reasoning checkpoints: Analyze dependency order, rollback risk, and test coverage.
Answer: Recommend a safer rollout sequence.
Verification: List checks before and after deployment.
```

## ChatGPT example
```text
Analyze this technical decision step by step. Provide a concise rationale, identify assumptions, and end with a recommendation and verification checklist.
```

## Codex example
```text
Explain the likely cause of this failing test with concise reasoning. Inspect the relevant code first, summarize the reasoning checkpoints, apply the fix, and verify with the targeted test.
```

## Related frameworks
- [Plan and Solve](../plan-and-solve/README.md) for plan-first reasoning.
- [Least-to-Most](../least-to-most/README.md) for ordered subproblems.
- [ReAct](../react/README.md) for reasoning grounded in tool actions.
- [Reflection](../reflection/README.md) for checking a completed answer.
