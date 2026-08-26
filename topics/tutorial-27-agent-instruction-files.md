---
title: "Tutorial 27 — AGENTS.md & CLAUDE.md: Agent Instruction Files"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 27 — AGENTS.md & CLAUDE.md: Agent Instruction Files

> Student-led tutorial (~15 min). The single highest-leverage file in your repo is the one that tells the agent how *your* project works.

## What it is
An *agent instruction file* is a standing, version-controlled document that an agentic tool reads automatically at the start of work in a project. It carries the conventions, commands, and context the agent should always know: how to run the tests, where things live, what style to follow, what to never touch. `CLAUDE.md` is Claude's convention; `AGENTS.md` is an emerging cross-tool standard adopted by several agentic environments. The format is just Markdown — the power is in being persistent and automatic rather than re-typed each session.

These files typically *layer*: a broad file at the repo root sets project-wide defaults, and more specific files deeper in the tree (or a personal/global file) refine or override them for a subdirectory or an individual's preferences. The agent composes the layers it sees, nearest-scope winning, much like cascading configuration.

## Why it matters for agentic development
This is Spine 2 — context engineering — in its most practical form. Instead of re-explaining your project every conversation, you engineer the context once and let the tool inject it. Good instruction files are the difference between an agent that guesses your build command and one that just runs it. They make agentic work reproducible across sessions, teammates, and even across tools, since the same Markdown can be read by multiple agents.

## Key ideas to cover
- Standing instructions vs. per-prompt instructions: persistence is the point.
- `CLAUDE.md` (Claude) and `AGENTS.md` (cross-tool) — same idea, different filenames.
- Layering/cascade: root → subdirectory → personal/global, nearest scope wins.
- What belongs: run/test/build commands, layout, conventions, "do not" rules, domain glossary.
- What does NOT belong: secrets, transient task notes, anything that dates quickly.
- Keep it tight — it's always in context, so every line costs tokens and attention.
- Tool-plural reality: support and exact filenames vary; the *convention* generalizes.

## Hands-on / demo
Live-author an `AGENTS.md`/`CLAUDE.md` for a symbolic-regression project: state the goal, list the "fit / evaluate / report" commands, define complexity and R² as the scoring vocabulary, and add a "do not edit generated results files" rule. Then give the agent a vague request ("improve the model search") and show how it now picks the right commands and metrics without being told — contrast with the same request in a directory that has no instruction file.

## Connections
- Spine 2: the canonical artifact of context engineering as a persisted layer.
- C1 (agentic coding): set up the file early; it pays off every challenge after.
- C3 (retrieval/grounding): instruction files are the "always-on" complement to retrieved context.
- Capstone: encode your domain's invariants so the evolutionary search respects them.

## Further reading
- Claude documentation on `CLAUDE.md` and memory/instruction files.
- The `AGENTS.md` cross-tool convention and its adopting ecosystems.
- General guidance on layered/cascading configuration and "context as a committed artifact."
