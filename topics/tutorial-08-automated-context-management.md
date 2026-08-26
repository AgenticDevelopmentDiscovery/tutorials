---
title: "Tutorial 08 — Automated Context Management"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 08 — Automated Context Management

> Student-led tutorial (~15 min). When the window fills, something has to give — compaction, memory, and knowing when to clear vs. continue keep long sessions coherent.

## What it is
Long agent sessions generate more tokens than any window can hold: turns of dialogue, tool outputs, file dumps, intermediate reasoning. Automated context management is the set of mechanisms that keep a session running past that limit without losing the plot. The core moves are **compaction/summarization** (replace a long history with a faithful shorter summary), **session boundaries** (when to start fresh), and **memory** (persist durable facts outside the window so they can be reloaded later).

The key insight is that not all context is equal. Some is transient (a stack trace you already fixed), some is durable (the task goal, key decisions, the file you're editing). Good management compresses or evicts the transient while preserving the durable. Done well, the agent feels like it remembers; done poorly, it forgets the goal or "remembers" a hallucinated summary.

## Why it matters for agentic development
Agents that do real work — multi-file refactors, long research loops, an evolutionary search over many generations — outlive a single window many times over. Without automated management they degrade: they re-read files they already saw, drop earlier constraints, or stall. The decision of *when to clear vs. continue* is an operational skill: continue when accumulated state is load-bearing, clear when history is mostly noise that's crowding out the real task. Memory turns one-shot agents into ones that improve across sessions.

## Key ideas to cover
- **Compaction/summarization**: collapse old turns into a compact, faithful summary; preserve goals and decisions, drop resolved detail.
- **Lossy by nature**: summarization can drop or distort — verify that critical facts survive the squeeze.
- **Sessions as units**: a fresh session is the cheapest, most reliable reset; scope work to fit.
- **Memory vs. context**: memory is durable storage *outside* the window (files, notes, a memory tool) that you reload deliberately; context is what's loaded *now*.
- **Clear vs. continue**: continue when prior state is essential; clear when the window is mostly stale and the goal can be restated cleanly.
- **Externalize state**: write decisions and results to files (the repo, a scratch log) so they survive any reset.
- **Cost and latency**: a bloated window is slower and pricier — management is an efficiency lever too.

## Hands-on / demo
Run a multi-generation symbolic-regression loop in one long session and let the window fill with per-generation logs. Show the agent starting to lose track of the best-so-far expression. Then introduce two fixes: (1) externalize state — have each generation append its best expression and score to a leaderboard file in the repo; (2) compact — summarize the run history into "best expression, best score, what's been tried." Restart from the summary plus the leaderboard file and show the agent resumes coherently. This previews the capstone's generate→evaluate→select loop running longer than any single window.

## Connections
- C4 (orchestration & reliability): managing context across a long loop is part of making agents reliable, not just clever.
- Capstone: the evolutionary search runs many generations — externalized state (leaderboard) and compaction are what let it persist.
- Spine 1 (evaluation→fitness): scores written to the leaderboard are durable memory; the eval harness output is exactly the state worth persisting.
- Spine 2 (context engineering): automated management is context engineering over time — the dynamic counterpart to Tutorial 07's static curation.

## Further reading
- Anthropic docs on compaction, memory tooling, and managing long agent sessions.
- Provider guidance on conversation summarization and session strategies.
- Literature on agent memory architectures (short-term window vs. long-term store).
- Course substrate: the shared eval-harness/leaderboard as a worked example of externalized state.
