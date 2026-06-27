# PyTorch Skill Definition

## Capability
Use this skill for neural network training loops, datasets, dataloaders, tensors, GPU usage, checkpoints, and inference code. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with shape tests, small-batch overfit checks, checkpoint load tests, deterministic seeds, and inference smoke tests.

## Best for
- Designing or modifying PyTorch-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on PyTorch tooling or runtime behavior.
- Creating prompts or workflows that require accurate PyTorch terminology.

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
Avoid silent shape bugs, device mismatch, missing eval mode, unstable training loops, and untracked experiment config.

