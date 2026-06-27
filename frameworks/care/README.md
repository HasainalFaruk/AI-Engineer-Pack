# CARE Framework

## Purpose
CARE stands for Context, Action, Result, and Example. It frames a prompt around the situation, the work to perform, the expected outcome, and a concrete sample that anchors quality.

## When to use
- You want a practical prompt that includes both instructions and an example.
- The assistant needs to produce a repeatable format.
- The task is clear but output quality depends on seeing the desired pattern.
- Creating documentation, issue templates, review comments, or structured summaries.

## When not to use
- Exploratory research where examples might narrow thinking too early.
- Tasks requiring deep tool iteration or multi-branch reasoning.
- Situations where no representative example is available.

## Advantages
- Examples reduce ambiguity quickly.
- Works well for reusable operational prompts.
- Encourages output-oriented thinking.
- Easier to adopt than larger frameworks.

## Limitations
- A poor example can bias the model toward bad structure.
- Does not force explicit risk analysis unless included in Result.
- Less suitable for complex design choices without additional reasoning steps.

## Prompt structure
```text
Context: What is the situation, source material, and constraint set?
Action: What should the assistant do?
Result: What final output and quality bar are required?
Example: What sample format, style, or level of detail should be followed?
```

## Practical example
```text
Context: We need consistent pull request summaries for backend changes.
Action: Summarize the change, tests, risks, and rollout notes.
Result: Return a Markdown PR description that reviewers can scan quickly.
Example: Use sections for Summary, Verification, Risk, and Rollback.
```

## ChatGPT example
```text
Context: I am preparing a weekly engineering update from raw notes.
Action: Group the notes into shipped work, in-progress work, blockers, and next steps.
Result: Return a concise update for engineering leadership.
Example: Use bullet points with owners only where explicitly provided.
```

## Codex example
```text
Context: Inspect the changed files in this repository.
Action: Produce a PR-ready summary of implementation, tests, and risks.
Result: Update the requested Markdown file or return the summary if no file is specified.
Example: Use headings Summary, Verification, and Notes.
```

## Related frameworks
- [RISE](../rise/README.md) for role-input-step-expectation prompts.
- [CO-STAR](../co-star/README.md) for audience and tone control.
- [BAB](../bab/README.md) for before-after transformation narratives.
- [Skeleton of Thought](../skeleton-of-thought/README.md) for structured outlines.
