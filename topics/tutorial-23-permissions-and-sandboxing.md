---
title: "Tutorial 23 — Permissions, Sandboxing & Safe Autonomy"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 23 — Permissions, Sandboxing & Safe Autonomy

> Student-led tutorial (~15 min). The more autonomous the agent, the more it matters what it *can't* do.

## What it is
An agent that can edit files, run shell commands, and hit the network is powerful — and that same power is the attack surface and the foot-gun. Permissions and sandboxing are the controls that bound an agent's actions. Permission modes govern *whether the agent must ask before acting*: from "prompt me for every command," through allowlists/denylists of specific tools or commands, up to fully autonomous modes. A sandbox governs *what is even reachable*: a restricted filesystem view, a network allowlist, a container or VM, so that even an action the agent decides to take cannot touch what it shouldn't.

The governing principle is least privilege: grant the narrowest capability that lets the task succeed, and make destructive or irreversible actions require explicit confirmation. "Trust and verify" is the operational stance — let the agent move fast inside a safe box, but keep humans in the loop at the boundaries (committing, pushing, deleting, spending money, sending email) and verify outputs rather than assuming them.

## Why it matters for agentic development
Evolutionary and orchestrated agent loops run many steps unattended; you will not watch every one. Safe autonomy is what makes unattended running acceptable: a sandbox lets a candidate-generating loop execute proposed code without risking your machine or secrets, and a denylist stops a runaway loop from racking up cost or clobbering data. Getting this right is the difference between leaving an overnight search running and never daring to.

## Key ideas to cover
- Least privilege: default-deny, grant the minimum capability per task.
- Permission modes: ask-every-time → allow/deny lists → auto-accept; when each is appropriate.
- Sandbox dimensions: filesystem scope, network allowlist, process/container isolation, secret redaction.
- Reversibility: gate irreversible actions (push, delete, spend, send) behind human confirmation.
- Trust-and-verify: fast inside the box, checked at the boundary; verify outputs, don't assume.
- Executing *agent-generated code* safely — the core risk in evolutionary search.
- Failure containment: timeouts, resource limits, kill switches for runaway loops.

## Hands-on / demo
Show the course agent (e.g., Claude CLI) running in a restricted mode: a filesystem scope limited to the project, a network allowlist, and a denylist for destructive commands. Then run a symbolic-regression candidate-evaluation step where the agent executes a *generated* expression in a sandboxed evaluator with a timeout and resource cap — demonstrate a malformed/infinite candidate getting safely killed instead of hanging the host.

## Connections
- Underpins reliable unattended orchestration in **C4** and safe overnight runs in the capstone.
- Sandboxed execution of generated candidates is mandatory for **LLM-driven evolutionary search** (tutorial 25), where the agent proposes code to be run.
- Reinforces **C1** repo hygiene: secrets out of context, reproducible bounded environments.
- Tool-plural relevance: permission/sandbox models differ across Claude (CLI/Cowork), Codex, and Gemini — compare them.

## Further reading
- Claude Code permission modes and settings documentation (allow/deny rules, sandboxing).
- OS-level sandboxing primitives (seccomp, namespaces, containers; macOS sandbox-exec).
- The principle of least privilege (classic security literature, Saltzer & Schroeder).
- Provider docs on tool-use safety and agent guardrails.
