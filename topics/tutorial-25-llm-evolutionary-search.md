---
title: "Tutorial 25 — LLM-Driven Evolutionary Search"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 25 — LLM-Driven Evolutionary Search

> Student-led tutorial (~15 min). What if the mutation operator could *read the code* and propose smart edits?

## What it is
LLM-driven evolutionary search keeps the evolutionary skeleton — a population of candidates, a fitness function, selection — but replaces the *random* mutation/crossover operators of classic genetic programming with a language model. Instead of swapping subtrees at random, you prompt the LLM with one or more high-scoring parent candidates (often as code) and ask it to propose an improved variant. The LLM's priors over plausible programs make its "mutations" vastly less random than GP's, so the search can climb toward good solutions in far fewer evaluations.

The loop is **generate → evaluate → select → mutate (repeat)**: the LLM *generates* candidate programs, the fitness function *evaluates* them, selection keeps the best (often in an island/MAP-Elites-style archive that preserves diversity), and those become parents the LLM *mutates* next. FunSearch (Romera-Paredes et al., Nature 2023) introduced this for evolving programs against a scoring function; AlphaEvolve extended it to richer codebases and objectives; OpenEvolve is an open reimplementation you can run. The crucial discipline is fitness design: because the LLM optimizes whatever you measure, a sloppy fitness function invites **eval hacking** — candidates that score well by exploiting the scorer rather than solving the problem.

## Why it matters for agentic development
This is the capstone's core method: it fuses every prior thread — agents that generate, a harness that evaluates, orchestration that runs the loop reliably, and a sandbox that executes generated code safely. It is also the clearest demonstration that *evaluation is everything*: in this paradigm the eval harness literally *is* the selective pressure, so its quality directly determines whether the search discovers science or learns to cheat.

## Key ideas to cover
- The substitution: LLM as a *smart* mutation/crossover operator over programs.
- The loop: generate → evaluate → select → mutate; population and archive management.
- Diversity maintenance: islands, MAP-Elites, novelty — avoiding premature convergence.
- Prompt design for mutation: showing parents, scores, and asking for a targeted improvement.
- Fitness design: what to reward; multi-objective accuracy + parsimony from tutorial 24.
- Eval hacking / reward gaming: candidates exploiting the scorer; held-out checks and guards.
- Compute budget: evaluations are the currency; cost-adjusted search and stopping criteria.

## Hands-on / demo
Run a minimal generate→evaluate→select loop (a small OpenEvolve-style script or hand-rolled) on the shared symbolic-regression task: the LLM proposes candidate equations as code, the **C2** harness scores them on held-out error plus a complexity penalty, the best survive and are fed back as parents. Run ~5 generations live, show the best-fitness curve improving, and then exhibit one "eval-hacking" candidate (e.g., one that special-cases the visible data) to motivate held-out evaluation.

## Connections
- This **is** the capstone method, applied to each student's own research data.
- Spine 1 (evaluation→fitness): the **C2** harness becomes the fitness function — the single most important design choice here.
- Builds directly on GP (tutorial 24), the generate→evaluate→select loop seeded in **C4**, and sandboxed execution of generated code (tutorial 23).
- Spine 2 (context engineering): retrieval/domain knowledge (**C3**) can be injected into mutation prompts to bias the LLM toward physically plausible forms.

## Further reading
- The FunSearch paper (Romera-Paredes et al., Nature 2023).
- AlphaEvolve (DeepMind) write-up on evolving code/algorithms with LLMs.
- The OpenEvolve open-source project as a runnable starting point.
- Literature on reward hacking / specification gaming in optimization and RL.
