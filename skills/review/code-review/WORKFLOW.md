# Code Review Workflow

## 1. Identify the Code Review surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Code Review and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for source changes, behavior risk, maintainability, test coverage, security implications, and actionable feedback.

## 5. Verify with the right tools
Use diff inspection, requirement comparison, targeted test review, and severity-ranked findings. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Code Review.

