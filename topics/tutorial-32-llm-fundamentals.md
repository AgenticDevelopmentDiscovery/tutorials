---
title: "Tutorial 32 — LLM Fundamentals"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 32 — LLM Fundamentals

> Student-led tutorial (~15 min). What is actually happening inside the box when an agent "thinks."

## What it is
A large language model is a neural network — almost always a Transformer — trained to predict the next token in a sequence. Text is first broken into **tokens** (subword units, not whole words) by a tokenizer; the model consumes a sequence of token ids and outputs a probability distribution over the next token. Generation is autoregressive: sample one token, append it, feed the longer sequence back in, repeat. There is no database lookup and no symbolic reasoning engine underneath — just a very large, learned function mapping token sequences to next-token probabilities.

Training happens in stages: **pretraining** on enormous text corpora teaches the next-token objective and absorbs broad world knowledge into the weights; **post-training** (instruction tuning and preference optimization such as RLHF) shapes the model into a helpful, steerable assistant. At **inference** the weights are frozen — the model is not learning from your prompt; anything it "remembers" within a conversation lives only in the context window you feed it. The **context window** is the maximum number of tokens (prompt + generation) the model can attend to at once.

## Why it matters for agentic development
Every capability and every failure mode of your agent traces back to this mechanism. Hallucination is the model confidently sampling plausible-but-wrong tokens because it optimizes likelihood, not truth. The context window is a hard budget that motivates the entire context-engineering spine — retrieval and memory exist to put the right tokens in front of a frozen model. Temperature and sampling control how deterministic your agent is, which matters enormously when you need reproducible evals. Understanding "next-token predictor over a fixed window" demystifies why grounding, evaluation, and prompt design are the real levers.

## Key ideas to cover
- Tokenization: subword tokens, why "token count != word count," and why it affects cost, context limits, and even arithmetic/spelling quirks.
- Next-token prediction and autoregressive generation; the model outputs a distribution, not a single answer.
- Training vs. inference: pretraining → post-training (instruction tuning, RLHF); weights frozen at inference, no in-place learning.
- Context window: a finite token budget; everything the model "knows in the moment" must fit inside it.
- Sampling controls: temperature, top-p / top-k; greedy vs. stochastic decoding and the determinism/diversity tradeoff.
- Capabilities: in-context learning, instruction following, broad knowledge, code/math to a point.
- Failure modes: hallucination, sensitivity to prompt phrasing, brittleness on long-horizon reasoning, knowledge cutoff/staleness.

## Hands-on / demo
Run a tokenizer (e.g., `tiktoken` or a Hugging Face tokenizer) on a few strings — a normal sentence, a long number, a chemical formula, a code snippet — and show the token splits and counts; connect this to context budgets. Then take a single symbolic-regression prompt ("propose a candidate expression for this dataset") and generate it at temperature 0, 0.7, and 1.2, showing how determinism and diversity change. Frame temperature as a knob for the capstone's exploration vs. exploitation.

## Connections
- Spine 1 (evaluation→fitness): determinism (temperature, sampling) directly affects whether your eval harness is reproducible.
- Spine 2 (context engineering): the finite context window is the *reason* retrieval and memory exist.
- Capstone: sampling temperature is the LLM's exploration knob in evolutionary search over expressions.
- C2 (research agent): knowing failure modes tells you what your eval harness must actually measure.

## Further reading
- "Attention Is All You Need" (Vaswani et al.) — the Transformer architecture.
- The GPT-3 paper ("Language Models are Few-Shot Learners") for in-context learning.
- The InstructGPT / RLHF paper for how post-training shapes assistants.
- A hands-on intro such as Karpathy's "Let's build GPT" or his tokenizer ("minbpe") walkthrough.
