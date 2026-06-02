---
name: graph-rag
description: Graph-based Retrieval-Augmented Generation for multi-hop reasoning and relational context retrieval.
---

# GraphRAG

Use this skill when answering queries that span multiple documents, require understanding connections between distant entities, or demand global summarization of a large text corpus.

## Instructions
1. **Analyze Schema**: Inspect the Knowledge Graph schema (entities, node types, relationships).
2. **Determine Query Mode**:
   - **Local Search**: For specific entity questions, query neighbor nodes, descriptions, and related edges within a N-hop distance.
   - **Global Search**: For thematic or overview questions, query pre-computed community summaries at the appropriate hierarchical level.
3. **Traverse and Retrieve**: Fetch path contexts and related metadata from the graph store.
4. **Generate Answer**: Synthesize the final response referencing the extracted entities, relationships, and source texts.
