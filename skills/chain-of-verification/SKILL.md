---
name: chain-of-verification
description: Reduce hallucinations by generating a baseline response, drafting verification questions, answering them independently, and synthesizing a corrected output.
---

# Chain of Verification (CoVe)

Use this skill when generating detailed factual content, historical analyses, lists, or structured summaries where accuracy is paramount.

## Instructions
1. **Baseline Generation**: Generate an initial comprehensive response to the user query.
2. **Verification Planning**: Extract key factual claims and draft a list of neutral, independent questions to verify them.
3. **Verification Execution**: Answer each verification question objectively, utilizing retrieval/search tools if possible, without referencing the baseline response to avoid confirmation bias.
4. **Synthesis & Correction**: Compare the verification answers against the baseline response. Correct any discrepancies and generate the final accurate output.
