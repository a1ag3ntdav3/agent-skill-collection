---
name: self-rag
description: Self-Reflective Retrieval-Augmented Generation (Self-RAG) pattern integrating self-critique of retrieved context relevance, output grounding, and utility.
---

# Self-Reflective Retrieval-Augmented Generation (Self-RAG)

Use this skill when accuracy and strict factual grounding are critical, especially in domains like medical, legal, financial, or specific software documentation.

## Instructions
1. **Retrieve Decision**: Analyze the query to determine if external knowledge retrieval is necessary.
2. **Context Evaluation**: Retrieve documents and grade their relevance. Prune irrelevant context.
3. **Grounded Generation**: Generate draft answers and verify that each factual claim is supported by the retrieved context.
4. **Refined Output**: Reject or refine answers that contain unsupported statements or fail to address the core query.
