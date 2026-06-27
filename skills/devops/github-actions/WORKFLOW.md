# GitHub Actions Workflow

## 1. Identify the GitHub Actions surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for GitHub Actions and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for CI workflows, job permissions, caching, matrices, artifacts, environments, and release automation.

## 5. Verify with the right tools
Use workflow syntax checks, least-privilege permissions, cache key review, branch trigger checks, and dry-run reasoning. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to GitHub Actions.

