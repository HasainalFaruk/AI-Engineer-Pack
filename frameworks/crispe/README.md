# CRISPE Framework

## Purpose
CRISPE is a detailed prompt framework commonly expanded as Capacity and Role, Insight, Statement, Personality, and Experiment. It is designed to give an assistant a role, context, task, communication character, and room to explore alternatives.

## When to use
- Designing prompts for complex creative or analytical tasks.
- Asking for several solution variants or experiments.
- Combining expert role, background insight, and output behavior.
- Creating higher-fidelity prompts for strategy, product, documentation, or architecture work.

## When not to use
- Simple tasks where a shorter framework would be clearer.
- Strict production changes where experimentation should be limited.
- Situations where the assistant must follow a fixed procedure with no creative latitude.

## Advantages
- Captures more nuance than minimal role-task prompts.
- Encourages exploration instead of a single default answer.
- Helps tune the assistant's voice and behavior.
- Useful for prompt libraries and reusable assistant instructions.

## Limitations
- The acronym is less standardized than CO-STAR or ReAct.
- Can become verbose if every section is filled mechanically.
- Personality and Experiment need clear boundaries for engineering tasks.

## Prompt structure
```text
Capacity and Role: What expertise should the assistant apply?
Insight: What background, constraints, or observations should guide the work?
Statement: What exact task should be completed?
Personality: What communication style or operating behavior is expected?
Experiment: What alternatives, examples, or tests should be explored?
```

## Practical example
```text
Capacity and Role: Act as a pragmatic software architect.
Insight: The team has a small backend service and limited operations support.
Statement: Propose a deployment architecture for predictable releases.
Personality: Be direct, risk-aware, and implementation-oriented.
Experiment: Compare two viable approaches and recommend one with tradeoffs.
```

## ChatGPT example
```text
Use CRISPE to improve this product requirements draft.
Capacity and Role: Product-minded technical editor.
Insight: The audience includes engineering, design, and support.
Statement: Rewrite the requirements for clarity and testability.
Personality: Calm, precise, and collaborative.
Experiment: Provide one concise version and one more detailed version.
```

## Codex example
```text
Use CRISPE for a repository architecture review.
Capacity and Role: Senior software architect.
Insight: Inspect the source tree, tests, and configuration before judging.
Statement: Identify maintainability risks and propose incremental improvements.
Personality: Practical and evidence-based.
Experiment: Offer two implementation paths when tradeoffs are meaningful.
```

## Related frameworks
- [CO-STAR](../co-star/README.md) for communication-focused prompts.
- [Tree of Thought](../tree-of-thought/README.md) for explicit alternatives.
- [Self-Refine](../self-refine/README.md) for iterative improvement.
- [Reflection](../reflection/README.md) for critique after a draft.
