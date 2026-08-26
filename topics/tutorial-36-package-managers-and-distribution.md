---
title: "Tutorial 36 — Software Distribution: Homebrew, uv & Friends"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 36 — Software Distribution: Homebrew, uv & Friends

> Student-led tutorial (~15 min). Where software comes from, and how to make your rig reproducible.

## What it is
A *package manager* installs software and its dependencies for you. They come in two broad layers. **System package managers** — Homebrew on macOS, `apt`/`dnf` on Linux, Chocolatey/winget on Windows — install OS-level tools and binaries (git, `just`, Pandoc, a LaTeX distribution, compilers). **Language package managers** install libraries and tools *within* an ecosystem: `uv`/`pip` for Python, `cargo` for Rust, `npm` for Node, and so on. They solve overlapping problems at different altitudes, and a working rig usually uses both.

The recurring themes across all of them are *dependency resolution* (find a mutually compatible set of versions), *lockfiles* (record the exact resolved versions so installs are reproducible), and *distribution* (publish your own tool so others can install it by name). `uv` is a fast modern example for Python that resolves, locks, and installs; `cargo` and `npm` show the same pattern with `Cargo.lock` and `package-lock.json`. (Python *environments* specifically get their own tutorial — here we stay at the broader package-manager and distribution landscape.)

## Why it matters for agentic development
"The rig" — the consistent set of tools the course assumes — is itself a reproducible install. If your environment is captured as a list of system packages plus locked language dependencies, an agent or a collaborator can recreate it deterministically, and your capstone experiments run the same on the grader's machine as on yours. Lockfiles are the difference between "I have the code" and "I can reproduce the result." Distribution also matters: when you build a small tool during the course, packaging it (a `pyproject.toml`, a crate, an npm package, or a Homebrew formula) is how it becomes installable rather than a script someone has to copy.

## Key ideas to cover
- Two layers: system managers (Homebrew/apt) vs. language managers (uv/pip, cargo, npm).
- Dependency resolution and *transitive* dependencies — why a resolver is needed.
- Manifest vs. lockfile: declared intent (`pyproject.toml`, `Cargo.toml`) vs. exact resolved versions (lockfile).
- Reproducible installs: commit the lockfile; `--frozen`/`ci` modes install exactly what's pinned.
- Pinning, version ranges, and the cost of unpinned "latest."
- Global tools vs. per-project installs (e.g., `uv tool`, `pipx`, `cargo install`, `npm -g`).
- Distributing your own tool: publish to a registry (PyPI, crates.io, npm) or a Homebrew formula.
- The rig as a reproducible install: one declarative spec rebuilds the whole environment.

## Hands-on / demo
Show two complementary moves. First, the *system* layer: `brew install pandoc just` (the tools from Tutorials 34–35) — note this is what bootstraps the rig. Second, the *language* layer: `uv add` a dependency, then show the generated lockfile and that `uv sync` reproduces the exact versions on a clean checkout. Briefly diff a `Cargo.lock` and a `package-lock.json` so the pattern reads as universal. Close by packaging a trivial command-line tool (a `pyproject.toml` with a script entry point) and installing it with `uv tool install .` — that's the path from "my script" to "an installable tool," and it's how the capstone's experiment harness should ship.

## Connections
- Reproducibility: lockfiles + a captured system-package list make the rig and every result reproducible.
- Capstone: the experiment runs from a locked, installable environment so a grader reproduces it exactly.
- C1 (agentic coding): the agent installs dependencies and reads manifests/lockfiles to understand the rig.
- The course's own build: the build tools (Pandoc, `just`) are installed via these same managers.

## Further reading
- Homebrew documentation and the formula authoring guide.
- `uv` documentation (resolver, lockfile, `uv tool`); contrast with `pip` and `pipx`.
- The Cargo Book and npm docs for lockfile and publishing models.
- Your OS package manager's manual (`apt`, `dnf`, winget) for the system layer.
