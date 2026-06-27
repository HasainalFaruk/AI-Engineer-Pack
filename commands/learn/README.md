# Learn Command

## Purpose
The learn command helps a user understand a concept, codebase, tool, domain, or workflow. It focuses on accurate explanation, progressive teaching, practical examples, and clear next steps.

## Inputs
- Topic, learning goal, and current skill level.
- Relevant files, documentation, examples, or source material.
- Preferred depth, format, and time constraints.
- Desired outcome, such as being able to modify code, use an API, or explain a design.

## Outputs
- Explanation tailored to the learner and goal.
- Concept map, walkthrough, examples, or exercises.
- Code references or documentation links when relevant.
- Suggested next steps or practice tasks.

## Step-by-step workflow
1. Identify what the user wants to be able to do after learning.
2. Assess existing context and avoid assuming too much background.
3. Break the topic into prerequisite ideas and practical applications.
4. Explain with examples from the repository or realistic scenarios.
5. Call out common misunderstandings and decision points.
6. Provide a short practice task or next reading path when useful.
7. Summarize the core mental model in plain language.

## Best practices
- Teach toward a concrete capability, not encyclopedic coverage.
- Use examples close to the user's project or role.
- Define terms before relying on them.
- Progress from simple to complex.
- Include checks for understanding when the topic is difficult.

## Common mistakes
- Giving a generic tutorial unrelated to the user goal.
- Overloading the user with advanced details too early.
- Skipping examples.
- Explaining APIs without showing how they are used in context.
- Hiding uncertainty when documentation or code is ambiguous.

## Example prompt
```text
Use the learn command to explain how this repository handles authentication. Start with the high-level flow, then walk through the key files, common extension points, and one safe practice exercise.
```

## Example output
```text
Authentication mental model:
Requests enter through middleware, credentials are validated by the auth service, and user permissions are attached to the request context.

Key files:
- app/auth/service.py: credential validation.
- app/auth/middleware.py: request integration.
- tests/auth/: expected behavior examples.

Practice:
Trace how an expired token is rejected and identify where a test would belong.
```

## Related skills
- [Documentation](../../skills/documentation/README.md)
- [Languages](../../skills/languages/README.md)
- [Architecture](../../skills/architecture/README.md)
- [Debugging](../../skills/debugging/README.md)

## Related frameworks
- [Least-to-Most](../../frameworks/least-to-most/README.md)
- [Skeleton of Thought](../../frameworks/skeleton-of-thought/README.md)
- [CO-STAR](../../frameworks/co-star/README.md)
- [Chain of Thought](../../frameworks/chain-of-thought/README.md)
