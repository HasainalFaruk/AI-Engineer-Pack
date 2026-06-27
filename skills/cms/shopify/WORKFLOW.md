# Shopify Workflow

## 1. Identify the Shopify surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Shopify and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for Liquid themes, app integration, Admin API workflows, metafields, checkout extensions, and storefront behavior.

## 5. Verify with the right tools
Use theme checks, GraphQL query validation, extension preview, test store smoke checks, and webhook verification. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Shopify.

