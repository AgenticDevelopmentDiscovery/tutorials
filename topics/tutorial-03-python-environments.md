---
title: "Tutorial 03 — Python Environments & Reproducibility"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 03 — Python Environments & Reproducibility

> Student-led tutorial (~15 min). "Works on my machine" is the enemy of science — environments are how you make an agent run reproducible.

## What it is
A Python environment is an isolated set of installed packages tied to a specific interpreter, so that one project's dependencies can't collide with another's. The classic tool is `venv` (a per-project folder holding its own `python` and `site-packages`); `conda` adds non-Python dependencies and binary management; `uv` is a fast modern resolver/installer that builds environments and lockfiles in seconds. Whatever the tool, the goal is the same: a named, recreatable sandbox you activate before working.

Reproducibility comes from **pinning**. A loose requirement like `numpy` means "whatever is newest today"; a pinned one like `numpy==2.1.3` means exactly that build. A **lockfile** (`uv.lock`, `poetry.lock`, `conda-lock`, or a fully-pinned `requirements.txt`) records the entire resolved dependency tree — every transitive package at an exact version — so anyone, anytime, on any machine can reconstruct the identical environment. Pinning your direct dependencies is good; a lockfile is what actually makes a run repeatable, because it captures the dependencies of your dependencies too.

## Why it matters for agentic development
Agent runs are experiments, and an experiment you can't rerun isn't science. When an agent discovers a model, fits a baseline, or scores against the eval harness, the result is only meaningful if the environment is fixed — a silent version bump in PySR, SciPy, or NumPy can change outputs or break the harness entirely. Pinned environments and lockfiles let you reproduce a leaderboard result, share it with a collaborator, and trust that a regression is a real change in *your* code, not a dependency that drifted underneath you. Reproducibility is also what makes an agent's work auditable: the environment is part of the artifact.

## Key ideas to cover
- Why isolation matters: dependency conflicts, global vs. project installs.
- `venv` basics (create, activate, `pip install`), and where packages actually live.
- `uv` for fast installs and lockfiles; `conda` when you need non-Python/binary deps.
- Pinning vs. lockfiles: direct dependencies vs. the full resolved tree.
- `requirements.txt` / `pyproject.toml` as the human-edited spec; the lockfile as the machine truth.
- Seeding randomness (`PYTHONHASHSEED`, library seeds) as the other half of reproducibility.
- Committing the lockfile so the environment travels with the repo.

## Hands-on / demo
Create a fresh environment for the symbolic-regression substrate two ways and compare: `python -m venv .venv` then `pip install -r requirements.txt`, versus `uv venv` + `uv pip install`. Generate a lockfile, then prove the point — delete the environment, recreate it from the lockfile, and rerun the linear-regression baseline to show byte-identical fitness. Bonus: bump one dependency unpinned and watch a result quietly shift, motivating why the lockfile is committed.

## Connections
- C1 (agentic coding & reproducible repo): the lockfile is a required artifact of the reproducible repo — this tutorial directly equips that challenge.
- C2 / capstone (Spine 1, evaluation→fitness): the eval harness and leaderboard are only comparable across students if everyone's environment is pinned; the fitness function must be deterministic.
- C4 (orchestration & reliability): a generate→evaluate→select loop that reinstalls or drifts mid-run is unreliable; a locked environment is a precondition for trustworthy automation.

## Further reading
- The official Python `venv` documentation and `pip` user guide.
- The `uv` documentation (Astral) for environments, lockfiles, and `uv run`.
- The conda / conda-lock docs for binary-heavy scientific stacks.
- "Twelve-Factor App" §III (Config) and §II (Dependencies) for the reproducibility mindset.
