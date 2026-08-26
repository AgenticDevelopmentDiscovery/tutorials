---
title: "Tutorial 04 — Anatomy of an LLM API Call"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 04 — Anatomy of an LLM API Call

> Student-led tutorial (~15 min). Under every shiny CLI is one HTTP request — open it up and the whole agent stack stops being magic.

## What it is
An LLM API call is an HTTP request to a model endpoint carrying a structured conversation and some controls, which returns the model's next message. The core is the **messages** array: an ordered list of turns, each with a `role` (`user`, `assistant`, sometimes `system`) and `content`. The API is **stateless** — the model has no memory between calls, so you resend the whole conversation every time. You also pick a **model** (more capable vs. faster/cheaper), set **max_tokens** (a cap on output length), and choose whether to **stream** (receive the answer token-by-token) or wait for the full response.

Two numbers govern cost and behavior. **Tokens** are sub-word chunks; both your input (the full message history) and the output are billed per token, at different rates per model, so a long conversation gets more expensive every turn — which is why context management (Spine 2) matters. **Temperature**-style sampling controls randomness, though modern reasoning models increasingly favor an "effort"/adaptive-thinking control instead of a raw temperature. The response carries the generated content, a **stop reason** (did it finish, hit the token cap, or call a tool?), and a **usage** record of tokens consumed.

## Why it matters for agentic development
Every agent framework — Claude Code, Codex, Gemini, your own Python loop — is ultimately a `while` loop around this one request: send messages, read the response, maybe execute a tool the model asked for, append the result as a new message, and call again. Once you can read a raw request and response, you can reason about latency, cost, why context gets expensive, why streaming improves perceived speed, and how tool-use turns a chat model into an agent. The CLI is convenience; the API is the contract.

## Key ideas to cover
- The request body: `model`, `messages` (roles + content), `max_tokens`, and that the API is stateless.
- Tokens: input *and* output are billed; cost grows with conversation length.
- The response: `content`, `stop_reason`, and `usage` (token counts).
- Sampling/effort controls and what they actually change.
- Streaming vs. non-streaming, and when each is worth it (long outputs → stream).
- Tool use as a stop reason: the model asks, your code runs it, you reply with the result.
- Errors and retries (rate limits, 5xx) — agents must handle them.

## Hands-on / demo
Make one call from Python against Claude (`claude-opus-4-8`) and dissect the response object live — print `response.content`, `response.stop_reason`, and `response.usage`:

```python
import anthropic
client = anthropic.Anthropic()
resp = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user",
               "content": "Propose a symbolic form for data where y grows with x^2."}],
)
print(resp.content[0].text)
print(resp.stop_reason, resp.usage)
```

Then run it again with the previous answer appended as an `assistant` turn plus a follow-up `user` turn, to show statelessness and the rising input-token count. For long outputs, switch to `client.messages.stream(...)` and watch tokens arrive incrementally.

## Connections
- C2 (build a research agent): the agent loop is exactly this call wrapped in tool-use handling — this tutorial is the foundation of that challenge.
- Spine 2 (context engineering): once you see that input tokens are resent and billed every turn, prompt/context management and later retrieval/memory become obviously necessary, not academic.
- C4 (orchestration & reliability): stop reasons, retries, and usage tracking are what a reliable generate→evaluate loop is built on.

## Further reading
- The official Anthropic API documentation (Messages API) and the `anthropic` Python SDK; Codex/OpenAI and Gemini have closely analogous APIs.
- The ReAct paper (Yao et al.) for the reason-act loop that turns a chat model into an agent.
- Provider pricing pages — read them once so token cost stops being abstract.
- Your provider's streaming and tool-use guides.
