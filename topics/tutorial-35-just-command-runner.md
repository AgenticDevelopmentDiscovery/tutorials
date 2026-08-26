---
title: "Tutorial 35 — Just: A Command Runner"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 35 — Just: A Command Runner

> Student-led tutorial (~15 min). Turn "the long command someone remembers" into `just run`.

## What it is
`just` is a command runner: you write named *recipes* in a `justfile`, and run them by name. A recipe bundles the real shell commands for a task — building the PDF, running the agent, executing tests, cleaning artifacts — behind a short, memorable verb. Instead of pasting a 200-character Pandoc invocation from someone's notes, a collaborator (or an agent) runs `just build` and gets the exact, blessed command every time.

Crucially, `just` is *not* a build system. Make exists to track file dependencies and rebuild only what changed, and its syntax carries decades of arcana — tab-sensitivity, implicit rules, `$$` escaping, `.PHONY` targets. `just` deliberately drops the dependency-graph machinery and keeps the good part: a clean, discoverable interface to a project's actions. Recipes take parameters, load `.env` files, set variables, and can be written in any language via a shebang line.

## Why it matters for agentic development
A `justfile` is a machine- and human-readable contract for "what can you do in this repo." An agent doesn't have to guess your build incantation or invent flags — it reads the recipes and calls `just <recipe>`. That makes agent actions reproducible and reviewable, and it standardizes the repo's surface so every project in the course exposes the same verbs (`just run`, `just build`, `just test`). Less tribal knowledge, fewer "works on my machine" failures.

## Key ideas to cover
- A `justfile` is a list of recipes; `just` (no args) or `just --list` shows them.
- Recipes wrap shell commands behind a name; the first recipe is often the default.
- Parameters: `just deploy staging` passes arguments into a recipe.
- Variables, `.env` loading, and `set` options (e.g., shell selection, `dotenv-load`).
- Shebang recipes let a recipe be a Python/Node script, not just shell lines.
- Contrast with Make: `just` does *no* dependency tracking — it's a runner, not a builder.
- Cross-platform friendliness and consistent quoting/escaping vs. Make's footguns.
- The "standard interface" idea: same verbs across every repo lower onboarding cost.

## Hands-on / demo
Write a four-recipe `justfile`: `build` (calls the Pandoc command from Tutorial 34), `run` (invokes the agent / search), `test`, and `clean`. Run `just --list` to show the self-documenting menu, then `just build` to produce the report PDF with one word. Add a parameterized recipe like `paper format="pdf"` and run `just paper docx`. Point out that the rig setup (Tutorial 36) installs `just`, and the capstone repo ships a `justfile` so a grader can reproduce every result with `just build` — no README archaeology.

## Connections
- C1 (agentic coding): the agent reads the `justfile` to learn and run the project's actions.
- C4 (orchestration): multi-step pipelines get named recipes the orchestrator can call.
- Capstone: ship a `justfile` so the entire paper + experiment reproduces with one command.
- Reproducibility / the course build: standard verbs (`just build`) make every repo build the same way.

## Further reading
- The `just` Programmer's Manual / official documentation and README.
- GNU Make manual — useful for understanding the dependency-tracking model `just` omits.
- "Task runner vs. build system" discussions; compare with `task` (Taskfile) and `npm` scripts.
