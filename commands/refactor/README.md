# Refactor Command

## Purpose
The refactor command improves internal structure without intentionally changing external behavior. It targets readability, maintainability, duplication, boundaries, and testability while preserving existing functionality.

## Inputs
- Refactor goal, affected area, and non-goals.
- Current code, tests, type checks, and behavior expectations.
- Existing architecture conventions and dependency boundaries.
- Risk tolerance and preferred verification scope.

## Outputs
- Focused structural changes that preserve behavior.
- Updated tests only when needed to maintain confidence.
- Documentation updates if structure, extension points, or developer workflow changes.
- Summary of behavior-preservation checks.

## Step-by-step workflow
1. Identify the code smell or maintainability problem to solve.
2. Establish current behavior using tests, snapshots, or documented expectations.
3. Choose a narrow refactor path that avoids unrelated behavior changes.
4. Make small mechanical changes first, then improve names or boundaries.
5. Run targeted tests after each meaningful step when risk is high.
6. Remove dead code only when confidently unused.
7. Summarize the structural improvement and verification evidence.

## Best practices
- Preserve public contracts unless the user explicitly requests a behavior change.
- Keep refactors small enough to review.
- Use existing abstractions before creating new ones.
- Separate behavior changes from structure changes.
- Verify with tests that cover the affected behavior.

## Common mistakes
- Mixing refactor with feature work.
- Renaming or moving too much at once.
- Introducing abstractions without reducing real complexity.
- Deleting code without checking references.
- Assuming tests are unnecessary because behavior should be unchanged.

## Example prompt
```text
Use the refactor command to simplify the invoice calculation module without changing behavior. Inspect current tests, reduce duplication, preserve public interfaces, and run targeted verification.
```

## Example output
```text
Refactored invoice calculation internals.

Changes:
- Extracted shared tax calculation helper.
- Removed duplicated rounding logic from three paths.
- Preserved public function signatures.

Verification:
- Ran invoice unit tests and existing calculation snapshot tests.
```

## Related skills
- [Architecture](../../skills/architecture/README.md)
- [Testing](../../skills/testing/README.md)
- [Review](../../skills/review/README.md)
- [Documentation](../../skills/documentation/README.md)

## Related frameworks
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [Reflection](../../frameworks/reflection/README.md)
- [Self-Refine](../../frameworks/self-refine/README.md)
- [Least-to-Most](../../frameworks/least-to-most/README.md)
