---
title: "Tutorial 07 — Context Engineering & the Context Window"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 07 — Context Engineering & the Context Window

> Student-led tutorial (~15 min). The model only knows what is in the window right now — context engineering is deciding what that is, and when.

## What it is
A language model has no memory beyond its context window: a finite budget of tokens holding the system prompt, instructions, retrieved documents, prior turns, tool outputs, and your latest message. Everything the model "knows" in the moment is whatever currently occupies that window. Context engineering is the practice of curating that contents — choosing what to include, in what order, at what level of detail, and what to leave out — so the model has exactly the information it needs and not a flood of distraction.

This is the center of Spine 2. Prompting (Tutorial 06) writes the instruction; context engineering builds the environment that instruction runs inside. Two failure modes bound the problem: too little context (the model guesses, hallucinates, repeats work) and too much (relevant signal gets buried, costs rise, and the model fixates on the wrong detail — the "lost in the middle" effect). Good context engineering is information triage under a token budget.

## Why it matters for agentic development
An agent's competence is mostly a function of what is in its window at each step. Repos are large; windows are not. The skill that separates a flailing agent from a sharp one is putting the right file, the right prior result, and the right instruction in front of the model at the right moment — and evicting the rest. Instruction layering (stable system rules → project conventions → task → live data) lets you control precedence so that durable rules survive while transient details cycle through.

## Key ideas to cover
- **The window is finite and shared**: system prompt, history, retrieved docs, tool outputs, and your message all compete for the same budget.
- **Relevance over volume**: more context is not better; precision and ordering matter ("lost in the middle").
- **Instruction layers**: durable system/role rules, then project conventions, then the immediate task, then live data — highest-precedence and most-stable on top.
- **CLAUDE.md as an index**: a project memory file that loads automatically gives the agent a stable map of conventions and pointers without re-explaining each session.
- **Just-in-time context**: pull a file or result into the window when needed, rather than front-loading everything.
- **Context as a budget you spend deliberately**: every token of noise is a token of signal you didn't include.
- **Provenance**: label where context came from so the model can weigh and cite it.

## Hands-on / demo
Demonstrate CLAUDE.md as an index. Start an agent in the course repo with no project file and ask it to add a baseline to the symbolic-regression ladder — watch it guess at conventions (file layout, how the eval harness is invoked). Then add a short CLAUDE.md that names the folder structure, the baseline ladder (linear → PySR → agentic), and how to run the eval, and repeat the same request. The second run is grounded and on-convention. The contrast shows context engineering as the lever, with no change to the underlying prompt.

## Connections
- Spine 2 (context engineering): this tutorial is its center — everything from retrieval to memory is "what goes in the window."
- C1 (reproducible repo): CLAUDE.md and folder conventions are context infrastructure, authored once and reused every session.
- C3 (retrieval/grounding): RAG (Tutorial 09) is automated just-in-time context — retrieval is context engineering at scale.
- Capstone: the evolutionary search reuses domain knowledge as context (constraints, prior expressions) to steer the search space.

## Further reading
- Anthropic documentation on CLAUDE.md / project memory and effective context use.
- The "lost in the middle" study on context-position effects in long contexts.
- Provider docs on context windows and token budgets for current models.
- A project's own `CLAUDE.md` and folder conventions as a worked example of context worth indexing.
