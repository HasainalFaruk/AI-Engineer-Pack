# Debug Command

## Purpose
The debug command investigates a failure, identifies the root cause, applies a focused fix when requested, and verifies that the issue is resolved without introducing avoidable regressions.

## Inputs
- Error messages, logs, stack traces, screenshots, or failing tests.
- Steps to reproduce or observed behavior.
- Expected behavior and affected environment.
- Relevant source files, configuration, dependencies, and recent changes.

## Outputs
- Root cause analysis or most likely cause with evidence.
- Focused fix when implementation is in scope.
- Regression test or verification step where feasible.
- Summary of commands/checks run and remaining uncertainty.

## Step-by-step workflow
1. Capture the symptom, expected behavior, and reproduction path.
2. Inspect the failing surface and nearby code before changing anything.
3. Reproduce the failure with the smallest reliable command or scenario.
4. Form a hypothesis grounded in observed evidence.
5. Apply the smallest fix that addresses the root cause.
6. Add or update regression coverage when practical.
7. Rerun targeted verification and summarize the cause, fix, and risk.

## Best practices
- Reproduce before fixing whenever possible.
- Change one cause at a time so verification is meaningful.
- Prefer root-cause fixes over masking symptoms.
- Keep logs and command output focused on the failing path.
- Add regression tests for bugs that can reappear.

## Common mistakes
- Guessing from the error message without inspecting code.
- Fixing a symptom while leaving the cause intact.
- Making broad refactors during a bug fix.
- Skipping verification after the change.
- Ignoring environment or configuration differences.

## Example prompt
```text
Use the debug command to fix the failing password reset test. Reproduce the failure, inspect the relevant auth code, apply a focused fix, add regression coverage if needed, and report verification.
```

## Example output
```text
Root cause:
The reset token expiry was parsed as local time while tokens are issued in UTC.

Fix:
Updated token validation to compare timezone-aware UTC timestamps.

Verification:
- Ran tests/auth/test_password_reset.py.
- Added a regression case for expired UTC tokens.
```

## Related skills
- [Debugging](../../skills/debugging/README.md)
- [Testing](../../skills/testing/README.md)
- [Security](../../skills/security/README.md)
- [Languages](../../skills/languages/README.md)

## Related frameworks
- [ReAct](../../frameworks/react/README.md)
- [Least-to-Most](../../frameworks/least-to-most/README.md)
- [Chain of Thought](../../frameworks/chain-of-thought/README.md)
- [Reflection](../../frameworks/reflection/README.md)
