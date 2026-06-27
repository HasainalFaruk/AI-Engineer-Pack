# Reflection Framework

## Purpose
Reflection asks the assistant to examine an answer, plan, or implementation after producing it. The goal is to identify mistakes, missing requirements, weak assumptions, and possible improvements before final handoff.

## When to use
- Reviewing a completed draft or code change.
- Checking whether an answer satisfies all user requirements.
- Identifying risks before deployment, release, or review.
- Improving reasoning-heavy outputs.

## When not to use
- When the assistant has not yet gathered enough evidence.
- When immediate action is needed and a review step would delay critical response.
- When the task already has a stronger external verifier, such as tests, that should run first.

## Advantages
- Catches omissions and contradictions.
- Encourages humility about assumptions.
- Works well as a final quality gate.
- Can be paired with checklists for consistent review.

## Limitations
- Reflection is not proof of correctness.
- The assistant may miss its own blind spots.
- Without criteria, reflection can become generic reassurance.

## Prompt structure
```text
Output to review: Provide the answer, plan, or changed artifact.
Criteria: List requirements, constraints, and quality checks.
Reflect: Identify gaps, risks, and unsupported assumptions.
Revise or recommend: Improve the output or state what should change.
Final check: Confirm what remains uncertain.
```

## Practical example
```text
Output to review: A deployment checklist.
Criteria: Rollback, monitoring, database safety, approvals, and communication.
Reflect: Identify missing release risks.
Revise: Add concrete preflight and post-deploy checks.
```

## ChatGPT example
```text
Reflect on the answer you just gave. Check it against my original requirements, identify any weak assumptions, and provide a revised final version only if needed.
```

## Codex example
```text
After making the code change, use Reflection to compare the diff against the request. Look for missed tests, docs, edge cases, and unintended scope expansion, then fix any concrete gaps and rerun verification.
```

## Related frameworks
- [Self-Refine](../self-refine/README.md) for iterative revision.
- [ReAct](../react/README.md) for evidence-gathering before reflection.
- [Chain of Thought](../chain-of-thought/README.md) for stepwise explanations.
- [Tree of Thought](../tree-of-thought/README.md) for evaluating alternatives.
