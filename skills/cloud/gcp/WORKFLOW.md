# Google Cloud Workflow

## 1. Identify the Google Cloud surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Google Cloud and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for Cloud Run, Cloud Functions, IAM, Pub/Sub, Cloud SQL, storage, logging, and project-level governance.

## 5. Verify with the right tools
Use IAM review, deployment smoke tests, service account checks, log-based metrics, and budget alert review. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Google Cloud.

