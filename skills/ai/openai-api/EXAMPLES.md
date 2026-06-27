# OpenAI API Examples

## Implementation example
Request: Use the OpenAI API skill to add a small feature in the current repository, follow existing conventions, and verify with schema validation, eval sets, prompt regression tests, token and latency checks, and failure-mode tests.

Expected output: A focused implementation summary, changed files, verification results, and notes about OpenAI API-specific risks.

## Review example
Request: Use the OpenAI API skill to review a pull request for correctness and risks.

Expected output: Severity-ranked findings that call out issues such as unbounded prompts, missing evals, fragile JSON parsing, tool-call ambiguity, and no fallback behavior.

## Debugging example
Request: Use the OpenAI API skill to investigate a failure involving model selection, prompts, tool use, structured outputs, evals, safety behavior, and latency/cost control.

Expected output: Root cause, focused fix or recommendation, verification evidence, and remaining uncertainty.

