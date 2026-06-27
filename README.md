# AI Engineer Pack

The AI Engineer Pack is a complete Markdown knowledge base for AI-assisted software engineering. It gives ChatGPT, Codex, GitHub Copilot, OpenAI Agents, and future coding assistants a shared structure for understanding tasks, selecting workflows, producing artifacts, and validating results.

## Repository Map
- [system](system/README.md): operating principles, quality standards, and guardrails.
- [routers](routers/README.md): decision rules for choosing the right pack resources.
- [frameworks](frameworks/README.md): prompt engineering frameworks and examples.
- [commands](commands/README.md): reusable workflows for common task verbs.
- [chatgpt](chatgpt/README.md): ChatGPT-specific usage guidance.
- [codex](codex/README.md): Codex-style agent collaboration guidance.
- [skills](skills/README.md): domain-specific playbooks.
- [templates](templates/README.md): starter templates for common projects.
- [checklists](checklists/README.md): delivery and review quality gates.
- [examples](examples/README.md): applied workflow examples.
- [docs](docs/README.md): roadmap, architecture, contribution, and FAQ documentation.
- [scripts](scripts/README.md): maintenance and validation helpers.
- [.github](.github/README.md): GitHub collaboration and automation configuration.

## Recommended Workflow
1. Use [routers](routers/README.md) to classify the request.
2. Select a task command from [commands](commands/README.md).
3. Choose a prompt framework from [frameworks](frameworks/README.md).
4. Apply one or more domain skills from [skills](skills/README.md).
5. Start from a template when creating a new artifact.
6. Validate with the matching checklist.
7. Record lasting decisions in [docs](docs/README.md).

## Example
A request to design and build a secure FastAPI service can combine [commands/design](commands/design/README.md), [frameworks/plan-and-solve](frameworks/plan-and-solve/README.md), [skills/security](skills/security/README.md), [templates/fastapi](templates/fastapi/README.md), and [checklists/testing](checklists/testing/README.md).

## Quality Standard
Documentation in this pack should be complete, specific, cross-linked, and usable without additional explanation. Avoid vague placeholders, unexplained jargon, and instructions that cannot be verified.
