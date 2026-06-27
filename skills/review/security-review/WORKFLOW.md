# Security Review Workflow

## 1. Identify the Security Review surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for Security Review and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for threats, sensitive data, access control, secrets, dependency risk, input validation, and abuse cases.

## 5. Verify with the right tools
Use threat model pass, secret scan review, dependency checks, auth tests, and exploit-oriented test cases. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to Security Review.

