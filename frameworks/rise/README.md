# RISE Framework

## Purpose
RISE structures prompts around Role, Input, Steps, and Expectation. It is a lightweight way to tell an assistant who to act as, what material to use, how to proceed, and what good output looks like.

## When to use
- You need a compact but complete prompt for routine work.
- The assistant should follow a specific professional role.
- The task has clear source material and an expected output.
- You want a repeatable prompt for support, analysis, documentation, or implementation planning.

## When not to use
- The task requires exploring multiple strategies or alternatives in depth.
- The assistant must use tools iteratively and revise based on observations.
- The prompt needs detailed tone, audience, or style controls.

## Advantages
- Simple enough for everyday use.
- Encourages procedural clarity without becoming verbose.
- Works across technical and non-technical tasks.
- Helps prevent vague role prompts by tying the role to inputs and expectations.

## Limitations
- Less expressive than CO-STAR for audience and tone.
- Less rigorous than ReAct for tool-based investigation.
- The Steps section can become too shallow for complex engineering work unless expanded.

## Prompt structure
```text
Role: Define the assistant's professional perspective.
Input: Provide source material, files, constraints, and context.
Steps: List the process the assistant should follow.
Expectation: Define the final output, quality bar, and validation criteria.
```

## Practical example
```text
Role: Senior API designer.
Input: Existing endpoint list, authentication requirements, and error format.
Steps: Identify resource boundaries, propose routes, define request and response schemas, and list tests.
Expectation: Return a concise API design with tradeoffs and open questions.
```

## ChatGPT example
```text
Role: Technical writing editor.
Input: The draft onboarding guide below.
Steps: Improve structure, remove repetition, preserve meaning, and add missing setup warnings.
Expectation: Return a polished Markdown guide and a short summary of major edits.
```

## Codex example
```text
Role: Senior repository maintainer.
Input: Current codebase, failing test output, and the user's bug report.
Steps: Inspect relevant files, identify the cause, make a focused fix, and run targeted verification.
Expectation: Summarize changed files, tests run, and any remaining risk.
```

## Related frameworks
- [CO-STAR](../co-star/README.md) for audience and tone control.
- [CARE](../care/README.md) for context-action-result framing.
- [Plan and Solve](../plan-and-solve/README.md) for more detailed task decomposition.
- [ReAct](../react/README.md) for tool-assisted investigation.
