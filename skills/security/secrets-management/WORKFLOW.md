# Secrets Management Workflow

## 1. Identify the Secrets Management surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Secrets Management and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for secret storage, rotation, environment configuration, vault integration, CI/CD secrets, and leak prevention.

## 5. Verify with the right tools
Use secret scanning, least-privilege access review, rotation runbooks, local env checks, and CI log review. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Secrets Management.

