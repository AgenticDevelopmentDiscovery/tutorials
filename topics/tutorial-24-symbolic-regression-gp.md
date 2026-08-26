---
title: "Tutorial 24 — Symbolic Regression & Genetic Programming"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 24 — Symbolic Regression & Genetic Programming

> Student-led tutorial (~15 min). Don't fit parameters to a fixed equation — discover the equation itself.

## What it is
Symbolic regression (SR) searches over the space of *mathematical expressions* to find a formula that fits data, instead of fitting coefficients of a pre-chosen model. The output is a human-readable equation — `y = a·sin(x) + b·x²` — not just weights. This makes SR attractive for scientific model discovery: the result is interpretable and can expose mechanism, not merely predict.

The classic engine is genetic programming (GP), an evolutionary algorithm whose individuals are *expression trees* (operators as internal nodes, variables/constants as leaves). GP maintains a population, scores each tree by a fitness function (typically prediction error), and breeds the next generation via selection, **crossover** (swap subtrees between two parents), and **mutation** (perturb a node, subtree, or constant). Because pure accuracy rewards ever-larger trees that memorize noise, SR is fundamentally a multi-objective problem: trade off accuracy against **parsimony** (expression complexity). Tools like PySR expose this as a Pareto front, letting you pick the simplest equation that is "accurate enough."

## Why it matters for agentic development
SR is the course's substrate and the capstone's task. Understanding GP as evolution-over-programs is exactly the mental model you need before swapping GP's random mutation operator for an LLM. The accuracy/parsimony trade-off is also where *fitness design* lives — and a well-designed fitness function is what keeps any evolutionary or agentic search honest rather than gaming the metric.

## Key ideas to cover
- Expression trees as the genotype; operators, variables, constants as nodes.
- The GP loop: population → fitness → selection → crossover → mutation → repeat.
- Crossover (subtree swap) vs. mutation (node/subtree/constant change).
- Fitness = fit error; why raw error alone overfits and bloats trees.
- Parsimony pressure and the accuracy–complexity Pareto front.
- Constant optimization inside a tree (e.g., nonlinear least squares on the leaves).
- Strengths/limits: interpretability vs. combinatorial search cost; baseline ladder linear → PySR.

## Hands-on / demo
Run PySR on a shared dataset (e.g., a noisy `v = sqrt(2·g·h)` or a Feynman-style equation) and walk through the resulting Pareto front: show several candidate equations of increasing complexity and decreasing error, and discuss which one you'd publish. Contrast with a plain linear-regression baseline on the same data to make the "discover the form, not just the coefficients" point concrete.

## Connections
- The direct precursor to the **capstone**: GP is the evolutionary skeleton the LLM-driven method replaces piece by piece.
- Spine 1 (evaluation→fitness): the SR fitness function *is* the **C2** eval harness — accuracy plus parsimony.
- Establishes the baseline ladder (linear → **PySR** → agentic/evolutionary) against which the capstone is measured.
- Feeds the shared leaderboard used in **C4** benchmarking (tutorial 21).

## Further reading
- The PySR documentation and the Cranmer (2023) paper on PySR/SymbolicRegression.jl.
- Koza's foundational work on Genetic Programming.
- The SRBench / Feynman symbolic-regression benchmark suite.
- Reviews on parsimony, Pareto fronts, and model selection in symbolic regression.
