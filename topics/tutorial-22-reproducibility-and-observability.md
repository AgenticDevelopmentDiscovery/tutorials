---
title: "Tutorial 22 — Reproducibility, Logging & Observability for Agent Runs"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 22 — Reproducibility, Logging & Observability for Agent Runs

> Student-led tutorial (~15 min). If you can't replay a run, you can't trust, debug, or publish it.

## What it is
Reproducibility means a run can be re-executed and yield the same result (or a controlled distribution of results). For agents this is harder than for ordinary code because there are extra sources of nondeterminism: model sampling temperature, tool outputs, retrieval over a changing corpus, and wall-clock-dependent behavior. You buy reproducibility back with discipline: pin model versions and decoding parameters, set and record seeds where they exist, snapshot the corpus and configs, and capture the full input that produced each output.

Observability is the runtime complement: structured logs, traces, and lineage that let you see *what the agent actually did*. A trace records the sequence of steps — prompts, tool calls, retrieved chunks, intermediate outputs — so a failure becomes inspectable rather than mysterious. Lineage records where each artifact came from (which data, which config, which parent run), which is exactly what you need when an evolutionary search produces a surprising winner and you must explain its provenance.

## Why it matters for agentic development
Agents fail in subtle, intermittent ways. Without logs and traces you debug by re-running and praying; with them you read the transcript and find the bad tool call. Reproducibility is also a research-integrity issue: a discovered model or equation is only a result if someone else can regenerate it. The same machinery — recorded seeds, pinned configs, run logs — is what makes a leaderboard credible and an evolutionary lineage auditable.

## Key ideas to cover
- Sources of nondeterminism in agents: sampling, tool outputs, retrieval, concurrency, time.
- Pin and record: model id/version, temperature/top-p, seed, prompt template, corpus snapshot, code commit.
- Structured run logs vs. ad-hoc prints; one record per step with inputs and outputs.
- Tracing: the full step sequence as a tree/timeline you can replay and inspect.
- Lineage/provenance: parent run, data version, config hash — link every artifact to its origin.
- Run manifests: a single file per run that captures everything needed to re-run it.
- Honest failure reporting: log errors, retries, and partial results; never silently drop them.

## Hands-on / demo
Wrap one symbolic-regression agent run so that it emits a JSON run manifest (model id, seed, dataset hash, config) plus a step log of every proposed equation and its harness score. Re-run from the manifest and show the results match. Then deliberately corrupt one input and show how the trace pinpoints exactly where the run diverged — and demonstrate logging a failed/timed-out candidate honestly rather than dropping it.

## Connections
- Operationalizes the reproducible-repo goal of **C1** and the reliability goal of **C4**.
- Lineage is essential for the capstone: an evolutionary run produces a *genealogy* of candidate equations that must be traceable to be trusted.
- Spine 1 (evaluation→fitness): logged scores from the **C2** harness are the audit trail of the fitness function.
- Spine 2 (context engineering): logging retrieved chunks (**C3**) makes RAG behavior observable.

## Further reading
- OpenTelemetry concepts (traces, spans) adapted to LLM/agent runs.
- LLM-tracing tools such as LangSmith, Phoenix/Arize, or Weights & Biases run tracking.
- Provider docs on determinism knobs (seeds, temperature, system fingerprint).
- The "Show Your Work"/reproducibility-checklist literature in ML (e.g., NeurIPS reproducibility checklist).
