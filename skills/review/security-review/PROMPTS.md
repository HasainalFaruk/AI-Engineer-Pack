# Security Review Prompts

## Build
Use the Security Review skill. Inspect existing project conventions, implement the requested change using idiomatic Security Review patterns, verify with threat model pass, secret scan review, dependency checks, auth tests, and exploit-oriented test cases, and summarize changed files and risks.

## Review
Use the Security Review skill. Review the change for correctness, maintainability, security, performance, and Security Review-specific pitfalls such as checking only dependencies, missing authorization paths, ignoring logs, and treating authentication as complete security. Provide findings by severity.

## Debug
Use the Security Review skill. Reproduce or reason through the issue, inspect relevant files and runtime signals, identify the likely cause, apply a focused fix if requested, and verify with threat model pass, secret scan review, dependency checks, auth tests, and exploit-oriented test cases.

## Document
Use the Security Review skill. Create documentation that explains setup, usage, configuration, limitations, and troubleshooting for this repository's Security Review implementation.

