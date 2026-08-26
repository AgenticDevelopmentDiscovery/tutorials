---
title: "Tutorial 11 — The Agent Loop (ReAct: Reason–Act–Observe)"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 11 — The Agent Loop (ReAct: Reason–Act–Observe)

> Student-led tutorial (~15 min). The single loop that turns a chatbot into an agent.

## What it is
A language model on its own produces text in one shot: prompt in, answer out. An *agent* wraps the model in a loop. At each step the model produces a **thought** (reasoning about what to do next), chooses an **action** (calling a tool with arguments), and then receives an **observation** (the tool's result) back into its context. It reasons again on the enriched context, acts again, and continues until it decides the task is done. This Reason–Act–Observe cycle is the ReAct pattern, and it is the beating heart of essentially every agentic system.

The key shift is that the model no longer has to "know" the answer up front. It can probe the world — run code, query a database, read a file — and let real observations correct its trajectory. Reasoning interleaves with grounding, so errors surface early and get repaired in the next iteration rather than compounding silently inside one long hallucinated response.

## Why it matters for agentic development
The loop is what makes agents *robust to their own ignorance*. A one-shot model guesses; a looping agent checks. For research tasks — fitting a model, debugging a pipeline, searching a space of candidate equations — the agent can try, observe failure (a high residual, a stack trace, a failed test), and adapt. Every reliability technique you will layer on later (retries, verification, multi-step planning) is a refinement of this basic cycle. Master the loop and the rest of the course is variations on a theme.

## Key ideas to cover
- One-shot generation vs. the iterative loop; why interleaving reasoning and action beats either alone.
- The three primitives: **thought** (private reasoning), **action** (a tool call), **observation** (the returned result).
- Grounding: observations come from the real world (tools), so the model's beliefs get corrected by evidence.
- Termination: how the loop knows it's done (a "final answer" action, a stopping condition, a budget).
- Failure modes: loops that never terminate, that thrash, or that ignore observations.
- Context growth: each observation is appended, so the loop is also a context-management problem.
- ReAct vs. plain chain-of-thought: action lets the model *get* information, not just *think* about it.

## Hands-on / demo
Show a tiny agent loop in ~30 lines of Python with one tool: `evaluate_expression(expr, data)` that fits a candidate symbolic-regression formula to a small dataset and returns the error. Give the agent a CSV of (x, y) and ask it to find a formula. Watch it think ("maybe it's linear"), act (`evaluate_expression("a*x+b")`), observe (error = 4.2), revise ("try quadratic"), and converge. Then run the same task as a single prompt with no tool and contrast the guessy, ungrounded answer.

## Connections
- This is the conceptual core of **C2** (build a research agent): the eval harness you build there is exactly the *observation* source the loop reasons against.
- **Spine 1 (evaluation→fitness):** the observation in symbolic regression is a fitness score — the same signal that becomes the evolutionary fitness function in the capstone.
- **C4 (orchestration & reliability):** the generate→evaluate→select loop is a multi-agent generalization of one agent's Reason–Act–Observe cycle.
- **Spine 2 (context engineering):** every observation enlarges the context window, foreshadowing C3's retrieval and memory work.

## Further reading
- The ReAct paper (Yao et al.) — the canonical formulation of reason+act interleaving.
- Documentation for any agent framework's "agentic loop" or "tool-use loop" (e.g., Claude Code, LangGraph) showing the loop concretely.
- The "Reflexion" line of work on agents that observe their own failures and retry.
