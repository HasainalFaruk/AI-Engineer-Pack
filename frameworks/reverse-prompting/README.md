# Reverse Prompting Framework

## Purpose
Reverse Prompting starts from a desired output and works backward to infer the prompt, inputs, constraints, and examples needed to reproduce that output reliably.

## When to use
- You have a good example output and want a reusable prompt.
- Standardizing reports, summaries, reviews, or documentation formats.
- Turning expert-written artifacts into repeatable assistant instructions.
- Improving prompt libraries by deriving prompts from successful results.

## When not to use
- When the example output is poor, incomplete, or misleading.
- When the desired output depends on hidden context that cannot be supplied.
- When originality is more important than reproducibility.

## Advantages
- Produces prompts grounded in real target quality.
- Helps uncover missing inputs and constraints.
- Useful for standardizing team workflows.
- Can convert one-off success into reusable process.

## Limitations
- Can overfit to a single example.
- May copy surface style while missing deeper reasoning.
- Needs multiple examples for robust prompt design when outputs vary.

## Prompt structure
```text
Target output: Provide the desired artifact or example.
Analyze: Identify structure, tone, assumptions, and required inputs.
Infer prompt: Draft instructions that would produce a similar output.
Test: Apply the prompt to a new input.
Refine: Adjust instructions based on differences.
```

## Practical example
```text
Target output: A strong pull request review summary.
Analyze: It includes severity, file references, impact, and suggested fixes.
Infer prompt: Ask the assistant to inspect a diff and report findings first, then tests and summary.
Test: Use the prompt on another change.
```

## ChatGPT example
```text
Use Reverse Prompting on this excellent project brief. Infer the reusable prompt that would generate briefs with the same structure, quality bar, and level of detail. Then provide the prompt and explain required inputs.
```

## Codex example
```text
Use Reverse Prompting to create a reusable Codex prompt from this successful bug-fix summary. Infer the repository inspection steps, verification expectations, and final response format, then save the prompt in the relevant docs file.
```

## Related frameworks
- [CARE](../care/README.md) for example-driven prompting.
- [CO-STAR](../co-star/README.md) for audience and response shaping.
- [Self-Refine](../self-refine/README.md) for improving the inferred prompt.
- [Reflection](../reflection/README.md) for checking whether the prompt captures the target output.
