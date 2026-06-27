# Skeleton of Thought Framework

## Purpose
Skeleton of Thought first creates a concise outline, then expands each part. It is useful for producing organized long-form answers without losing structure.

## When to use
- Long documentation, reports, tutorials, or implementation plans.
- Tasks where structure should be approved or inspected before detail.
- Generating comprehensive content while preserving scanability.
- Breaking a large answer into stable sections.

## When not to use
- Short answers or simple edits.
- Tasks where the structure is already fixed.
- Debugging work that depends on tool observations rather than outline expansion.

## Advantages
- Prevents rambling long-form output.
- Makes gaps visible early.
- Supports incremental expansion.
- Useful for documentation and planning artifacts.

## Limitations
- A weak outline leads to weak expansion.
- Can become too rigid if new evidence changes the structure.
- Does not by itself validate technical correctness.

## Prompt structure
```text
Goal: Define the final artifact.
Skeleton: Draft the main sections or steps.
Review: Check the skeleton for missing or unnecessary parts.
Expand: Fill each section with concise detail.
Verify: Confirm the final output matches the requested scope.
```

## Practical example
```text
Goal: Create a runbook for incident response.
Skeleton: Detection, severity, ownership, diagnostics, mitigation, communication, postmortem.
Expand: Add concrete steps and examples under each heading.
Verify: Check that on-call engineers can follow it under pressure.
```

## ChatGPT example
```text
Use Skeleton of Thought to create a tutorial. Start with the section outline, then expand each section with concise explanations and examples. Keep the final result in Markdown.
```

## Codex example
```text
Use Skeleton of Thought to add developer documentation. Inspect the code first, draft the README outline, expand each section with repository-specific facts, and verify links and commands.
```

## Related frameworks
- [CARE](../care/README.md) for example-anchored sections.
- [Plan and Solve](../plan-and-solve/README.md) for execution planning.
- [CO-STAR](../co-star/README.md) for audience-sensitive long-form writing.
- [Self-Refine](../self-refine/README.md) for improving the expanded draft.
