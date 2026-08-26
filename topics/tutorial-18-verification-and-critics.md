---
title: "Tutorial 18 — Verification, Critics & Self-Correction"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 18 — Verification, Critics & Self-Correction

> Student-led tutorial (~15 min). A generator that can't check its own work is a slot machine; pair it with a critic and you get a system that improves.

## What it is
Verification is the step where an agent's output is checked against something — a critic model, a consistency test, an adversarial probe, or hard ground truth — before it's accepted. A *critic pass* is a second look (often a second model or a second prompt) that reviews the generator's output for errors, missing requirements, or unjustified claims. *Self-consistency* samples several independent attempts and trusts the answer that agrees with itself across them. *Adversarial verification* deliberately tries to break the output: construct a counterexample, find the failing input, attack the proof. *Ground-truth checks* are the gold standard when available — running the test suite, executing the code, comparing against a known answer.

The unifying idea: separate generation from judgment. The same model that confidently produces a wrong answer can often catch the error when re-tasked as a critic, because critiquing and generating are different operations. Verification is how you convert a fluent guess into a checked result.

## Why it matters for agentic development
Agents amplify both correctness and error at scale — an unverified agent will happily commit subtly wrong code or report a model that overfits. A verification layer is the safety rail. More than that, it's the engine of *improvement*: generate a candidate, critique it, regenerate informed by the critique, and you have a refinement loop. That loop — generate, evaluate, select the better candidate — is exactly the structure C4 builds toward and the capstone scales into evolutionary search. Cheap verification you can run automatically is worth far more than expensive verification you run rarely.

## Key ideas to cover
- Generator vs critic as distinct roles; why a second pass catches what the first missed.
- Critic passes: rubric-based review, requirement checklists, "find the bug in this."
- Self-consistency: majority vote over independent samples; when agreement signals correctness.
- Adversarial verification: counterexample search, fuzzing, red-teaming the output.
- Ground-truth checks: tests, execution, held-out data — always prefer these when you have them.
- The hierarchy of trust: a hard metric beats an LLM critic beats no check (sets up Tutorials 19–20).
- Seeding the loop: critique → revise → re-evaluate is the generate→evaluate→select skeleton.

## Hands-on / demo
On a symbolic-regression task, have the generator propose a candidate expression. Then run three verifiers in sequence: (1) ground truth — evaluate held-out RMSE and reject if it overfits the training split; (2) adversarial — probe the expression at extreme inputs to expose blow-ups or undefined regions; (3) critic — ask a second model "is this expression more complex than the data justify?" Show how each catches a different failure (overfit, instability, needless complexity), and how feeding the critiques back yields a cleaner second candidate.

## Connections
- C4 (orchestration & reliability): this tutorial directly seeds the generate→evaluate→select loop — verification *is* the "evaluate" stage.
- Spine 1 (evaluation→fitness): a critic that scores candidates is a soft fitness function; the eval harness (Tutorial 19) is the hard one.
- Capstone: evolutionary search is generate-and-verify run for many generations; the selection pressure comes from verification.
- C2 (research agent): the eval harness born there is the ground-truth verifier these critics defer to.

## Further reading
- Papers on self-consistency decoding and self-refine / reflexion-style critique loops.
- Anthropic guidance on using a separate critic prompt or model to review agent output.
- Literature on LLM self-correction and its limits (models don't always catch their own errors).
- Property-based testing / fuzzing tools as the adversarial-verification analog from software engineering.
