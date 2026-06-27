# ReAct Framework

## Purpose
ReAct combines reasoning and acting. The assistant alternates between deciding what it needs to know, taking an action such as reading a file or running a command, observing the result, and updating its next step.

## When to use
- Debugging, repository inspection, incident analysis, and research tasks.
- Work where facts must be gathered from tools before deciding.
- Tasks that require checking assumptions against external or local evidence.
- Multi-step coding work with verification after changes.

## When not to use
- Pure writing tasks where no investigation is required.
- Sensitive environments where tool actions are risky without explicit approval.
- Simple questions that can be answered directly.

## Advantages
- Grounds conclusions in observations.
- Reduces unsupported assumptions.
- Fits coding agents that can read files, run tests, and inspect outputs.
- Encourages incremental progress and verification.

## Limitations
- Can be slower than direct answering.
- Tool output can distract if the investigation is not scoped.
- Requires discipline to avoid unnecessary actions.
- Internal reasoning should be summarized rather than exposed in excessive detail.

## Prompt structure
```text
Goal: State the outcome.
Context: Provide known constraints and relevant background.
Investigate: Identify what must be inspected or tested.
Act: Use tools or concrete steps to gather facts or make changes.
Observe: Summarize what was learned.
Conclude: Provide the answer, fix, or next action with verification.
```

## Practical example
```text
Goal: Fix a failing login test.
Investigate: Read the test, authentication handler, and recent changes.
Act: Run the targeted test, inspect the failure, apply a focused fix, and rerun it.
Conclude: Summarize the root cause, changed files, and verification.
```

## ChatGPT example
```text
Use a ReAct-style workflow to troubleshoot this API error. Ask for missing logs only if necessary, analyze the evidence I provide, identify likely causes, and give the smallest safe next diagnostic step.
```

## Codex example
```text
Use ReAct to debug the failing checkout flow. Inspect relevant files, run targeted tests, apply a focused fix, rerun verification, and summarize observations without exposing unnecessary internal reasoning.
```

## Related frameworks
- [Plan and Solve](../plan-and-solve/README.md) for up-front decomposition.
- [Reflection](../reflection/README.md) for post-answer critique.
- [Self-Refine](../self-refine/README.md) for iterative revisions.
- [Least-to-Most](../least-to-most/README.md) for solving dependent subproblems.
