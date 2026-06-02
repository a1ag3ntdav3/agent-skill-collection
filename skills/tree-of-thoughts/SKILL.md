---
name: tree-of-thoughts
description: Search and evaluate multiple alternative reasoning paths to solve complex, multi-step planning or logic tasks.
---

# Tree of Thoughts

Use this skill when facing complex planning, multi-step math, or logic puzzles where a single wrong initial assumption could break the entire solution.

## Instructions
1. **Decompose**: Split the problem into distinct, logical steps.
2. **Branch**: Generate 3 alternative thoughts/options for the current step.
3. **Evaluate**: Critique each option objectively:
   - Identify pros, cons, and potential failure modes.
   - Rate each as "High", "Medium", or "Low" viability.
4. **Select**: Proceed with the highest-rated option.
5. **Backtrack**: If your current path encounters a roadblock or contradiction, state the error, return to the previous branch point, and proceed with the next best option.
