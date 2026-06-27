# Test Command

## Purpose
The test command designs, adds, runs, or improves verification for software behavior. It focuses on confidence, regression prevention, and clear evidence that requirements are met.

## Inputs
- Behavior or change to verify.
- Existing test framework, fixtures, test data, and conventions.
- Risk areas, acceptance criteria, and edge cases.
- Desired scope: unit, integration, end-to-end, performance, security, or manual checks.

## Outputs
- New or updated tests when implementation is requested.
- Test plan or coverage analysis when planning is requested.
- Test execution results and interpretation.
- Documented gaps or risks that remain untested.

## Step-by-step workflow
1. Identify the behavior, risk, and acceptance criteria.
2. Inspect existing tests to match style, fixtures, and naming.
3. Choose the cheapest test level that gives reliable confidence.
4. Add focused tests for normal paths, edge cases, and known regressions.
5. Run targeted tests and fix failures caused by the change.
6. Broaden to related suites if shared behavior is affected.
7. Summarize coverage, results, and remaining gaps.

## Best practices
- Test behavior rather than implementation details.
- Keep tests deterministic and independent.
- Use clear names that describe the scenario and expected result.
- Add regression tests for fixed bugs.
- Prefer targeted tests first, then broader suites when needed.

## Common mistakes
- Adding brittle tests tied to private implementation.
- Covering only the happy path.
- Ignoring fixtures and local test conventions.
- Treating a passing narrow test as proof of all related behavior.
- Leaving failing or skipped tests unexplained.

## Example prompt
```text
Use the test command to add regression coverage for expired reset tokens. Follow existing auth test patterns, include edge cases, run the targeted test file, and summarize remaining gaps.
```

## Example output
```text
Added regression tests for reset token expiry.

Coverage:
- Valid token within expiry window.
- Expired token rejected.
- Timezone-aware UTC comparison.

Verification:
- Ran tests/auth/test_password_reset.py successfully.
```

## Related skills
- [Testing](../../skills/testing/README.md)
- [Debugging](../../skills/debugging/README.md)
- [Security](../../skills/security/README.md)
- [Review](../../skills/review/README.md)

## Related frameworks
- [Least-to-Most](../../frameworks/least-to-most/README.md)
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [Reflection](../../frameworks/reflection/README.md)
- [ReAct](../../frameworks/react/README.md)
