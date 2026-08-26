---
title: "Tutorial 14 — Multi-Agent Orchestration Patterns"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 14 — Multi-Agent Orchestration Patterns

> Student-led tutorial (~15 min). When one agent isn't enough, how do you wire several together?

## What it is
A single agent loop (Tutorial 11) takes you far, but some tasks are better served by *multiple* agents with distinct roles, prompts, and tools, coordinated by an orchestration pattern. The common patterns are: **hub-and-spoke**, where a coordinator agent decomposes a task and dispatches subtasks to specialist agents, then integrates results; **pipeline**, where agents are arranged in a sequence and each transforms the output of the previous one (e.g., generate → critique → refine); and **peer-review / debate**, where multiple agents tackle the same problem and a judge (or a vote) selects or merges the best output. These patterns can nest and combine.

The reason multi-agent setups help is mostly about *context* and *specialization*. Each agent gets a focused prompt and a clean, smaller context window, which reduces distraction and error. Roles can be tuned independently — a "generator" agent optimized for creativity, an "evaluator" agent optimized for rigor. The cost is coordination overhead, latency, and new failure modes, so multi-agent is a tool to reach for when a single agent demonstrably saturates.

## Why it matters for agentic development
Orchestration is where the course's evolutionary capstone lives. A generate→evaluate→select loop *is* a multi-agent pattern: proposer agents generate candidate models, an evaluator scores them, and a selector keeps the best. Knowing the standard patterns — and their failure modes — lets you design loops that are reliable, parallelizable, and debuggable instead of a tangle of prompts calling prompts.

## Key ideas to cover
- When multiple agents beat one: specialization, context isolation, parallelism, independent tuning.
- **Hub-and-spoke:** coordinator decomposes, dispatches, and integrates.
- **Pipeline:** staged transformation (generate → critique → refine), each stage a focused agent.
- **Peer-review / debate / ensemble:** multiple solvers + a judge or vote to select.
- The generator–evaluator–selector triad as the canonical research loop.
- Coordination costs: latency, token budget, error propagation, deadlock/looping.
- Choosing a pattern by task shape; combining and nesting patterns.

## Hands-on / demo
Build a three-role mini-pipeline for symbolic regression: a **proposer** agent emits several candidate formulas, an **evaluator** agent (calling the eval harness) scores each on held-out data, and a **selector** agent keeps the top few and asks the proposer to mutate them. Run two or three rounds and show the best error dropping. This is the capstone's evolutionary loop in miniature — make that explicit to the audience.

## Connections
- **C4 (orchestration & reliability):** this tutorial is the conceptual core of C4 and seeds the generate→evaluate→select loop.
- **Capstone & Spine 1:** the evaluator's score *is* the fitness function; the selector *is* evolutionary selection. The whole pattern is the capstone skeleton.
- **C2:** each agent calls the shared eval harness/leaderboard as a tool.
- **Tutorial 15 (sub-agents):** the spokes and stages are typically implemented as scoped sub-agents.

## Further reading
- Multi-agent framework docs (e.g., the Claude Agent SDK's subagents, AutoGen, CrewAI, LangGraph) — compare patterns.
- Papers on LLM debate and multi-agent collaboration for reasoning.
- Literature on the generate-and-test / evolutionary loop in program and equation synthesis.
