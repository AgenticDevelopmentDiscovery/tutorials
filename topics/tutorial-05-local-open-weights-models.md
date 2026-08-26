---
title: "Tutorial 05 — Running Open-Weights Models Locally"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 05 — Running Open-Weights Models Locally

> Student-led tutorial (~15 min). When the weights live on your laptop, the model is yours — no API key, no per-token bill, no data leaving the room.

## What it is
Open-weights models are LLMs whose trained parameters are published for download (e.g. Llama, Mistral, Qwen, Gemma families), so you can run inference on your own hardware instead of calling a hosted API. Two ecosystems dominate the workflow. **Hugging Face** is the hub: a registry of model weights, datasets, and the `transformers` library that loads and runs them in Python. **Ollama** (and `llama.cpp` under it) is the easy button: a single command pulls a model and serves it behind a local, OpenAI-style HTTP endpoint, so the same agent code that hit a cloud API now hits `localhost`.

The enabling trick is **quantization** — storing weights at lower numerical precision (8-bit, 4-bit) instead of 16/32-bit. This shrinks a model several-fold, letting a 7–8B model run on a consumer GPU or even a modern laptop's RAM, at a small and usually acceptable accuracy cost. The tradeoffs are concrete: local models are smaller and generally less capable than frontier hosted models, but they are private, free at the margin, offline-capable, and fully under your control — including the ability to inspect, fine-tune, and pin them.

## Why it matters for agentic development
A tool-plural course shouldn't be hostage to one vendor's API or budget. A local open-weights model — the course's optional Hugging Face path — gives every student a no-cost, private agent backend for experimentation, plus a baseline that never changes out from under them. For the symbolic-regression substrate, a local model can drive cheap, high-volume generate→evaluate iterations where frontier quality isn't required, while reserving paid API calls for the hard cases. Knowing how to stand up a local endpoint also demystifies the whole stack: you see that "an agent" is just code pointed at *some* model, hosted or not.

## Key ideas to cover
- Open weights vs. closed APIs: what you can download, run, inspect, and fine-tune.
- Hugging Face Hub + `transformers`/`pipeline` for loading and running models in Python.
- Ollama / llama.cpp for a one-command local server with an API-compatible endpoint.
- Quantization (4-bit/8-bit, GGUF) and the size/speed/accuracy tradeoff.
- Hardware reality: VRAM/RAM budgets, picking a model size that fits.
- When local beats API: privacy, cost, offline, reproducibility — and when it doesn't (frontier capability).
- Accessibility: removing API keys and bills as a barrier to entry.

## Hands-on / demo
Pull a small quantized model with Ollama (`ollama run qwen2.5:7b`) and chat in the terminal, then show the same model behind an HTTP endpoint so your Tutorial-04 agent code runs unchanged by just swapping the base URL. Compare: ask both a local 7B model and a frontier hosted model to propose a symbolic form for the same dataset, and discuss where the local one suffices versus where it falls short — exactly the routing decision the capstone faces. Optionally load the same weights via Hugging Face `transformers` to show the lower-level path.

## Connections
- Course tool-plurality: this is the optional local Hugging Face backend — it keeps the course vendor-neutral and zero-cost for high-volume runs.
- C4 / capstone (Spine 1, evaluation→fitness): a free local model lets the generate→evaluate→select loop run many more candidates per dollar; the eval harness scores hosted and local outputs identically.
- C2 (research agent): swapping a local endpoint in for a hosted one proves the agent loop is model-agnostic.

## Further reading
- The Hugging Face `transformers` documentation and model cards on the Hub.
- The Ollama documentation and the `llama.cpp` project README (GGUF quantization).
- The "QLoRA" paper (Dettmers et al.) for the intuition behind low-bit quantization.
- Model licenses (Llama, Mistral, Qwen, Gemma) — "open weights" is not always "open source"; read the terms.
