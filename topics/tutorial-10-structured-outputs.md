---
title: "Tutorial 10 — Structured Outputs & Schema-Constrained Generation"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 10 — Structured Outputs & Schema-Constrained Generation

> Student-led tutorial (~15 min). If you're parsing prose to extract an answer, you've already lost — make the model emit structure you can trust.

## What it is
Structured output is generation constrained to a machine-readable shape — most commonly JSON conforming to a declared schema, or the structured arguments of a tool/function call. Instead of asking the model for a paragraph and then scraping a number out of it with brittle regex, you declare the fields, types, and constraints you need, and the model returns data that fits. Schema-constrained generation enforces this at decode time: the output is *guaranteed* to be valid JSON matching the schema, so the parsing step that used to fail silently simply can't.

The contrast with "parse the prose" is the whole point. Prose parsing is fragile: phrasing drifts, the model adds a polite preamble, a number appears with unexpected units. A schema makes the contract explicit and the output checkable. The same machinery underlies tool calling, where the model's request to invoke a function is itself a schema-constrained object the runtime can execute directly.

## Why it matters for agentic development
Agents are pipelines — the output of one step is the input to the next. That handoff has to be reliable, and free-form text is a terrible interface between automated stages. Structured outputs make agent steps composable: a planning step emits a typed plan, a tool-call step emits validated arguments, an evaluation step emits a scored record. Validation catches malformed results before they corrupt downstream logic, and a schema doubles as documentation of what each step is contractually obligated to produce.

## Key ideas to cover
- **Schema as contract**: declare fields, types, and constraints up front; the output must conform.
- **Tool-call-style outputs**: function calling is structured generation — the model emits arguments a runtime executes.
- **Validation**: parse-then-validate (e.g., against a JSON Schema / typed model); reject or repair on failure.
- **Structure beats parsing prose**: brittle regex over free text vs. a guaranteed shape.
- **Composability**: typed outputs are clean interfaces between agent steps.
- **Constrained decoding vs. prompt-and-hope**: enforcing the grammar at decode time beats merely asking nicely.
- **Design the schema for the consumer**: include exactly the fields the next stage needs, no prose.

## Hands-on / demo
Define a schema for a symbolic-regression result: `{ "expression": string, "variables": [string], "mse": number, "complexity": integer, "notes": string }`. Run the agent with a free-text prompt and show how flaky it is to extract `mse` and `complexity` from the prose answer. Then re-run requesting output against the schema (or as a tool call) and validate each result. Feed the validated records straight into a leaderboard sort — no scraping, no cleanup. The audience sees structured output as the connective tissue that lets the eval harness ingest agent results automatically.

## Connections
- C2 (research agent): the eval harness is born here — structured agent outputs are what the harness can score without hand-parsing.
- Spine 1 (evaluation→fitness): a schema'd result record is *directly* the unit the fitness function consumes in the capstone.
- C4 (orchestration & reliability): typed step-to-step handoffs are a backbone of reliable multi-step agents.
- Capstone: the generate→evaluate→select loop runs on structured candidate records flowing into the leaderboard.

## Further reading
- JSON Schema specification and a typed-validation library (e.g., a Pydantic-style model).
- Provider documentation on tool/function calling and structured/JSON output modes.
- Anthropic docs on tool use and structured outputs for current models.
- Notes on constrained decoding / grammar-constrained generation.
