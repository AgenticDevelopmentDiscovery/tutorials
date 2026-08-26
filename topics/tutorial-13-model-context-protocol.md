---
title: "Tutorial 13 — The Model Context Protocol (MCP)"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 13 — The Model Context Protocol (MCP)

> Student-led tutorial (~15 min). A USB-C port for plugging tools and data into any agent.

## What it is
The Model Context Protocol (MCP) is an open standard for connecting agents to external tools, data, and context in a uniform way. Tutorial 12's function calling is *local* — you hand-define tools inside your program. MCP generalizes this across process and vendor boundaries. An **MCP server** exposes capabilities — tools to call, resources to read, and prompts to reuse — over a defined protocol. An **MCP client** (your agent host, e.g., a CLI or IDE) connects to one or more servers and makes their capabilities available to the model. Because the interface is standardized, the same database server, file server, or web-search server can plug into any MCP-aware agent, regardless of which model provider is behind it.

The payoff is composability. Instead of every agent re-implementing a connector to your lab's data store, you write one MCP server and every agent in the course can use it. Servers run as separate processes (local over stdio, or remote over HTTP), which also gives you a clean security and isolation boundary.

## Why it matters for agentic development
MCP is the difference between a one-off agent and an *ecosystem*. It lets you build a capability once and reuse it everywhere, mix tools from different authors, and swap the underlying model without rewriting your tools. For a cross-disciplinary cohort, that means a shared, growing toolbox: someone's protein-database server and someone else's symbolic-regression evaluator become available to the whole class through the same standard interface.

## Key ideas to cover
- The problem MCP solves: the N×M connector explosion (every agent × every tool).
- Three things a server can expose: **tools** (callable functions), **resources** (readable data/context), **prompts** (reusable templates).
- Client–server architecture; transports (local stdio vs. remote HTTP/SSE).
- How discovered tools become ordinary function calls to the model (MCP rides on top of tool use).
- Security and trust: separate processes, scoping, approving servers before use.
- Where MCP fits the stack: above the model API, below your application logic.
- Reusability: write a server once, share it across the cohort and across providers.

## Hands-on / demo
Stand up a minimal MCP server that wraps the course eval harness, exposing one tool `evaluate_formula(expr, data)` and one resource `dataset://current`. Connect it to an MCP-aware client (e.g., Claude Code or VS Code) and show the agent discovering the tool, reading the dataset resource as context, and calling the evaluator — all without the harness being hand-coded into the agent. Contrast with Tutorial 12's in-process version to make the boundary concrete.

## Connections
- **C3 (retrieval/grounding):** MCP resources are a clean way to feed retrieved or domain data into the agent — directly serving Spine 2 (context engineering).
- **C2 (research agent) & Spine 1:** packaging the eval harness as an MCP server makes the same fitness signal reusable by every later agent and the capstone.
- **C4 (orchestration):** standardized servers make multi-agent setups far easier to wire together reliably.
- **Tool-plural goal:** one MCP server works across Claude, Codex, Gemini, and open-source hosts.

## Further reading
- The MCP specification and the official "introduction to MCP" docs.
- Reference MCP server implementations (filesystem, fetch, database) as templates.
- Your agent host's MCP configuration guide (e.g., Claude Code's MCP setup docs).
