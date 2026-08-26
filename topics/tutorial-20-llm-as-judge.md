---
title: "Tutorial 20 — LLM-as-a-Judge & Its Pitfalls"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 20 — LLM-as-a-Judge & Its Pitfalls

> Student-led tutorial (~15 min). Asking a model to grade outputs is seductively easy and quietly dangerous — learn where it helps and where it lies.

## What it is
LLM-as-a-judge is the practice of using a language model to score or rank outputs that have no cheap automatic metric — essay quality, explanation clarity, whether an answer "addresses the question," which of two responses is better. You give the judge model a rubric and an output (or a pair), and it returns a score, a label, or a preference. It's appealing because it scales human-like judgment to thousands of items at near-zero marginal cost, and it can evaluate things a regex or RMSE never could.

The catch is that the judge is itself a fallible, biased model, and its scores are not ground truth — they're another generation. Treated carefully, an LLM judge is a useful soft signal. Treated as an oracle, it becomes a target that the system under evaluation learns to *game*, and a source of systematic error that looks like rigor because it produces precise-seeming numbers.

## Why it matters for agentic development
Much of what agents produce is open-ended, so the temptation to close the loop with an LLM judge is constant — and in an optimization or evolutionary setting, that temptation is a trap. The moment a judge's score becomes a selection target, the generator is incentivized to exploit the judge's biases rather than improve the actual output (Goodhart's law in action). Knowing when to trust a soft LLM judge versus when to demand a hard, gameable-resistant metric is what keeps a generate→evaluate→select loop honest instead of self-deluding. The decision is risk-based: the higher the optimization pressure, the harder the metric you need underneath.

## Key ideas to cover
- When to reach for a judge: open-ended outputs with no cheap ground-truth metric.
- Known biases: position bias (favoring the first/second option), verbosity bias, self-preference (favoring its own style/family), and sycophancy.
- Gaming and Goodhart: once a judge score is optimized against, it stops measuring what you wanted.
- Mitigations: clear rubrics, randomized option order, multiple judges / ensembles, pairwise instead of absolute scoring, and a held-out human-labeled calibration set.
- Trust hierarchy: hard metric > LLM judge backed by human calibration > unchecked LLM judge.
- Use the judge as a filter or tie-breaker, not as the sole fitness function under heavy optimization.
- Always validate the judge against human labels before believing its numbers.

## Hands-on / demo
On a model-discovery task, set up an LLM judge to rate candidate expressions for "interpretability" (something RMSE can't capture). First, demonstrate position bias: swap the order of two candidates and watch the preference flip. Then show gaming: let a generator optimize purely against the judge and watch it produce expressions that *sound* elegant in their description but score worse on held-out RMSE. Finally, fix the setup — randomize order, add the hard RMSE metric as a gate, and use the judge only to break ties among RMSE-equivalent candidates. Contrast the three regimes.

## Connections
- Spine 1 (evaluation→fitness): an LLM judge is a *soft* fitness signal; the eval harness (Tutorial 19) is the *hard* one — the capstone should lean on the latter.
- C4 (orchestration & reliability) and the capstone: under evolutionary selection pressure, a gameable judge corrupts the search — this tutorial is the cautionary counterpart to Tutorials 18–19.
- Tutorial 18 (critics): a critic improves an output; a judge scores it — related roles, different risk profiles when optimized against.
- C2 (research agent): use an LLM judge to triage, but keep the held-out hard metric as the source of truth.

## Further reading
- Papers on LLM-as-a-judge reliability, position/verbosity/self-preference bias (e.g. the MT-Bench / "judging LLM-as-a-judge" line of work).
- Writing on Goodhart's law and reward gaming in optimization against learned metrics.
- Guidance on rubric design, pairwise comparison, and calibrating judges against human labels.
- Anthropic and broader eval documentation on combining model-based and hard-metric scoring.
