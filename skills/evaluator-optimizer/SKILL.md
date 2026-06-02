---
name: evaluator-optimizer
description: Iterative refinement loop with a generator producing outputs and an evaluator critiquing them.
---

# Evaluator-Optimizer

Use this skill to implement the Evaluator-Optimizer pattern, iterating on a solution through alternating generation and objective critique steps.

## Instructions
1. **Generate**: Produce an initial draft, code snippet, or plan based on the task description.
2. **Evaluate**: Critique the output against explicit quality guidelines, rules, or test suites.
3. **Feedback**: Provide structured, actionable feedback (what failed, why, and how to improve).
4. **Optimize**: Revise the solution using the evaluator's feedback.
5. **Exit**: Exit the loop once all quality standards are met or the maximum iteration threshold is reached.
