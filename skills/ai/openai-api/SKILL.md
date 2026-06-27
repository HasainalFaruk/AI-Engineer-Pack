# OpenAI API Skill Definition

## Capability
Use this skill for model selection, prompts, tool use, structured outputs, evals, safety behavior, and latency/cost control. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with schema validation, eval sets, prompt regression tests, token and latency checks, and failure-mode tests.

## Best for
- Designing or modifying OpenAI API-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on OpenAI API tooling or runtime behavior.
- Creating prompts or workflows that require accurate OpenAI API terminology.

## Inputs
- User goal, acceptance criteria, and affected environment.
- Relevant source files, config files, dependencies, logs, or test output.
- Version constraints and deployment context.
- Security, performance, accessibility, reliability, or maintenance requirements.

## Outputs
- Focused plan, implementation, review, or debugging guidance.
- Technology-specific risks, tradeoffs, and verification steps.
- Updated docs or examples when behavior or usage changes.

## Watch for
Avoid unbounded prompts, missing evals, fragile JSON parsing, tool-call ambiguity, and no fallback behavior.

