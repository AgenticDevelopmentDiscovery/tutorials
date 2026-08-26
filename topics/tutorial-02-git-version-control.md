---
title: "Tutorial 02 — Git & Version Control as an Agent Safety Net"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 02 — Git & Version Control as an Agent Safety Net

> Student-led tutorial (~15 min). Commit before you let it loose — Git is the undo button that makes trusting an autonomous agent rational.

## What it is
Git is a distributed version-control system that records snapshots of your project over time. A **commit** is an immutable snapshot plus a message and a parent pointer; the chain of commits is your history. A **branch** is just a movable label pointing at a commit, so creating one is cheap and instant. A **diff** is the line-by-line change between two snapshots — the unit in which you review work. The working directory, the staging area (`git add`), and the commit form a three-stage pipeline: you choose what to stage, then freeze it with `git commit`.

The mental model that matters: history is a graph of snapshots you can move through. `git status` shows what's changed, `git diff` shows the changes themselves, `git log` shows the trail, and `git checkout` / `git restore` / `git revert` / `git reset` let you move back to any prior state. Because every commit is a complete, addressable point, you can always return to known-good ground — which is precisely what makes Git a safety net rather than just a backup.

## Why it matters for agentic development
An agent editing your repository is fast, tireless, and occasionally confidently wrong. The discipline that makes this safe is simple: **commit a clean, working state before you hand the agent a task.** If the run goes sideways — a broken refactor, a deleted file, a plausible-but-wrong rewrite — `git restore` or `git reset --hard` returns you to that checkpoint in seconds. Branches let you run an agent on an isolated copy and merge only if you like the result. Diffs turn "what did the agent change?" from a mystery into a reviewable artifact. Version control converts agent autonomy from a gamble into a bounded, reversible experiment.

## Key ideas to cover
- The three states: working directory → staging (`git add`) → commit.
- Reading history and change: `git status`, `git diff`, `git log --oneline`.
- Branches as cheap labels; `git switch -c`, merging, and why isolation helps.
- Rollback ladder: `git restore`, `git revert` (safe, makes a new commit), `git reset --hard` (destructive).
- "Commit before you let it loose" as a workflow rule, not a chore.
- `.gitignore` for data, secrets, and large artifacts; remotes and `git push`.
- Reviewing an agent's work as a diff before accepting it.

## Hands-on / demo
Initialize a repo around the symbolic-regression starter (`git init`, commit the baseline scripts). Then deliberately let an agent "improve" a fitness function, and show two outcomes from one clean checkpoint: when the change is good, `git diff` reviews it and you commit; when it's bad, `git reset --hard HEAD` wipes it instantly. Finish by branching (`git switch -c try-pysr`) so an experimental PySR baseline lives apart from `main` until it earns its merge.

## Connections
- C1 (agentic coding & reproducible repo): the reproducible repo *is* a Git repo; this tutorial is the backbone of that challenge.
- C2/C4: every agent run in the capstone loop should start from a committed state and end as a reviewable diff — the safety net that lets the generate→evaluate→select loop run unattended.
- Spine 1 (evaluation→fitness): commit the eval harness so leaderboard results are tied to an exact, recoverable code state.

## Further reading
- The official Git documentation and "Pro Git" (Chacon & Straub), freely available online.
- "Oh Shit, Git!?!" for recovering from common mistakes.
- Your platform's docs for pull requests and code review (GitHub, GitLab).
- `git help revert` vs `git help reset` — internalize the difference before you need it.
