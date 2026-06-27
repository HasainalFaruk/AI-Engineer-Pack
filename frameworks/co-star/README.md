# CO-STAR Framework

## Purpose
CO-STAR is a prompt design framework that organizes a request into Context, Objective, Style, Tone, Audience, and Response. It is useful when the quality of the answer depends as much on communication fit as on task completion.

## When to use
- Writing prompts for customer-facing, executive, educational, or brand-sensitive outputs.
- Asking an assistant to transform technical information for a specific audience.
- Creating repeatable prompts where style and tone matter.
- Preparing documentation, reports, proposals, or training material.

## When not to use
- Low-level debugging where repository facts matter more than writing style.
- Tasks with no meaningful audience or tone requirements.
- Situations where the prompt should be extremely compact, such as a one-line command.

## Advantages
- Makes audience and response expectations explicit.
- Reduces mismatched tone, format, and level of detail.
- Works well for documentation, teaching, marketing, and stakeholder communication.
- Easy for non-technical users to understand and reuse.

## Limitations
- Does not provide a reasoning workflow by itself.
- Can overemphasize presentation before facts are validated.
- Needs pairing with ReAct, Plan and Solve, or Reflection for complex engineering tasks.

## Prompt structure
```text
Context: What background, constraints, source material, or repository facts matter?
Objective: What should the assistant accomplish?
Style: What form or writing style should the answer use?
Tone: What emotional or professional register should it have?
Audience: Who will read or use the output?
Response: What format, sections, or deliverable should be returned?
```

## Practical example
```text
Context: We are documenting a new authentication module for maintainers.
Objective: Explain how the module works and how to extend it safely.
Style: Concise technical documentation with headings and examples.
Tone: Professional and direct.
Audience: Backend engineers joining the project.
Response: Return a Markdown guide with setup, flow, extension points, and security notes.
```

## ChatGPT example
```text
Use CO-STAR to turn these meeting notes into a release announcement.
Context: The release adds offline mode, faster startup, and improved error messages.
Objective: Produce an announcement that explains value without overselling.
Style: Product update.
Tone: Clear, confident, and friendly.
Audience: Existing SaaS customers.
Response: Markdown with a title, summary, feature sections, and migration notes.
```

## Codex example
```text
Use CO-STAR to update the repository documentation.
Context: Inspect the authentication files and existing docs first.
Objective: Create maintainer-facing documentation for the login flow.
Style: GitHub Markdown.
Tone: Precise and practical.
Audience: Engineers who will modify the code later.
Response: Update the relevant README and summarize changed files plus verification.
```

## Related frameworks
- [RISE](../rise/README.md) for role-driven work.
- [CRISPE](../crispe/README.md) for richer prompt constraints.
- [CARE](../care/README.md) for action-and-result prompts.
- [Plan and Solve](../plan-and-solve/README.md) for execution planning.
