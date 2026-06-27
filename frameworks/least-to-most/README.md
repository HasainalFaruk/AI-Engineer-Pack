# Least-to-Most Framework

## Purpose
Least-to-Most decomposes a hard problem into simpler subproblems and solves them in dependency order. Each smaller result supports the next, making complex tasks more tractable.

## When to use
- Problems with clear prerequisite steps.
- Debugging where basic facts must be established before deeper causes.
- Algorithm, migration, or architecture tasks that build from foundations.
- Teaching complex concepts progressively.

## When not to use
- Problems where alternatives must be explored in parallel.
- Simple tasks that do not need decomposition.
- Situations where dependency order is unknown and requires discovery first.

## Advantages
- Reduces cognitive load.
- Makes progress measurable.
- Helps avoid skipping foundational checks.
- Works well for tutorials and complex implementation plans.

## Limitations
- Can be too linear for ambiguous design problems.
- Requires good decomposition judgment.
- May miss cross-cutting concerns if subproblems are isolated too strongly.

## Prompt structure
```text
Problem: State the complex goal.
Decompose: Break it into ordered subproblems from simplest to hardest.
Solve: Address each subproblem using prior answers.
Integrate: Combine the results into the final solution.
Verify: Check that the integrated answer satisfies the original goal.
```

## Practical example
```text
Problem: Add role-based access control.
Decompose: Identify roles, map permissions, inspect auth flow, design checks, implement middleware, add tests.
Solve: Complete each step before moving to the next.
Integrate: Document how roles are enforced across the app.
```

## ChatGPT example
```text
Use Least-to-Most to teach how OAuth works. Start with actors, then tokens, then authorization flow, then refresh behavior, then common implementation risks.
```

## Codex example
```text
Use Least-to-Most to implement permissions. First inspect existing auth primitives, then add the smallest permission model, then wire it into routes, then add tests and docs.
```

## Related frameworks
- [Plan and Solve](../plan-and-solve/README.md) for general task planning.
- [Chain of Thought](../chain-of-thought/README.md) for concise stepwise rationale.
- [ReAct](../react/README.md) for tool-grounded subproblem solving.
- [Tree of Thought](../tree-of-thought/README.md) for comparing branches when order is not obvious.
