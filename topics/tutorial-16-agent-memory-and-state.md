---
title: "Tutorial 16 — Agent Memory & State"
status: draft
updated: 2026-06-25
unit: tutorial
---

# Tutorial 16 — Agent Memory & State

> Student-led tutorial (~15 min). An agent with no memory re-derives everything from scratch every turn — memory is what turns a chatbot into a collaborator.

## What it is
An agent's "memory" is everything it can condition on beyond the user's current message. The cheapest form is the context window itself: the running transcript the model sees on each step (short-term, volatile, bounded by token limits). Beyond that lies external state that survives a single response or a single session — a scratchpad file, a vector store of past observations, a structured database of facts, or a summary the agent rewrites as it goes. Memory is therefore less a single feature than a layered system: what's in front of the model right now, what can be pulled back in on demand, and what is deliberately discarded.

The core engineering problem is not storing things — disks are cheap — but deciding what to remember, in what form, and when to bring it back. Raw transcripts grow without bound and bury signal in noise; good memory systems compress (summaries), index (retrieval keys), and forget (eviction policies). This is context engineering applied to time.

## Why it matters for agentic development
Multi-step agents fail in characteristic ways when memory is mishandled: they loop because they forgot a step already failed, they contradict earlier decisions, or they blow the context window mid-task and silently drop the instructions. Designing memory explicitly — a scratchpad for working state, a durable store for cross-session facts, and a compaction step that summarizes rather than truncates — is often the difference between an agent that finishes a long task and one that drifts. Memory also makes runs reproducible and auditable: persisted state is a log you can inspect.

## Key ideas to cover
- Short-term (context window) vs long-term (external store) memory, and why the boundary is a design choice.
- Scratchpads / working memory: the agent writes intermediate state to a file or note and reads it back, freeing the context window.
- Persistence across sessions: serializing facts, decisions, and artifacts so a later run resumes instead of restarting.
- Compaction: summarizing old turns vs naive truncation; what information must survive a summary.
- Retrieval as recall: storing memories and pulling the relevant few back in (overlaps with RAG, Tutorial 09, in C3).
- What to forget: stale facts, dead ends, secrets, and noise; eviction and TTL policies.
- Memory hygiene: avoiding "context poisoning," where a wrong fact gets remembered and repeatedly reinforced.

## Hands-on / demo
Run a symbolic-regression agent on a dataset across two sessions. In session one, have it record to a `scratchpad.md`: candidate model forms it tried, their held-out error, and which feature transforms helped. End the session. In session two, start a fresh context but load `scratchpad.md` — show the agent immediately skips the linear baseline it already beat and proposes a refinement of its best prior expression. Contrast with a no-memory run that re-explores the same dead ends. The persisted scratchpad is visibly the difference.

## Connections
- C1 (reproducible repo): persisted memory is just versioned state in the repo — scratchpads and summaries live next to code and are diffable.
- Spine 2 (context engineering): memory *is* context engineering over time — choosing what to keep in the window is the same skill as choosing what to retrieve.
- Capstone: an evolutionary search must remember the population, fitnesses, and lineage across generations; that's long-term agent memory under another name.
- C3 (retrieval): long-term memory and RAG share the store-then-recall machinery.

## Further reading
- Anthropic's documentation on context windows, prompt caching, and context management for long-running agents.
- Writings on the "MemGPT"-style approach of paging memory in and out of a bounded context.
- Vector-store / embedding library docs (e.g. FAISS, Chroma) as the substrate for long-term recall.
- Discussions of context compaction and summarization strategies in agent frameworks.
