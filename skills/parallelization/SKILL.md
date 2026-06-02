---
name: parallelization
description: Execute multiple LLM calls concurrently, using either sectioning (independent subtasks) or voting (generating candidates for consensus), then aggregate the results.
---

# Parallelization

Use this skill to implement the Parallelization pattern, running LLM tasks concurrently to reduce latency and improve reliability.

## Instructions
1. **Deconstruct**: Analyze the task to see if it can be split into independent subtasks (Sectioning) or requires consensus/evaluation (Voting).
2. **Fan-Out**: Execute the LLM calls concurrently using asynchronous processes or threads.
3. **Consolidate**: Aggregate the results. For Sectioning, combine the outputs coherently. For Voting, run a consensus algorithm, majority vote, or LLM judge to select the best output.
4. **Handle Failures**: Ensure graceful fallbacks if some parallel calls fail or timeout.
