# Next.js Workflow

## 1. Identify the Next.js surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Next.js and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for routing, server and client components, data fetching, caching, middleware, API routes, and deployment behavior.

## 5. Verify with the right tools
Use build checks, route smoke tests, server/client boundary checks, metadata validation, and cache behavior tests. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Next.js.

