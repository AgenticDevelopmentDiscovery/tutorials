---
title: "Tutorial 26 — Agent Skills"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 26 — Agent Skills

> Student-led tutorial (~15 min). Stop re-explaining the same procedure to your agent every session — package it once as a skill.

## What it is
A *skill* is a packaged, reusable unit of agent capability: a named bundle of instructions (and often a few supporting files or scripts) that an agent can load on demand to perform a specific kind of task well. Claude Code "skills" are one concrete implementation, but the idea is general — a skill captures *how to do something* (the steps, conventions, gotchas, and helper code) so the agent doesn't have to rediscover it each time. You can think of it as a callable procedure for an agent, written mostly in natural language, with optional executable bits.

Crucially, skills are *progressively disclosed*: the agent sees a short description of each available skill, and only pulls the full instructions into context when the task actually calls for it. This keeps the everyday context window lean while making deep, specialized know-how available the moment it's relevant.

## Why it matters for agentic development
Skills are where ad-hoc prompting graduates into reusable engineering. Once you've worked out a reliable procedure — running an eval, formatting a results table, fitting a model — encoding it as a skill means every future session (and every teammate) gets it for free, consistently. This is the difference between a clever one-off chat and a durable capability you can build a course project on.

## Key ideas to cover
- A skill = name + description + body of instructions, optionally bundled scripts/resources.
- Progressive disclosure: only the description is always-on; the body loads when invoked.
- When to build one: a task you repeat, that has a "right way," or that bundles tribal knowledge.
- When NOT to: one-off tasks, or things better handled by a tool/API call.
- Composition: skills can call tools, invoke scripts, and chain with other skills.
- Portability: a skill is mostly text + files, so it travels across projects and people.
- Analogous mechanisms exist in other tools (custom commands, recipes, prompt packs) — the *pattern* is portable even when the format isn't.

## Hands-on / demo
Build a tiny "fit-and-report" skill for the course substrate. Its body: given a dataset of (x, y) pairs, the agent should propose a small set of candidate symbolic forms, fit each, report R² and complexity, and print the best expression. Trigger it twice on different toy datasets to show that the *same* procedure runs without re-prompting. Then show the description-only listing to make progressive disclosure concrete: the full body never enters context until you invoke it.

## Connections
- C1 (agentic coding): your first repeatable workflows are natural skill candidates.
- C2 (research agent / eval harness): wrap the eval harness as a skill so the capstone can call it as a fitness routine — Spine 1 in miniature.
- Spine 2 (context engineering): skills are domain-knowledge-as-context, loaded on demand.
- Capstone: candidate-generation and scoring steps become composable skills.

## Further reading
- Claude Code / Claude Agent documentation on "skills" and progressive disclosure.
- Tool-plural analogues: custom slash commands, "recipes," and reusable prompt libraries in other agent CLIs.
- General writing on capability packaging and the "tools vs. instructions" distinction for agents.
