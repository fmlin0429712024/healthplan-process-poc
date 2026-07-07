---
tags: [llm, wiki, knowledge-management, rag]
date: 2026-07-07
type: source
---

# The LLM Wiki Pattern

**Type:** Article
**Date:** 2026-04-04
**Source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**Tags:** #llm #wiki #knowledge-management #rag

## Summary

The LLM Wiki pattern is a new approach to building personal knowledge bases using Large Language Models. Unlike traditional RAG (Retrieval-Augmented Generation) systems that retrieve and synthesize information on every query, the LLM Wiki pattern has the LLM incrementally build and maintain a persistent wiki — a structured, interlinked collection of markdown files.

The core innovation is that the LLM acts as a wiki maintainer rather than just a query engine. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting contradictions, and maintaining cross-references. This creates a persistent artifact that grows richer with every source.

## Key Takeaways

- **Core difference from RAG:** Traditional RAG systems rediscover knowledge from scratch on every question. The LLM Wiki pattern maintains a persistent wiki that sits between you and raw sources, with the LLM doing incremental updates.

- **Three-layer architecture:** Raw sources (immutable documents), the wiki (LLM-generated markdown files), and the schema (configuration document defining structure and workflows).

- **Core operations:** Ingest (process new sources), Query (answer questions using the wiki with citations), and Lint (health-check for contradictions, orphans, and gaps).

- **Maintenance advantage:** The tedious part of maintaining a knowledge base is bookkeeping — updating cross-references, keeping summaries current, noting contradictions. LLMs don't get bored and can touch 15 files in one pass, making maintenance cost near zero.

- **Use cases:** Personal knowledge management, research, reading companion, business/team internal wikis, competitive analysis, due diligence, trip planning, course notes.

## Related Pages

- [[Andrej-Karpathy]] — Author of the LLM Wiki pattern
- [[LLM-Wiki-Pattern]] — Concept page for the pattern itself
- [[RAG]] — Comparison with traditional Retrieval-Augmented Generation
- [[Memex]] — Historical connection to Vannevar Bush's Memex (1945)

## Contradictions & Questions

No contradictions noted yet. This is the foundational document for this wiki.

## Raw Notes

- **Tools and Workflow:** Obsidian recommended for browsing (graph view, backlinks, search). WikiLinks format `[[page-name]]` for internal references. index.md for content catalog (works well up to ~100 sources). log.md for chronological record of operations.

- **Philosophy:** The human's job is to curate sources, direct analysis, ask good questions, and think about meaning. The LLM's job is everything else — summarizing, cross-referencing, filing, bookkeeping.

- **Historical context:** Related to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails. The part Bush couldn't solve was who does the maintenance. The LLM handles that.