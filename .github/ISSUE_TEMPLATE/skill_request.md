---
name: Skill request
description: Request a new skill category, technology-specific skill, or improvement to an existing skill
title: "Skill: "
labels: [skill, enhancement, needs-triage]
assignees: []
---

## Skill request type
Select one:

- [ ] New skill category under `skills/`
- [ ] New technology-specific skill under an existing category
- [ ] Improvement to an existing skill
- [ ] New prompts, workflow, checklist, or examples for an existing skill

## Proposed skill path
Use the existing structure where possible.

```text
skills/languages/rust/
skills/web/svelte/
skills/cloud/aws/
```

## Purpose
What should this skill help AI assistants do? Be specific about the technology, workflow, or engineering domain.

## Expected files
A complete technology skill should include:

- [ ] `README.md`
- [ ] `SKILL.md`
- [ ] `WORKFLOW.md`
- [ ] `PROMPTS.md`
- [ ] `CHECKLIST.md`
- [ ] `EXAMPLES.md`

## Use cases
List practical tasks this skill should support, such as build, debug, review, test, deploy, document, or optimize.

## Technology-specific guidance
Describe important tools, conventions, verification methods, risks, or common mistakes the skill should cover.

## Example prompt
Provide one example prompt that should work with this skill.

```text
Use the proposed skill to review a configuration change for security, deployment risk, and missing tests.
```

## Related pack resources
Link related commands, frameworks, templates, or checklists if known.

## Contribution notes
If you want to implement this skill, follow the skill structure described in [CONTRIBUTING.md](../../CONTRIBUTING.md) and preserve existing category folders.
