# scikit-learn Skill Definition

## Capability
Use this skill for classical ML pipelines, preprocessing, feature engineering, model selection, cross-validation, and reproducible training. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with train/test split checks, cross-validation, metric review, pipeline serialization tests, and leakage audits.

## Best for
- Designing or modifying scikit-learn-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on scikit-learn tooling or runtime behavior.
- Creating prompts or workflows that require accurate scikit-learn terminology.

## Inputs
- User goal, acceptance criteria, and affected environment.
- Relevant source files, config files, dependencies, logs, or test output.
- Version constraints and deployment context.
- Security, performance, accessibility, reliability, or maintenance requirements.

## Outputs
- Focused plan, implementation, review, or debugging guidance.
- Technology-specific risks, tradeoffs, and verification steps.
- Updated docs or examples when behavior or usage changes.

## Watch for
Avoid data leakage, fitting preprocessors outside pipelines, weak baselines, metric mismatch, and irreproducible random seeds.

