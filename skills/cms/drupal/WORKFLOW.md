# Drupal Workflow

## 1. Identify the Drupal surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Drupal and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for modules, entities, fields, routes, permissions, configuration export, and content modeling.

## 5. Verify with the right tools
Use cache rebuilds, config import/export checks, permission tests, and module install smoke tests. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Drupal.

