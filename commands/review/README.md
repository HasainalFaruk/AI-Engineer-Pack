# Review Command

## Purpose
The review command evaluates code, documentation, designs, or plans for correctness, risk, maintainability, missing tests, and alignment with requirements. It prioritizes actionable findings over general commentary.

## Inputs
- Diff, pull request, file list, design document, or implementation summary.
- Original requirements or acceptance criteria.
- Test results, logs, screenshots, or reproduction details when available.
- Project conventions and relevant checklists.

## Outputs
- Findings ordered by severity with file references when possible.
- Clear explanation of impact and suggested remediation.
- Open questions or assumptions that affect confidence.
- Brief summary of what was reviewed and any test gaps.

## Step-by-step workflow
1. Identify the review target and expected behavior.
2. Inspect changed files and nearby code paths that depend on them.
3. Compare the change against requirements, conventions, and risk areas.
4. Look for correctness bugs, security issues, regressions, missing tests, and unclear docs.
5. Rank findings by severity and remove low-value style-only noise.
6. Provide concrete fixes or next investigative steps.
7. State test coverage reviewed and remaining uncertainty.

## Best practices
- Lead with findings, not praise or broad summaries.
- Cite exact files and lines when available.
- Explain why each issue matters to users, maintainers, or production behavior.
- Distinguish confirmed bugs from questions or possible improvements.
- Keep recommendations scoped to the reviewed change.

## Common mistakes
- Treating preferences as defects.
- Missing behavior outside the changed file.
- Reporting issues without impact or remediation.
- Burying severe findings under long summaries.
- Ignoring tests and documentation gaps.

## Example prompt
```text
Use the review command on this diff. Focus on correctness, regressions, security, missing tests, and documentation gaps. Put findings first, ordered by severity, with file and line references where possible.
```

## Example output
```text
Findings:
- High: app/auth/session.py:42 allows expired refresh tokens because the expiry check compares against issue time instead of expiration time. This can keep sessions valid longer than intended.
- Medium: tests/auth/test_session.py lacks a regression test for expired refresh tokens.

Open questions:
- Should refresh token expiry be enforced at middleware or service level?
```

## Related skills
- [Review](../../skills/review/README.md)
- [Security](../../skills/security/README.md)
- [Testing](../../skills/testing/README.md)
- [Architecture](../../skills/architecture/README.md)

## Related frameworks
- [Reflection](../../frameworks/reflection/README.md)
- [ReAct](../../frameworks/react/README.md)
- [Chain of Thought](../../frameworks/chain-of-thought/README.md)
- [Self-Refine](../../frameworks/self-refine/README.md)
