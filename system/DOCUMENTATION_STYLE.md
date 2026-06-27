# Documentation Style

This document defines how AI engineering agents should write and update documentation.

Use it with [OUTPUT_FORMAT.md](OUTPUT_FORMAT.md), [CODING_STANDARDS.md](CODING_STANDARDS.md), and [VERSIONING.md](VERSIONING.md).

## Goals

Documentation should help readers succeed quickly and safely.

Good documentation is:

- Accurate.
- Current.
- Specific.
- Actionable.
- Easy to scan.
- Honest about limitations.
- Consistent with the product or repository.

## Audience First

Identify the likely reader:

- New contributor.
- Maintainer.
- API consumer.
- Operator.
- Security reviewer.
- End user.
- Future AI coding agent.

Adjust depth, vocabulary, and examples accordingly.

## Structure

Prefer clear headings and short sections.

Common structure:

```text
# Title

Brief purpose.

## When To Use

## Requirements

## Steps

## Examples

## Troubleshooting

## Related Documents
```

Do not add every section if it does not help the reader.

## Style

Use:

- Direct language.
- Active voice.
- Concrete examples.
- Commands that can be copied safely.
- Tables only when comparison helps.
- Checklists for repeatable review.

Avoid:

- Placeholder text.
- Marketing filler.
- Unexplained acronyms.
- Vague claims such as "easy", "simple", or "robust" without evidence.
- Stale screenshots or version-specific claims without context.

## Code Examples

Examples should be:

- Correct.
- Minimal.
- Runnable or clearly illustrative.
- Safe.
- Consistent with project style.

Never include real secrets in examples. Use realistic but fake values such as `example_api_key` only when clearly non-secret.

## Cross-References

Cross-reference related documents when it helps navigation.

Examples:

- Security-sensitive documentation should link to [SECURITY_RULES.md](SECURITY_RULES.md).
- Release process documentation should link to [VERSIONING.md](VERSIONING.md).
- Contributor standards should link to [CODING_STANDARDS.md](CODING_STANDARDS.md) and [QUALITY_STANDARDS.md](QUALITY_STANDARDS.md).

Avoid excessive links that interrupt reading.

## Maintenance

Update documentation when:

- Behavior changes.
- Public APIs change.
- Setup steps change.
- Configuration changes.
- Error handling changes.
- Operational procedures change.
- Security expectations change.

Documentation should be reviewed with the same care as code when it affects production operation.

## Documentation Checklist

- The title states the subject.
- The first paragraph states the purpose.
- Steps are complete and ordered.
- Examples are accurate and safe.
- Cross-links are useful.
- Terminology matches [GLOSSARY.md](GLOSSARY.md) where applicable.
- Version-specific information follows [VERSIONING.md](VERSIONING.md).
