# pytest Workflow

## 1. Identify the pytest surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for pytest and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for Python test suites, fixtures, parametrization, plugins, mocking, coverage, and regression tests.

## 5. Verify with the right tools
Use pytest targeted runs, fixture scope review, coverage checks, and failure reproduction. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to pytest.

