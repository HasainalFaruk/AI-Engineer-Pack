# RAG Workflow

## 1. Identify the RAG surface
Locate the files, configuration, runtime path, and user flow affected by the request.

## 2. Inspect local conventions
Check existing naming, folder structure, dependency versions, tests, and deployment assumptions before proposing changes.

## 3. Choose a technology-fit approach
Use patterns that are idiomatic for RAG and compatible with the repository rather than introducing unrelated tools.

## 4. Implement or analyze narrowly
Make the smallest useful change, or provide the smallest useful diagnosis, while accounting for retrieval augmented generation, chunking, embeddings, vector stores, citations, reranking, and answer grounding.

## 5. Verify with the right tools
Use retrieval evals, citation checks, chunk inspection, latency tests, and hallucination probes. Record any checks that could not be run.

## 6. Handoff clearly
Summarize changed files or recommendations, important tradeoffs, and remaining risks specific to RAG.

