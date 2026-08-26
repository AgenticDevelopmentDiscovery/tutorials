---
title: "Tutorial 09 — Retrieval-Augmented Generation & Embeddings"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 09 — Retrieval-Augmented Generation & Embeddings

> Student-led tutorial (~15 min). Retrieval is how you put the right knowledge in the window automatically — and, for us, how you constrain a search space.

## What it is
Retrieval-augmented generation (RAG) couples a model with an external knowledge store: instead of relying on what's in the weights, the system *retrieves* relevant material at query time and places it in the context window before generating. The retrieval usually runs on **embeddings** — dense vectors that map text (or other data) into a geometry where semantic similarity is proximity. You **chunk** a corpus into passages, embed each chunk, and store the vectors; at query time you embed the query, do a **vector search** (nearest-neighbor) to find the closest chunks, and ground the generation in them.

Two design choices dominate quality. Chunking determines what a "unit of knowledge" is — too large and retrieval is imprecise, too small and it loses coherence. Embedding/retrieval quality determines whether the right chunk surfaces at all. RAG is best understood not as a toy Q&A trick but as automated, query-conditioned context engineering: it decides what enters the window for each request.

## Why it matters for agentic development
Agents need facts they were never trained on — your lab's prior results, a domain's governing equations, your own paper's methods. RAG grounds the agent in those, reducing hallucination and making outputs traceable to sources. More sharply for this course: retrieval can act as a **search-space constraint**. In symbolic regression the space of candidate expressions is vast; retrieving domain knowledge — known functional forms, dimensional constraints, prior good expressions — biases the agent toward physically plausible candidates instead of blind enumeration. Retrieval becomes a prior on the search, not just a lookup.

## Key ideas to cover
- **Embeddings**: text → vector; similarity ≈ distance in vector space.
- **Vector search**: approximate nearest-neighbor over the embedded corpus; trade recall for speed.
- **Chunking**: the granularity decision that quietly determines retrieval precision and coherence.
- **Grounding**: generation conditioned on retrieved passages, ideally with citations back to source.
- **Retrieval as constraint, not Q&A**: surface known forms / constraints to prune a search space.
- **Failure modes**: irrelevant retrievals, missing the right chunk, and over-trusting retrieved-but-wrong text.
- **Evaluation**: measure retrieval (did we fetch the right chunk?) separately from generation (did we use it well?).

## Hands-on / demo
Build a tiny retrieval index over a corpus of known physical laws and functional forms (power laws, exponential decay, oscillatory terms with their typical variable structure). For a symbolic-regression dataset, embed a short description of the data, retrieve the closest candidate forms, and feed them to the agent as priors before it proposes an expression. Compare against an unprimed run on the same data: the retrieval-primed agent reaches a plausible form faster and proposes fewer nonsensical candidates. This makes "retrieval as search-space constraint" concrete rather than abstract.

## Connections
- C3 (retrieval/grounding): this is the direct foundation — RAG is the Challenge 3 skill, applied to model discovery.
- Spine 2 (context engineering): retrieval is automated just-in-time context — the scalable form of Tutorial 07's curation.
- Capstone: domain-knowledge-as-context retrieved into the evolutionary loop steers candidate generation toward valid expressions.
- Spine 1 (evaluation→fitness): retrieval quality itself is evaluable, and the same harness logic applies to scoring retrieved grounding.

## Further reading
- Original RAG paper (retrieval-augmented generation, generically named).
- Sentence-embedding and vector-search libraries (e.g., a sentence-transformers-style model; an ANN index like FAISS-style tooling).
- Provider embeddings documentation and current embedding-model options.
- Notes on chunking strategies and RAG evaluation (retrieval vs. generation metrics).
