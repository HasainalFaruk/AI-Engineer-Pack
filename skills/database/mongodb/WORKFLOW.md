# MongoDB Workflow

## 1. Identify the MongoDB surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for MongoDB and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for document modeling, indexes, aggregation pipelines, schema validation, and operational query patterns.

## 5. Verify with the right tools
Use index explain plans, aggregation tests, fixture-backed queries, and migration sampling. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to MongoDB.

