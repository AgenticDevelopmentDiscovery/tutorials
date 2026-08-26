---
title: "Tutorial 28 — VS Code as an Agentic IDE"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 28 — VS Code as an Agentic IDE

> Student-led tutorial (~15 min). The terminal is great until you need to *see* a fifteen-file diff — that's when the editor earns its keep.

## What it is
VS Code is a widely used code editor that, through agent extensions, becomes a place where an AI agent edits your project *inside the editor you're already reading*. Rather than a pure chat or a bare command-line loop, an agentic IDE shows proposed changes as inline diffs you can review, accept, or reject hunk by hunk, with full syntax highlighting, file navigation, and the rest of the editor's machinery alongside. Several agents plug into VS Code (Claude's extension, others), so the editor is a tool-plural host rather than a single vendor's surface.

The core shift is that the agent and the human share one workspace. The agent proposes; you see exactly what would change, where, and in context; you keep or discard it. The edit loop — read, change, review, run — stays inside one window instead of being split across a chat tab and a terminal.

## Why it matters for agentic development
For students starting from zero tooling, the GUI lowers the cost of *review*, which is the skill that actually keeps agentic work safe and honest. Seeing a colored diff and approving it deliberately builds the habit of reading what the agent did rather than trusting it blindly. As projects grow past a couple of files, visual diffing and in-editor navigation scale far better than scrolling terminal output.

## Key ideas to cover
- Editor + agent extension: the agent works *in* your workspace, not beside it.
- Inline diffs and hunk-level accept/reject as the primary review surface.
- The tight edit loop: propose → review → run/test → iterate, all in one window.
- When a GUI beats the bare CLI: large multi-file changes, careful review, visual debugging.
- When the CLI still wins: automation, scripting, headless/remote, reproducible pipelines.
- Tool-plural: multiple agents target VS Code; the IDE is the neutral host.
- Integration with terminals, source control views, and notebooks for quantitative work.

## Hands-on / demo
Open a small symbolic-regression script in VS Code and ask the in-editor agent to refactor the candidate-generation function and add a results table. Walk through the inline diff: accept the refactor hunk, reject an unwanted change to the plotting code, then run the script in the integrated terminal to confirm. The point is to demonstrate *selective acceptance* — something awkward in a pure chat transcript.

## Connections
- C1 (agentic coding): a natural home base for the first hands-on challenge.
- C4 (orchestration): the editor as the cockpit where you supervise agent-driven changes.
- Spine 1 (eval becomes fitness): run and eyeball eval outputs right beside the code.
- Capstone: review generations of candidate models with real diffs, not blind trust.

## Further reading
- VS Code documentation and its extension marketplace.
- Claude's VS Code extension docs and other agent extensions for the editor.
- General writing comparing IDE-based vs. CLI-based agentic workflows.
