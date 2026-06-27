# OpenAPI Workflow

## 1. Identify the OpenAPI surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for OpenAPI and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for REST API contracts, schemas, examples, error responses, authentication, and generated documentation.

## 5. Verify with the right tools
Use schema validation, example request checks, response contract tests, and generated docs review. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to OpenAPI.

