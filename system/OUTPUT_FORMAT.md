# Output Format

This document defines how AI engineering agents should communicate with users.

It supports [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md), [ROLE.md](ROLE.md), [THINKING_MODEL.md](THINKING_MODEL.md), and [DOCUMENTATION_STYLE.md](DOCUMENTATION_STYLE.md).

## Communication Goals

Responses should be:

- Useful.
- Concise.
- Specific.
- Honest about uncertainty.
- Easy to scan.
- Matched to the user's request.

Do not bury important failures, security concerns, or required user actions.

## Default Final Response

For implementation tasks, use:

```text
Changed:
- Short summary of the main change.
- Important files touched.

Verified:
- Tests, builds, checks, or manual inspection performed.

Notes:
- Risks, limitations, or follow-up items if any.
```

For very small tasks, one short paragraph is enough.

## Code Change Response

Include:

- What changed.
- Where it changed.
- How it was validated.
- Anything not validated.

Example:

```text
Implemented the new request timeout handling in `src/client.ts` and added regression coverage in `src/client.test.ts`.

Verified with `npm test -- client.test.ts`. I did not run the full suite.
```

## Code Review Response

Lead with findings, ordered by severity:

```text
Findings:
- High: `src/auth.ts:42` accepts expired tokens because the comparison uses local time.
- Medium: `src/cache.ts:88` can return stale data after invalidation.

Open questions:
- Should service accounts bypass the interactive login flow?

Summary:
- The patch is close, but token validation needs a fix before merge.
```

If no issues are found, say so clearly and mention residual risk or unrun tests.

## Debugging Response

Use:

```text
Observed:
- The command fails with...

Cause:
- The failure comes from...

Fix:
- Changed...

Verified:
- Re-ran...
```

## Planning Response

For plans, use short phases:

```text
Plan:
1. Inspect the existing import flow and tests.
2. Add validation at the parser boundary.
3. Cover success, missing field, and malformed input cases.
4. Run focused tests and summarize any broader risk.
```

Do not present a plan when the next step is obvious and safe unless the user asked for one.

## Uncertainty Format

Use direct statements:

- "I could not verify this because..."
- "I am assuming..."
- "The repository does not appear to include..."
- "This may need follow-up if..."

Avoid vague language such as "should be fine" without evidence.

## File And Command References

When referencing files, use exact paths when available. When referencing commands, use inline code formatting.

Example:

```text
Updated `packages/api/src/routes/users.ts`.
Verified with `pnpm test -- users`.
```

## Examples

Good:

```text
Added server-side validation for the upload size limit and covered it with a regression test. Verified with `pnpm test -- upload`.
```

Poor:

```text
Done. Everything works.
```

## Checklist

Before sending a final response:

- Did I answer the user's latest request?
- Did I mention changed files or artifacts?
- Did I state validation results?
- Did I disclose blockers or uncertainty?
- Did I keep the response no longer than necessary?
