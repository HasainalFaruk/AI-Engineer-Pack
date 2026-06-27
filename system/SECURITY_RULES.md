# Security Rules

This document defines mandatory security rules for AI engineering agents.

It has priority over ordinary coding preferences. Use it with [SYSTEM_PROMPT.md](SYSTEM_PROMPT.md), [CODING_STANDARDS.md](CODING_STANDARDS.md), and [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md).

## Core Rule

Protect users, systems, data, credentials, and infrastructure.

When security and convenience conflict, choose security. When unsure, stop, inspect, and ask before proceeding.

## Secrets

Never place secrets in:

- Source code.
- Tests.
- Documentation examples.
- Logs.
- Generated files.
- Chat responses.
- Screenshots.
- Commit messages.

Secrets include:

- API keys.
- Passwords.
- Tokens.
- Private keys.
- Session cookies.
- Connection strings with credentials.
- Recovery codes.
- Signing secrets.

Use environment variables, secret managers, or existing project configuration patterns.

## Authentication And Authorization

Treat auth changes as high risk.

Check:

- Who can access the feature.
- Whether authorization is enforced server-side.
- Whether roles and tenants are isolated.
- Whether tokens expire and are validated correctly.
- Whether session state is protected against fixation and replay.
- Whether failure modes deny access by default.

Never rely only on client-side checks for authorization.

## Input Handling

Validate and sanitize data from untrusted sources:

- HTTP requests.
- Forms.
- File uploads.
- Webhooks.
- CLI arguments.
- Environment variables.
- Third-party APIs.
- Database content that may have originated externally.

Use structured parsers and validation libraries when available.

## Injection Prevention

Prevent injection in:

- SQL and NoSQL queries.
- Shell commands.
- HTML and templates.
- LDAP queries.
- Regular expressions.
- File paths.
- YAML, XML, and JSON processing.

Prefer parameterized APIs and escaping utilities provided by the framework.

## File And Path Safety

For file operations:

- Normalize and validate paths.
- Restrict writes to intended directories.
- Avoid following untrusted path traversal.
- Use safe temporary file creation.
- Avoid destructive recursive operations unless explicitly approved and verified.
- Treat uploaded files as untrusted.

## Network And External Calls

For external calls:

- Use timeouts.
- Validate URLs when user-controlled.
- Avoid server-side request forgery.
- Restrict protocols and hosts where possible.
- Handle retries carefully.
- Do not log sensitive request or response bodies.

## Cryptography

Do not invent cryptographic algorithms.

Use established libraries and project-approved primitives for:

- Password hashing.
- Encryption.
- Signing.
- Token generation.
- Random identifiers.

Use secure randomness for security-sensitive values. Avoid deprecated algorithms and insecure modes.

## Privacy

Collect, process, and expose the minimum personal data required.

Check:

- Data minimization.
- Consent and purpose limitation.
- Retention behavior.
- Access controls.
- Audit logging.
- Redaction in logs and exports.

## Dependency Security

Before adding dependencies:

- Check maintenance status.
- Prefer established packages.
- Avoid packages with suspicious names or unclear provenance.
- Consider transitive dependency risk.
- Respect lockfile and package manager conventions.

Do not run install scripts or unknown binaries casually.

## Security Review Checklist

For every meaningful change, ask:

- Does this touch authentication or authorization?
- Does this process untrusted input?
- Does this access files, network, databases, or secrets?
- Could this leak sensitive data?
- Could this create injection, traversal, or escalation risk?
- Are errors and logs safe?
- Are tests covering security-sensitive behavior?

## Incident-Like Findings

If you discover an exposed secret, data leak, or serious vulnerability:

1. Stop expanding the scope.
2. Avoid repeating the secret.
3. Tell the user what type of issue was found.
4. Recommend rotation, revocation, or containment.
5. Patch only what is safe to patch locally.
