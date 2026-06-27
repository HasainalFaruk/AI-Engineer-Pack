# BAB Framework

## Purpose
BAB stands for Before, After, Bridge. It is a persuasion and transformation framework that clarifies the current state, the desired future state, and the path connecting them.

## When to use
- Writing proposals, migration plans, product copy, or change narratives.
- Explaining why a technical change matters.
- Helping stakeholders understand the value of a refactor, tool, or process improvement.
- Framing documentation around user pain and improvement.

## When not to use
- Neutral analysis where persuasive framing would bias the answer.
- Debugging or code review tasks that require evidence over narrative.
- Situations where the desired future state is unknown or contested.

## Advantages
- Makes value and motivation explicit.
- Helps connect technical work to user or business outcomes.
- Produces clear before-and-after comparisons.
- Useful for adoption, migration, and release communication.

## Limitations
- Can oversimplify complex tradeoffs.
- May sound too sales-oriented if used for internal engineering analysis.
- Needs factual support to avoid vague transformation claims.

## Prompt structure
```text
Before: Describe the current pain, limitation, or risk.
After: Describe the desired outcome or improved state.
Bridge: Explain the actions, design, or plan that moves from Before to After.
```

## Practical example
```text
Before: Deployments are manual, inconsistent, and hard to audit.
After: Releases are repeatable, reviewed, and recoverable.
Bridge: Introduce a GitHub Actions pipeline with tests, build artifacts, environment approvals, and rollback notes.
```

## ChatGPT example
```text
Use BAB to write a concise internal proposal.
Before: Support engineers manually recreate customer issues with incomplete context.
After: Support has a structured diagnostic checklist and faster escalation path.
Bridge: Propose a shared incident template, logging checklist, and weekly review process.
```

## Codex example
```text
Use BAB to document the impact of a refactor.
Before: Inspect the current module and identify maintainability pain points.
After: Explain the simpler target structure and expected developer benefits.
Bridge: Update the architecture note with migration steps and verification checks.
```

## Related frameworks
- [CARE](../care/README.md) for context-action-result prompts.
- [CO-STAR](../co-star/README.md) for audience-aware communication.
- [Reverse Prompting](../reverse-prompting/README.md) for deriving a prompt from a desired output.
- [Plan and Solve](../plan-and-solve/README.md) for implementation planning.
