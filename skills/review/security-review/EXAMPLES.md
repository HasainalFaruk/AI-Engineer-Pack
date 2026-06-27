# Security Review Examples

## Implementation example
Request: Use the Security Review skill to add a small feature in the current repository, follow existing conventions, and verify with threat model pass, secret scan review, dependency checks, auth tests, and exploit-oriented test cases.

Expected output: A focused implementation summary, changed files, verification results, and notes about Security Review-specific risks.

## Review example
Request: Use the Security Review skill to review a pull request for correctness and risks.

Expected output: Severity-ranked findings that call out issues such as checking only dependencies, missing authorization paths, ignoring logs, and treating authentication as complete security.

## Debugging example
Request: Use the Security Review skill to investigate a failure involving threats, sensitive data, access control, secrets, dependency risk, input validation, and abuse cases.

Expected output: Root cause, focused fix or recommendation, verification evidence, and remaining uncertainty.

