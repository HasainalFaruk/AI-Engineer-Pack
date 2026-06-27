# RAG Skill Definition

## Capability
Use this skill for retrieval augmented generation, chunking, embeddings, vector stores, citations, reranking, and answer grounding. The assistant should inspect local conventions first, choose technology-appropriate patterns, and verify results with retrieval evals, citation checks, chunk inspection, latency tests, and hallucination probes.

## Best for
- Designing or modifying RAG-specific code, configuration, documentation, or tests.
- Reviewing implementation risks and maintainability concerns.
- Debugging failures that depend on RAG tooling or runtime behavior.
- Creating prompts or workflows that require accurate RAG terminology.

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
Avoid poor chunking, stale indexes, missing source attribution, irrelevant top-k retrieval, and no answerability threshold.

