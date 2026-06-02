---
name: corrective-rag
description: RAG workflow with self-evaluation, web search fallback, and context filtering.
---

# Corrective RAG

Use this skill when performing document searches where retrieval accuracy is critical and local databases may have gaps.

## Instructions
1. **Retrieve**: Pull relevant documents from local vector indexes or file caches.
2. **Grade**: Evaluate the retrieved contents for semantic relevance to the query.
3. **Trigger Search**: If relevance is low or partial, execute web searches or scrape documentation pages.
4. **Filter & Compress**: Remove boilerplate HTML, ads, and noise, passing only clean factual context to the generation phase.
