---
title: "Tutorial 21 — Model Benchmarking & Leaderboards"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 21 — Model Benchmarking & Leaderboards

> Student-led tutorial (~15 min). How do you say one model or agent is "better" without fooling yourself?

## What it is
Model benchmarking is the practice of running two or more models (or agents, or prompt/scaffold configurations) on the *same* task under the *same* conditions and comparing them on a defined metric. A leaderboard is just the ranked, persisted record of those comparisons. The hard part is rarely the running — it is making the comparison *fair*: identical inputs, identical evaluation code, controlled randomness, and a metric that actually reflects what you care about rather than what is easy to measure.

Benchmarking is also where cost enters the picture. A model that scores marginally higher but costs 10x the tokens or wall-clock time may be the wrong choice. Cost-adjusted scoring — score per dollar, score per second, or score at a fixed budget — turns a one-dimensional ranking into an honest trade-off curve. For agents specifically, you must also fix the *scaffold* (tools, retries, context) because a weak model with a good harness routinely beats a strong model with a bad one.

## Why it matters for agentic development
You will constantly face "which model / which prompt / which tool config should I ship?" Without a benchmark you answer by vibes, and vibes do not survive a deadline. A reusable harness that takes a candidate (model + config) and returns a comparable score lets you make these decisions quickly, defensibly, and reproducibly — and that same harness is the seed of your fitness function later.

## Key ideas to cover
- Fix everything but the variable under test: same data split, same eval code, same seeds, same prompt unless prompt *is* the variable.
- Choose a metric that matches the goal; report a distribution (across items/seeds), not a single number.
- Cost-adjusted scoring: score-per-token, score-per-second, or best-score-at-fixed-budget.
- For agents, the scaffold (tools, retries, context window use) is part of what you're benchmarking.
- Contamination and overfitting to the leaderboard: a held-out set the leaderboard never sees.
- Statistical care: variance across runs, paired comparisons, enough items to distinguish signal from noise.
- Persisting results: a leaderboard is data — record candidate id, config hash, metric, cost, timestamp.

## Hands-on / demo
Take the shared symbolic-regression eval harness and run two model backends (e.g., Claude vs. an open-source Hugging Face model) as the "agent" proposing candidate equations for one dataset. Score each on the harness metric (held-out prediction error plus a complexity penalty), record wall-clock and token cost, and produce a tiny two-row leaderboard with a cost-adjusted column. Discuss how the ranking flips when you switch from raw accuracy to accuracy-at-fixed-budget.

## Connections
- Directly extends the **C4** model-benchmarking activity (orchestration & reliability).
- The harness you compare with is the **C2** eval harness — Spine 1 (evaluation→fitness): the same scoring code that ranks models here becomes the fitness function in the capstone.
- Cost-adjusted scoring previews the capstone's compute budget for evolutionary search.
- Reproducible comparison depends on the **C1** repo discipline (pinned configs, seeds).

## Further reading
- The HELM benchmark framework (Stanford CRFM) for multi-metric, cost-aware evaluation.
- The PySR documentation for the baseline symbolic-regression scorer.
- Papers on benchmark contamination and leaderboard overfitting (e.g., the "Lessons from the NeurIPS held-out / Kaggle leaderboard" line of work).
- Anthropic and other provider model cards for per-model cost and capability baselines.
