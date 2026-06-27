# Build Command

## Purpose
The build command turns a requested feature, service, integration, or artifact into a working implementation. It emphasizes repository inspection, incremental construction, verification, and a clear handoff.

## Inputs
- User goal and acceptance criteria.
- Relevant repository files, dependencies, configuration, and existing patterns.
- Runtime, deployment, security, and compatibility constraints.
- Expected verification method, such as tests, local run, or manual checks.

## Outputs
- Implemented code or generated artifact inside the current repository.
- Updated documentation when setup, behavior, or usage changes.
- Tests, examples, or verification notes that prove the build works.
- Final summary of changed files, checks run, and residual risks.

## Step-by-step workflow
1. Confirm the target outcome, non-goals, and definition of done.
2. Inspect existing architecture, naming, dependencies, and nearby implementations.
3. Choose the smallest design that satisfies the requirement and fits the codebase.
4. Implement the core path first, then add validation, error handling, and edge cases.
5. Add or update tests, examples, and documentation.
6. Run targeted verification first, then broader checks if the change affects shared behavior.
7. Summarize what was built, how it was verified, and what remains risky or optional.

## Best practices
- Follow existing project conventions before introducing new abstractions.
- Keep the first working version small and complete.
- Prefer explicit acceptance criteria over broad feature interpretation.
- Update documentation when users or maintainers need new instructions.
- Verify behavior with the narrowest reliable check before running expensive suites.

## Common mistakes
- Building a larger feature than requested.
- Adding new dependencies when existing tools are sufficient.
- Skipping error handling, validation, or tests.
- Treating generated code as complete without running it.
- Forgetting documentation for new setup or usage behavior.

## Example prompt
```text
Use the build command to add CSV export for the admin users table. Inspect existing admin patterns first, implement the smallest working endpoint and UI action, add tests, update documentation if needed, and summarize verification.
```

## Example output
```text
Built CSV export for the admin users table.

Changed files:
- app/admin/users/export.py
- app/admin/users/routes.py
- tests/admin/test_user_export.py

Verification:
- Ran targeted export tests.
- Manually checked generated headers and escaping behavior.

Notes:
- Export uses existing admin authorization middleware.
```

## Related skills
- [Architecture](../../skills/architecture/README.md)
- [Testing](../../skills/testing/README.md)
- [Security](../../skills/security/README.md)
- [Documentation](../../skills/documentation/README.md)

## Related frameworks
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [ReAct](../../frameworks/react/README.md)
- [Least-to-Most](../../frameworks/least-to-most/README.md)
- [Self-Refine](../../frameworks/self-refine/README.md)
