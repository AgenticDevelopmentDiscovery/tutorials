---
title: "Tutorial 15 — Sub-Agents & Agent Teams"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 15 — Sub-Agents & Agent Teams

> Student-led tutorial (~15 min). Delegate work to focused helpers without drowning in context.

## What it is
A **sub-agent** is an agent spawned by another agent to handle a scoped piece of work. The parent delegates a well-defined task, the sub-agent runs its own Reason–Act–Observe loop with its *own* context window and (often) its own toolset, and returns just a result — not its entire transcript. This is the implementation substrate beneath the orchestration patterns of Tutorial 14: the spokes of a hub, the stages of a pipeline, and the debaters in a panel are all sub-agents.

The central benefit is **context boundaries**. A sub-agent's exploration — the dozens of files it read, the failed tool calls it made — stays in *its* context; only the distilled conclusion comes back to the parent. This keeps the parent's context clean and focused, which is the single biggest lever on agent reliability over long tasks. Sub-agents can also run with **isolation** (e.g., separate git worktrees) so parallel agents don't clobber each other's files, and they can run **in parallel** to cut wall-clock time on independent subtasks.

## Why it matters for agentic development
Context is the scarce resource in agentic work, and sub-agents are the primary tool for managing it. Delegation lets a coordinator stay strategic while helpers do narrow, token-heavy work. Isolation via worktrees lets you fan out many candidate-exploring agents safely. Scoping — giving each sub-agent only the tools and instructions it needs — both improves focus and limits blast radius. These are exactly the moves you need to make the evolutionary capstone tractable and parallel.

## Key ideas to cover
- Sub-agent = scoped, delegated agent with its own loop and context window.
- **Context boundaries:** the sub-agent absorbs the noisy exploration; only the result returns.
- **Scoping:** restrict tools, instructions, and read/write access per sub-agent.
- **Isolation:** separate worktrees/sandboxes so parallel agents don't collide.
- **Parallelism:** fan out independent subtasks; gather and integrate results.
- Designing the *return contract*: what a sub-agent should hand back (concise, structured).
- Pitfalls: over-delegation, lost context at the boundary, coordination/merge conflicts.

## Hands-on / demo
For the symbolic-regression substrate, have a coordinator spawn N sub-agents in parallel, each in its own worktree, each exploring a different model family (polynomial, trigonometric, exponential) against the eval harness. Each returns only its best formula and score. The coordinator collects the N results, compares them on the leaderboard, and reports the winner — never seeing the messy interior search of any sub-agent. Show how the parent's context stays small even though a lot of work happened.

## Connections
- **Capstone & Spine 1:** parallel sub-agents are how you scale the population of candidate models in the evolutionary loop; each reports a fitness score from the C2 harness.
- **C4 (orchestration & reliability):** sub-agents are the building blocks of the patterns in Tutorial 14.
- **Spine 2 (context engineering):** context boundaries are the most direct, practical form of context engineering in the whole course.
- **C1 (reproducible repo):** worktree isolation keeps parallel work reproducible and merge-safe.

## Further reading
- Your agent host's sub-agent / task-delegation docs (e.g., Claude Code subagents and the Task tool, the Claude Agent SDK).
- Git worktree documentation for the isolation mechanism.
- Writing on "context engineering" and managing agent context windows over long tasks.
