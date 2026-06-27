# Contributing

Thank you for improving the AI Engineer Pack. This repository is a Markdown-first toolkit for ChatGPT, Codex, GitHub Copilot, OpenAI Agents, and future AI coding assistants.

## Contribution principles
- Keep changes specific to the AI Engineer Pack.
- Preserve existing folder structure and filenames unless a change explicitly requires otherwise.
- Use professional Markdown with clear headings and realistic examples.
- Avoid placeholders, generic filler, and unresolved drafting notes.
- Cross-link related commands, frameworks, skills, templates, checklists, and documentation.
- Run validation scripts before opening a pull request.

## Recommended workflow
1. Search existing issues and documentation for related work.
2. Identify the affected folder and expected file conventions.
3. Make the smallest complete change that solves the problem.
4. Run `python scripts/validate.py` from the repository root.
5. Open a pull request using [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md).

## Skill contributions
Technology-specific skills belong under an existing category folder, such as `skills/web/react/` or `skills/cloud/aws/`. A complete skill folder includes:

- `README.md`
- `SKILL.md`
- `WORKFLOW.md`
- `PROMPTS.md`
- `CHECKLIST.md`
- `EXAMPLES.md`

## Documentation quality
Good documentation in this repository is actionable, concrete, and easy for both humans and AI assistants to follow. Include examples when a workflow could be misunderstood.

## More detail
Project-level contribution notes also live in [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).
