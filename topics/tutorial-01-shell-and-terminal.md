---
title: "Tutorial 01 — The Unix Shell & Terminal for Agentic Work"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 01 — The Unix Shell & Terminal for Agentic Work

> Student-led tutorial (~15 min). The shell is the agent's hands — learn it and you learn how every coding agent actually touches your machine.

## What it is
The Unix shell is a text interface to your operating system: you type a command, a program runs, and text comes back. The terminal is the window that hosts that conversation. A small set of primitives does almost everything — navigating the filesystem (`cd`, `ls`, `pwd`), inspecting and moving files (`cat`, `cp`, `mv`, `rm`, `find`), and inspecting running work (`ps`, `kill`, `jobs`). The deeper idea is composition: every program reads from standard input and writes to standard output, and the pipe (`|`) wires one program's output into the next program's input, so `grep`, `sort`, `wc`, and friends combine into ad-hoc data pipelines without any glue code.

Three concepts unlock the rest. **Streams**: stdin, stdout, and stderr are separate channels, which is why you can redirect results to a file (`> out.txt`) while errors still print to the screen. **Exit codes**: every command returns 0 for success or non-zero for failure, which is how scripts and agents decide whether a step worked. **Processes**: commands are programs the kernel schedules, which you can background (`&`), foreground, and signal — the same mechanics a long-running training job or local server relies on.

## Why it matters for agentic development
A coding agent does not have magic access to your computer — it acts by emitting shell commands that a harness executes, then reading the text that comes back. The shell *is* the agent's body. When you understand streams, exit codes, and processes, you can read what an agent is doing, predict what it can and cannot reach, and design tools that are safe to hand it. An agent that runs `pytest` and checks the exit code is doing exactly what you'd do by hand; knowing the substrate lets you debug it when it goes wrong.

## Key ideas to cover
- The filesystem as a tree; absolute vs. relative paths; `cd`, `ls`, `pwd`, `find`.
- stdin/stdout/stderr, redirection (`>`, `>>`, `2>`), and why stderr stays separate.
- Pipes and composition: `grep | sort | uniq -c | sort -rn` as a one-line analysis.
- Exit codes (`$?`) and how agents use them as pass/fail signals.
- Processes, backgrounding (`&`), foreground, and signals (`Ctrl-C`, `kill`).
- Environment variables (`PATH`, `$HOME`) and where commands are found.
- Globbing and quoting — the two things that surprise newcomers most.

## Hands-on / demo
Starting from a folder of CSV experiment outputs, build a pipeline live: `ls *.csv | wc -l` to count runs, then `cat results/*.csv | cut -d, -f3 | sort -n | tail -1` to pull the best fitness score across a sweep. Then show the agentic version — run a one-line model-discovery baseline (`python fit_linear.py data.csv`), inspect its exit code with `echo $?`, and redirect its log with `python fit_linear.py data.csv > run.log 2>&1`. The point lands when you note this is exactly the loop the eval harness will automate.

## Connections
- C1 (agentic coding & reproducible repo): everything the agent does in your repo flows through these commands; you can't reason about reproducibility without them.
- C2 (research agent / eval harness): the harness invokes scripts and reads exit codes and stdout — Spine 1 (evaluation→fitness) is built on this plumbing.
- C4 (orchestration & reliability): backgrounding, signals, and exit codes are how a generate→evaluate→select loop is supervised.

## Further reading
- "The Unix Programming Environment" (Kernighan & Pike) — still the clearest account of composition.
- The GNU coreutils manual and `man` pages for any command (`man find`).
- "Bash Guide" / the Bash reference manual for quoting and globbing rules.
- Your terminal emulator's docs (iTerm2, Windows Terminal, GNOME Terminal) for tabs, splits, and search.
