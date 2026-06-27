# Plan and Solve Framework

## Purpose
Plan and Solve separates planning from execution. The assistant first decomposes the task, then follows the plan to produce the answer or implementation. This reduces missed steps in multi-part work.

## When to use
- Implementation tasks that touch multiple files.
- Debugging work with several likely causes.
- Documentation or migration tasks with several deliverables.
- Any request where execution order affects correctness.

## When not to use
- Small tasks where planning would be overhead.
- Emergencies where the first diagnostic action is obvious and urgent.
- Highly exploratory work where Tree of Thought is needed before choosing a plan.

## Advantages
- Creates a visible execution path.
- Helps identify dependencies and verification points early.
- Reduces skipped requirements.
- Works especially well for coding agents.

## Limitations
- A bad initial plan can still lead to bad execution.
- Plans must be updated when new evidence appears.
- Can become rigid if treated as a contract instead of a working guide.

## Prompt structure
```text
Goal: Define the desired outcome.
Context: Provide repository, user, and constraint information.
Plan: Break the task into ordered steps.
Solve: Execute each step, updating the plan if needed.
Verify: Run checks or review criteria.
Report: Summarize changes, evidence, and risks.
```

## Practical example
```text
Goal: Add CSV export to an admin page.
Plan: Inspect existing export patterns, add backend endpoint, add UI action, add tests, update docs.
Solve: Implement each step in order.
Verify: Run targeted backend and frontend checks.
```

## ChatGPT example
```text
Use Plan and Solve to create a migration plan for moving from manual releases to automated deployments. Start with a numbered plan, then expand each step with owners, risks, and validation.
```

## Codex example
```text
Use Plan and Solve to implement the requested feature. Inspect the codebase, create a short plan, make the changes, run targeted verification, and summarize files changed plus tests run.
```

## Related frameworks
- [ReAct](../react/README.md) for tool-based investigation during execution.
- [Least-to-Most](../least-to-most/README.md) for dependency-heavy problems.
- [Self-Refine](../self-refine/README.md) for improving the first solution.
- [Tree of Thought](../tree-of-thought/README.md) for comparing plans before choosing one.
