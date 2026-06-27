# Design Command

## Purpose
The design command turns a goal or problem into a technical approach before implementation. It defines requirements, constraints, architecture, tradeoffs, interfaces, risks, and validation criteria.

## Inputs
- Problem statement, user goals, and acceptance criteria.
- Existing architecture, dependencies, APIs, data model, and operational constraints.
- Security, performance, reliability, accessibility, and maintainability requirements.
- Known alternatives, non-goals, and decision deadlines.

## Outputs
- Proposed design with rationale and tradeoffs.
- Interfaces, data flow, component responsibilities, and migration notes.
- Risks, open questions, and validation strategy.
- Implementation plan or decision record when requested.

## Step-by-step workflow
1. Clarify goals, users, constraints, and non-goals.
2. Inspect existing system boundaries and conventions.
3. Identify functional and non-functional requirements.
4. Generate viable approaches when tradeoffs are meaningful.
5. Compare approaches against criteria such as complexity, safety, cost, and maintainability.
6. Recommend a design and define validation steps.
7. Document decisions, risks, rollout, and future extension points.

## Best practices
- Start with requirements before solutions.
- Make tradeoffs explicit.
- Favor designs that fit existing architecture.
- Include failure modes and operational concerns.
- Define how the design will be tested or reviewed.

## Common mistakes
- Jumping to implementation before requirements are clear.
- Ignoring existing system boundaries.
- Optimizing for novelty instead of maintainability.
- Leaving data ownership or error handling undefined.
- Omitting migration and rollback considerations.

## Example prompt
```text
Use the design command to propose a role-based permissions model for this app. Inspect existing auth patterns, compare two approaches, recommend one, and include data model, API impact, tests, and migration risks.
```

## Example output
```text
Recommended design: policy-based permissions layered on existing roles.

Rationale:
- Preserves current role checks.
- Allows fine-grained permissions without rewriting middleware.
- Keeps migration additive.

Validation:
- Unit tests for policy resolution.
- Integration tests for protected routes.
- Manual admin permission smoke test.
```

## Related skills
- [Architecture](../../skills/architecture/README.md)
- [Security](../../skills/security/README.md)
- [Database](../../skills/database/README.md)
- [Testing](../../skills/testing/README.md)

## Related frameworks
- [Tree of Thought](../../frameworks/tree-of-thought/README.md)
- [Plan and Solve](../../frameworks/plan-and-solve/README.md)
- [CO-STAR](../../frameworks/co-star/README.md)
- [Reflection](../../frameworks/reflection/README.md)
