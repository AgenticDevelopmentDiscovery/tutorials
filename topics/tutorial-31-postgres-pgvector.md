---
title: "Tutorial 31 — Postgres & pgvector"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 31 — Postgres & pgvector

> Student-led tutorial (~15 min). When your single file stops scaling, graduate to a real database — without giving up SQL or vectors.

## What it is
PostgreSQL is a mature, open-source, client-server relational database. Unlike SQLite it runs as a process you connect to over a socket, supports many concurrent readers and writers, enforces rich types and constraints, and scales to large datasets with sophisticated indexing and a real query planner. It is the default "serious" relational database for research infrastructure and production systems alike.

`pgvector` is a Postgres extension that adds a first-class `vector` column type plus distance operators (`<->` for L2, `<=>` for cosine, `<#>` for inner product) and approximate-nearest-neighbor indexes (IVFFlat and HNSW). Because the vectors live inside Postgres, you can write a *single* query that filters on ordinary columns (date, author, experiment id) **and** ranks by embedding similarity — a hybrid SQL + vector search. You keep all the relational machinery you already know and gain similarity search on top.

## Why it matters for agentic development
As an agent's knowledge base grows — many users, frequent updates, millions of chunks, metadata-heavy filtering — the embedded store's single-writer, brute-force model becomes the bottleneck. Postgres + pgvector lets the *store* grow with the project: concurrent writes from multiple agent runs, ANN indexes that keep retrieval fast at scale, and hybrid queries that combine structured filters with semantic ranking. It is the same conceptual interface as your SQLite store, so the RAG logic you wrote in C3 ports over with minimal change.

## Key ideas to cover
- Client-server vs. embedded: why concurrency, durability, and shared access push you off SQLite.
- The `vector` type and the distance operators (`<->`, `<=>`, `<#>`); matching the operator to your embedding's training objective.
- ANN indexes: IVFFlat (lists/probes) vs. HNSW (m / ef_search); the recall-vs-latency tradeoff and that they are *approximate*.
- Hybrid queries: `WHERE` on metadata + `ORDER BY embedding <=> query LIMIT k` in one statement.
- When to graduate: dataset size, write concurrency, need for joins/filters, multiple consumers, ops maturity.
- Connecting from Python (e.g., `psycopg`); normalizing vectors; keeping embedding dimension consistent.

## Hands-on / demo
Stand up Postgres (Docker or a managed instance), `CREATE EXTENSION vector`, and load the same capstone corpus from Tutorial 30 — but now tag each row with metadata like `domain` and `source_year`. Demonstrate a hybrid query: "find the 5 chunks most similar to this query embedding, but only among `domain = 'mechanics'` and `source_year >= 2000`." Then build an HNSW index and show the latency drop on a larger synthetic set, noting that results are now approximate.

## Connections
- C3 (retrieval/grounding): the scale-up path for the same RAG store; hybrid filtering improves grounding precision.
- Spine 2 (context engineering): structured + semantic retrieval is how domain-knowledge-as-context matures.
- C4 (orchestration): a shared Postgres lets multiple orchestrated agents read/write one knowledge base concurrently.
- Tutorial 30 (SQLite): the "before" half of the graduation story — start there, move here on need.

## Further reading
- PostgreSQL official documentation (data types, indexing, the query planner).
- The `pgvector` project README on GitHub (operators, IVFFlat and HNSW index tuning).
- `psycopg` (Postgres adapter for Python) documentation.
- HNSW paper (Malkov & Yashunin) for the index intuition behind approximate search.
