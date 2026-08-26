---
title: "Tutorial 29 — Cowork & Codex: Agentic Coding Environments"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 29 — Cowork & Codex: Agentic Coding Environments

> Student-led tutorial (~15 min). What changes when you stop driving the agent keystroke-by-keystroke and start *delegating whole tasks*?

## What it is
Beyond the interactive terminal CLI sits a class of higher-level, often asynchronous agentic environments. Claude *Cowork* and OpenAI *Codex* (the agentic coding product) are two examples: instead of a live back-and-forth where you watch every step, you hand off a described task and the environment works on it — frequently in its own sandbox or branch — then returns a result for you to review. The interaction model shifts from *pairing in real time* toward *delegating and reviewing*, closer to assigning work to a junior collaborator than to autocompleting your own typing.

These environments still rest on the same primitives you've learned — instructions, tools, context, review — but raise the altitude. They tend to manage their own working copy of the project, run longer, and surface their output as a reviewable bundle of changes plus a summary of what was done and why.

## Why it matters for agentic development
Delegation is the scaling move in agentic development: once a task is well-specified, an async environment lets it run while you do something else, and lets several tasks run in parallel. But it raises the stakes on the two skills this course keeps returning to — *clear specification up front* and *disciplined review after*. The agent's autonomy is only as safe as your eval and your reading of the diff. This is exactly where Spine 1 (evaluation as fitness) becomes load-bearing: good async delegation needs a good automatic check.

## Key ideas to cover
- Interactive CLI vs. async/delegated environment: real-time pairing vs. hand-off.
- Sandboxed/branch-based execution: the agent works on its own copy, you merge after.
- Specification quality drives outcome quality — vague task in, vague work out.
- Review as the control point: read the summary AND the diff, don't rubber-stamp.
- Parallelism: multiple delegated tasks at once, supervised rather than driven.
- Tool-plural: Cowork (Claude) and Codex (OpenAI) are examples of one pattern, not the only ones.
- Knowing when to delegate vs. stay interactive: clarity, risk, and reviewability decide.

## Hands-on / demo
Take a well-specified capstone subtask — e.g. "add a complexity penalty to the fitness function and update the eval harness to report it" — and delegate it to an async environment (or simulate the hand-off if access is limited). Show the returned change set and summary, then *review it against the eval*: run the harness, confirm the metric appears and behaves, and accept or send back. The emphasis is the review ritual, not the magic.

## Connections
- C4 (orchestration): delegated environments are orchestration at the task level.
- Spine 1: an automatic eval is what makes unattended delegation trustworthy.
- Capstone: offload candidate-generation or scoring experiments while you analyze results.
- C1 (agentic coding): contrast with the interactive CLI you started on to feel the altitude shift.

## Further reading
- Claude Cowork documentation and overviews of delegated/async agent workflows.
- OpenAI Codex (agentic coding) documentation.
- General writing on autonomy levels in agents and "specify-delegate-review" workflows.
