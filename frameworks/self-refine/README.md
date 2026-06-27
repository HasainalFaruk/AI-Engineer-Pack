# Self-Refine Framework

## Purpose
Self-Refine improves an answer or artifact through iterative cycles: draft, critique, revise, and verify. It is useful when quality improves through deliberate review rather than a single pass.

## When to use
- Editing documentation, prompts, proposals, or design notes.
- Improving generated code after an initial implementation.
- Strengthening tests, examples, or explanations.
- Tasks where the first draft is likely incomplete but useful.

## When not to use
- Tasks requiring fresh evidence rather than revision.
- Simple answers where refinement adds little value.
- Changes where repeated edits could introduce churn without a clear quality target.

## Advantages
- Builds critique into the workflow.
- Improves clarity, completeness, and consistency.
- Helps catch omissions before handoff.
- Works well with checklists and rubrics.

## Limitations
- Can loop without improving if criteria are vague.
- May polish the wrong answer if facts were not verified first.
- Needs a stopping rule such as meeting a checklist or passing tests.

## Prompt structure
```text
Draft: Produce the initial answer or artifact.
Critique: Evaluate it against explicit criteria.
Revise: Improve the draft based on critique.
Verify: Check whether the revised version satisfies the goal.
Stop: Summarize final output and remaining risks.
```

## Practical example
```text
Draft a README for a new CLI tool.
Critique it for missing installation, usage, configuration, examples, and troubleshooting.
Revise the README to close the gaps.
Verify that commands and links are consistent.
```

## ChatGPT example
```text
Use Self-Refine on this architecture proposal. First identify clarity, risk, and completeness issues, then rewrite the proposal and provide a short explanation of what improved.
```

## Codex example
```text
Use Self-Refine after implementing the feature. Review the changed files for missed tests, inconsistent naming, and documentation gaps. Apply focused revisions, rerun verification, and summarize the final state.
```

## Related frameworks
- [Reflection](../reflection/README.md) for critique-focused review.
- [Chain of Thought](../chain-of-thought/README.md) for stepwise rationale.
- [CARE](../care/README.md) for example-anchored output.
- [Plan and Solve](../plan-and-solve/README.md) for the initial implementation pass.
