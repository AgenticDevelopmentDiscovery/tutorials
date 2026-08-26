---
title: "Tutorial 06 — Prompt Engineering Patterns"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 06 — Prompt Engineering Patterns

> Student-led tutorial (~15 min). A handful of reusable patterns turn a vague request into a reliable instruction the model can actually execute.

## What it is
Prompt engineering is the craft of writing the natural-language instruction that steers a model toward a useful, repeatable output. It is not a bag of magic phrases; it is the discipline of being precise about the task, the inputs, the constraints, and the shape of the answer. A good prompt reads less like a chat message and more like a small specification: it says what to do, shows what "good" looks like, and bounds what to ignore.

For a quantitative audience, the useful mental model is that the prompt is the program and the model is a noisy interpreter. Ambiguity is the enemy. The patterns below — specificity, few-shot examples, decomposition, and role/system framing — are the levers that reduce that noise without touching model weights.

## Why it matters for agentic development
Agents are prompts in a loop. Every tool call, every planning step, every self-check is governed by an instruction you wrote. When a prompt is sloppy, the failure compounds across the loop — a slightly-off interpretation early becomes a wrong tool call, a wrong file edit, a wrong conclusion. Treating the prompt as a versioned spec is what makes agent behavior debuggable and reproducible rather than a slot machine.

## Key ideas to cover
- **Specificity beats politeness**: name the inputs, the output format, the units, the edge cases. "Fit a model" vs. "fit a symbolic expression in variables x1,x2; return the expression and its MSE on the held-out split."
- **Few-shot / examples**: show 1–3 worked input→output pairs to pin down format and style faster than any description.
- **Decomposition**: split a hard task into ordered sub-steps (plan, then execute, then verify) instead of one mega-instruction.
- **Role / system prompts**: persistent framing ("you are a careful research assistant who refuses to overfit") sets defaults that survive the whole session.
- **The prompt as a spec**: state success criteria explicitly so the output is checkable, not just plausible.
- **Negative constraints**: say what NOT to do (don't invent data, don't change the schema).
- **Make uncertainty legible**: ask the model to flag low-confidence steps rather than bluff.

## Hands-on / demo
Take a symbolic-regression task and show two prompts side by side. Prompt A: "find a formula for this data." Prompt B: a structured version that names the variables, fixes the operator set (+, −, ×, /, sin), requests the expression plus its error on a held-out split, and gives one worked example of the expected output. Run both against the same dataset and compare: B yields a parseable, comparable answer; A yields prose you have to clean up by hand. The point lands immediately when the audience sees the format discipline pay off.

## Connections
- C1 (agentic coding): your first real prompts steer code generation in a reproducible repo — prompt-as-spec mirrors commit-as-record.
- C2 (research agent): the agent's planning and tool-selection prompts are where these patterns earn their keep.
- Spine 1 (evaluation→fitness): a prompt that states explicit success criteria is already halfway to an eval — the same criteria become scoring rules later.
- Spine 2 (context engineering): prompting is the inner loop; context engineering (Tutorial 07) is the outer loop that decides what surrounds the prompt.

## Further reading
- Anthropic's prompt engineering guidance and prompt-library documentation.
- The "few-shot learning" framing from the original large-LM papers (name generically: GPT-3-era in-context learning).
- Any current model provider's system-prompt / role best-practices doc.
- A project's own `CLAUDE.md` and prior prompts as a living library of spec-style instructions.
