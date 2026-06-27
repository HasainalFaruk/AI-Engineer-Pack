# Security Policy

## Supported content
The AI Engineer Pack is a documentation and workflow repository. Security support applies to the current content in the main repository, including prompts, commands, skills, templates, checklists, examples, GitHub configuration, and project documentation.

## Reporting a vulnerability
Please report security issues privately when they could help someone cause harm, bypass controls, expose secrets, weaken authentication, or encourage unsafe engineering behavior.

Examples include:

- Guidance that recommends insecure authentication, authorization, session, or secrets handling.
- Prompts that encourage exposing credentials, private data, or internal systems.
- Templates that include unsafe default permissions, public data exposure, or weak deployment practices.
- GitHub Actions or repository automation that could expose secrets or grant excessive permissions.
- Security checklists that omit critical controls in a way likely to mislead users.

Use the security reporting channel configured for this repository. If GitHub private vulnerability reporting is enabled, prefer that path. If it is not available, follow the contact guidance in [SUPPORT.md](SUPPORT.md) and avoid posting sensitive exploit details in a public issue.

## What to include
A useful report includes:

- Affected file or folder path.
- Description of the security concern.
- Potential impact.
- Steps, prompt, or example that demonstrates the issue.
- Suggested safer wording or mitigation, if known.

## Public issues for non-sensitive security improvements
Use a public issue when the concern is educational, low risk, and does not expose an exploitable path. For example, requesting stronger wording in `skills/security/` or additional OWASP examples can usually be public.

## Response expectations
Maintainers will triage security reports based on severity, exploitability, and project impact. Accepted reports may result in documentation changes, template updates, checklist improvements, workflow permission changes, or contributor guidance updates.

## Safe contribution practices
When contributing security-related content:

- Prefer least privilege, defense in depth, and secure defaults.
- Avoid publishing real secrets, tokens, private URLs, or customer data.
- Include verification steps and abuse cases where useful.
- Cross-link relevant security skills and checklists.
- Review [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
