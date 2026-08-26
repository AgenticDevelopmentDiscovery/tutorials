---
title: "Tutorial 19 — Building Evaluation Harnesses for Agents"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 19 — Building Evaluation Harnesses for Agents

> Student-led tutorial (~15 min). The harness you build here is the same object that becomes your fitness function in the capstone — build it like it matters, because it does.

## What it is
An evaluation harness is the machinery that takes an agent (or a candidate solution it produced) and returns a number — or a small set of numbers — saying how good it is, automatically and repeatably. Its parts are standard: a set of *held-out tasks* the agent hasn't seen, *metrics* that capture what "good" means, an *automatic scorer* that computes those metrics without a human in the loop, and a *runner* that executes everything and logs results. Good harnesses also support *ablations* — toggling one component (retrieval on/off, a tool removed, a prompt changed) to attribute performance to causes rather than guessing.

The discipline is borrowed from ML evaluation but sharpened for agents: because agents are stochastic and multi-step, the harness must handle variance (multiple seeds), partial credit (per-subtask scoring), and the ever-present risk of leakage between what you tune on and what you test on. A harness is trustworthy only to the degree its held-out set is genuinely held out.

## Why it matters for agentic development
You cannot improve what you cannot measure, and with agents you especially cannot trust your own impression — a run that *feels* better may just be a lucky sample. A harness converts vibes into a comparable scalar, which lets you iterate honestly: change something, re-run, see if the number moved beyond noise. This is the load-bearing skill of the whole course. The harness you build in Challenge 2 is not a throwaway grading script — it is reused, generalized, and ultimately promoted into the *fitness function* that drives selection in the evolutionary capstone. Treat it as core infrastructure.

## Key ideas to cover
- Held-out tasks and leakage: keep a test split the agent never sees during development.
- Metrics that match intent: accuracy is rarely enough; combine error, complexity, robustness, cost.
- Automatic scoring: a function from (output, ground truth) → score, with no human in the loop.
- Variance and seeds: run multiple times; report mean and spread, not a single lucky run.
- Ablations: change one factor at a time to learn *why* performance changed.
- A shared leaderboard: same tasks, same scorer, comparable numbers across students/methods.
- Designing for reuse: the same interface that grades an agent can score a candidate model in a search.

## Hands-on / demo
Build a minimal harness for symbolic model discovery. Define a held-out dataset split and a scorer that returns held-out RMSE *plus* an expression-complexity penalty (so a giant overfit formula scores worse than a clean one). Run the baseline ladder through it — linear regression, then PySR, then an agentic candidate — and post all three to the shared leaderboard. Then show the punchline: wrap the same scorer as `fitness(candidate) -> float` and demonstrate it slotting unchanged into a selection loop. The grader and the fitness function are literally the same code.

## Connections
- C2 (research agent): this is where the harness is *born* — the central artifact of Challenge 2.
- Spine 1 (evaluation→fitness): this tutorial is the center of Spine 1; the harness here *becomes* the capstone's fitness function with no rewrite.
- Capstone: evolutionary symbolic regression selects on exactly this score — your harness is the selection pressure.
- C1 (reproducible repo) and C4 (reliability): a harness is only as good as its reproducibility — fixed seeds, pinned data, logged runs.

## Further reading
- Frameworks for LLM/agent evaluation (e.g. OpenAI Evals, lm-evaluation-harness) for harness structure.
- PySR / symbolic-regression documentation for built-in accuracy-vs-complexity scoring.
- ML methodology references on train/validation/test splits and data leakage.
- Writing on held-out benchmarks, contamination, and why "evaluate on what you tuned" lies to you.
