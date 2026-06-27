# Document Command

## Purpose
The document command creates or updates Markdown guidance so users, maintainers, operators, or reviewers can understand and use a system. It focuses on accuracy, audience fit, examples, and durable maintenance value.

## Inputs
- Documentation goal and target audience.
- Source code, configuration, existing docs, examples, or release notes.
- Required format, location, tone, and depth.
- Known behavior, setup steps, troubleshooting notes, and limitations.

## Outputs
- New or updated documentation in the correct repository location.
- Examples, commands, diagrams, or checklists where useful.
- Cross-links to related files.
- Summary of documentation scope and any unverified assumptions.

## Step-by-step workflow
1. Identify the audience and what they need to accomplish.
2. Inspect source material instead of relying on assumptions.
3. Choose the right documentation type: README, guide, reference, runbook, FAQ, or decision record.
4. Draft clear sections with examples and links to related material.
5. Verify commands, paths, configuration names, and behavior descriptions.
6. Remove stale or contradictory text when updating existing docs.
7. Summarize what was documented and what remains uncertain.

## Best practices
- Write for the reader's task, not the author's implementation memory.
- Prefer concrete examples over abstract descriptions.
- Keep headings consistent and scannable.
- Cross-link related docs, templates, and checklists.
- Update documentation in the same change that updates behavior.

## Common mistakes
- Documenting behavior without inspecting the code.
- Leaving placeholders, stale commands, or broken links.
- Writing only for experts when the audience includes new contributors.
- Duplicating information that should be linked instead.
- Forgetting troubleshooting and limitations.

## Example prompt
```text
Use the document command to create maintainer documentation for the job queue. Inspect the code first, explain setup, flow, configuration, failure handling, and testing, then add cross-links to related docs.
```

## Example output
```text
Updated job queue documentation.

Added sections:
- Runtime overview.
- Configuration reference.
- Retry and failure behavior.
- Local testing workflow.
- Troubleshooting checklist.

Verification:
- Checked file paths and configuration names against source.
```

## Related skills
- [Documentation](../../skills/documentation/README.md)
- [Architecture](../../skills/architecture/README.md)
- [Review](../../skills/review/README.md)
- [Testing](../../skills/testing/README.md)

## Related frameworks
- [CO-STAR](../../frameworks/co-star/README.md)
- [Skeleton of Thought](../../frameworks/skeleton-of-thought/README.md)
- [CARE](../../frameworks/care/README.md)
- [Self-Refine](../../frameworks/self-refine/README.md)
