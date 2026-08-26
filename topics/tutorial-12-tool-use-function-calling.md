---
title: "Tutorial 12 — Tool Use & Function Calling"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 12 — Tool Use & Function Calling

> Student-led tutorial (~15 min). How a text model reaches out and *does* things.

## What it is
Tool use (a.k.a. function calling) is the mechanism that lets a language model invoke external code. You give the model a set of **tool definitions**: each is a name, a natural-language description, and a **schema** (typically JSON Schema) describing the arguments. When the model decides a tool is needed, instead of emitting prose it emits a structured **tool call** — the tool name plus arguments conforming to the schema. Your runtime executes the actual function, captures the result, and feeds that result back into the model's context as a **tool result** message. The model then continues, now knowing what the tool returned.

Crucially, the model does not run the code — it only *requests* the call. The orchestration layer (your harness, or a CLI like Claude Code) is what actually executes and returns results. This separation is what makes tool use safe and inspectable: you can validate arguments, sandbox execution, log every call, and decide whether to approve it.

## Why it matters for agentic development
Tools are how an agent's reasoning touches reality. Without them a model is a closed box; with them it can run experiments, query data, edit files, and call APIs. Good tool design is most of the work in building a reliable agent: descriptions that tell the model *when* to use the tool, schemas tight enough to prevent malformed calls, and results formatted so the model can actually parse them. The agent loop from Tutorial 11 is powered entirely by tools — each "action" is a function call.

## Key ideas to cover
- Anatomy of a tool definition: name, description, parameter schema (JSON Schema), required vs. optional fields.
- The round-trip: model emits a tool call → runtime executes → tool result returns to context → model continues.
- The model *chooses* tools (and arguments) from descriptions — so descriptions are prompts, not docs.
- Schemas as guardrails: typed/enumerated parameters reduce malformed or unsafe calls.
- Multiple and parallel tool calls; handling errors and returning them as observations.
- Result formatting: concise, structured, and self-describing beats raw dumps.
- Common pitfalls: vague descriptions, over-broad tools, results too large for context.

## Hands-on / demo
Define two tools for the course substrate: `fit_linear(data)` and `evaluate_formula(expr, data)` returning an error metric. Show the JSON Schema for each, then prompt the model to "find the best model for this data." Trace the actual tool-call JSON it emits, execute it, and show the tool-result message going back. Demonstrate a failure: pass a malformed `expr`, return the error string as the tool result, and watch the model recover by trying a corrected expression.

## Connections
- **C2 (research agent):** your eval harness is literally exposed to the agent *as a tool* — `evaluate_formula` is the harness's public face.
- **Spine 1 (evaluation→fitness):** the tool result (an error/fitness score) is the signal that later drives evolutionary selection in the capstone.
- **C1 (reproducible repo):** tool execution should be deterministic and logged, reinforcing C1's reproducibility discipline.
- **Tutorial 13 (MCP):** function calling is *local*; MCP standardizes how tools are exposed across processes and providers.

## Further reading
- Any provider's tool-use / function-calling guide (e.g., Anthropic's tool use docs, OpenAI function calling) — compare the shared shape.
- The JSON Schema specification — the lingua franca of tool argument definitions.
- The Toolformer paper for the research motivation behind teaching models to call tools.
