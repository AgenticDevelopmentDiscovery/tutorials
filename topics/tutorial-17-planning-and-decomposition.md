---
title: "Tutorial 17 — Planning & Task Decomposition for Agents"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 17 — Planning & Task Decomposition for Agents

> Student-led tutorial (~15 min). Sometimes the smartest thing an agent can do is stop and write down the plan before touching anything.

## What it is
Planning is the act of producing an explicit, inspectable sequence of intended steps before (or interleaved with) execution. Decomposition is breaking a large, fuzzy goal into smaller subgoals that are individually checkable. The two go together: a plan is usually a decomposition with an order and dependencies. In agent practice this ranges from lightweight ("think step by step, then act") to structured "plan mode," where the agent drafts a full plan, the human approves or edits it, and only then does the agent execute — turning an opaque autonomous run into a reviewable contract.

Planning trades latency and tokens for reliability and steerability. By committing to a plan up front, the agent exposes its assumptions early (cheap to correct) rather than late (expensive to undo). It also creates natural checkpoints: each subgoal is a place to verify progress, hand off, or abort.

## Why it matters for agentic development
Long-horizon tasks are where unguided agents wander: they fix the wrong thing, gold-plate, or lose the thread halfway. An explicit plan keeps the work on-altitude and gives the human a single high-leverage intervention point. Decomposition also makes verification tractable — you can check each subgoal against a criterion instead of judging one giant diff. And it enables parallelism and delegation: independent subgoals can be farmed out to subagents. But planning is not free or always helpful, and knowing when to skip it is part of the skill.

## Key ideas to cover
- Plan-then-act vs react-as-you-go; the latency/reliability trade-off.
- Plan mode as a human-in-the-loop checkpoint: approve, edit, or reject before any side effects.
- Subgoaling and dependency structure: what must be sequential vs what can run in parallel.
- Decomposition granularity: subgoals small enough to verify, large enough to be worth a step.
- Replanning: detecting when reality diverges from the plan and revising rather than forcing it.
- When planning hurts: trivial tasks, fast-feedback loops, and over-planning that ossifies a bad first guess.
- Plans as artifacts: a written plan is documentation and an audit trail.

## Hands-on / demo
Take the model-discovery capstone problem and run it two ways. First, ask the agent to "find the best symbolic model for this dataset" with no plan — narrate how it jumps straight into fitting. Second, invoke plan mode: the agent proposes a plan (inspect data → establish linear baseline → run PySR → propose agentic refinements → evaluate on held-out split). Edit one step live (insert a feature-engineering pass), approve, and let it execute. Show that the planned run is steerable and its progress legible step by step.

## Connections
- C4 (orchestration & reliability): planning and decomposition are the backbone of orchestrating multi-step, multi-agent workflows.
- Capstone: the evolutionary loop is itself a plan — generate → evaluate → select — and each candidate-generation step can be locally planned.
- Spine 1 (evaluation→fitness): decomposition gives you per-subgoal checkpoints that the eval harness can score.
- C1: plan mode pairs naturally with the reproducible-repo discipline — the plan is committed alongside the work.

## Further reading
- Claude Code's plan mode and the broader pattern of human-approved agent plans (Anthropic docs).
- Papers on ReAct (reasoning + acting) and on "least-to-most" / decomposition prompting.
- Writing on hierarchical task networks and subgoal decomposition in classical planning, for contrast.
- Tree-of-thoughts and plan-search literature for when search over plans pays off.
