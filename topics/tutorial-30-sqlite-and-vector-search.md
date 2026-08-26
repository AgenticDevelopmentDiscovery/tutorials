---
title: "Tutorial 30 — SQLite & Vector Search (sqlite-vec)"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 30 — SQLite & Vector Search (sqlite-vec)

> Student-led tutorial (~15 min). The database that ships inside your app — and now does vector search too.

## What it is
SQLite is an embedded, zero-configuration relational database: there is no server process, no port, no daemon. The entire database is a single file on disk (or in memory), and you talk to it through a library linked directly into your program. It is the most widely deployed database in the world — it lives inside browsers, phones, and aircraft — precisely because it has no operational overhead. For a researcher, it means you can `import sqlite3` (it ships with Python) and have durable, transactional, SQL-queryable storage in one line.

`sqlite-vec` is a small loadable extension that teaches SQLite to store and query vectors. You create a virtual table of embeddings, insert your float arrays, and run k-nearest-neighbor queries with a `MATCH`-style operator that ranks rows by distance (L2, cosine, etc.). The result is a complete, file-based vector store with no infrastructure: the same `.db` file holds your documents, your metadata, and your embeddings side by side.

## Why it matters for agentic development
A retrieval-augmented agent needs somewhere to put its embeddings, and the first instinct is to reach for a hosted vector database. For most research projects that is premature: it adds an account, a network dependency, and a moving part that breaks reproducibility. SQLite + sqlite-vec gives you a RAG store you can commit alongside your code, hand to a labmate, and run offline. It keeps the *store* boring so the interesting work — chunking, grounding, evaluation — stays in focus.

## Key ideas to cover
- SQLite is embedded and serverless: one file, no daemon, ACID transactions, ships with Python's stdlib.
- Loadable extensions: how `sqlite-vec` plugs in via `db.enable_load_extension(True)` / `load_extension(...)`.
- Virtual tables (`vec0`) for storing fixed-dimension float vectors alongside an `id`.
- KNN queries: `ORDER BY distance` with cosine or L2; returning the nearest chunks for a query embedding.
- Keeping documents, metadata, and vectors in one file — join vector hits back to source text with plain SQL.
- Limits: it is brute-force / single-writer; great to ~10^5–10^6 vectors, not a horizontally-scaled service.
- Reproducibility: a `.db` file is a versionable, shareable artifact.

## Hands-on / demo
Build a tiny grounding store for the capstone. Take ~50 short documents describing candidate model forms or domain facts (e.g., physical-law snippets for symbolic regression), embed them, and write each into a `vec0` table keyed to a `documents` table holding the raw text. Then embed a query like "conservation law relating force and acceleration," run a KNN query for the top-5, and join back to print the source snippets. Show the whole thing is one `.db` file you can delete and rebuild deterministically.

## Connections
- C3 (retrieval/grounding): this is the *store* layer of your RAG pipeline — pair it with the separate embeddings/RAG tutorial.
- Spine 2 (context engineering): the file-based store is the simplest "domain-knowledge-as-context" backend before you scale up.
- Capstone: ground candidate-expression generation in retrieved domain facts without standing up infrastructure.
- Tutorial 31 (Postgres/pgvector): the natural next step when one file and one writer stop being enough.

## Further reading
- SQLite official documentation (especially "When To Use SQLite" and the virtual-table interface).
- The `sqlite-vec` project README and quickstart on GitHub.
- Python `sqlite3` module docs (extension loading, `enable_load_extension`).
- Background reading on approximate vs. exact nearest-neighbor search.
