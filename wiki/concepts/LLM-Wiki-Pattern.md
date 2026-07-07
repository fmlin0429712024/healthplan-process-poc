---
tags: [llm, wiki, knowledge-management, pattern]
date: 2026-07-07
type: concept
---

# LLM Wiki Pattern

**Type:** Pattern/Method
**Proposed by:** [[Andrej-Karpathy]]
**Year:** 2026

## Summary

The LLM Wiki pattern is a method for building personal knowledge bases where Large Language Models act as persistent wiki maintainers rather than just query engines. Unlike traditional RAG systems that retrieve and synthesize information on every query, the LLM Wiki pattern has the LLM incrementally build and maintain a structured, interlinked collection of markdown files that compounds over time.

## Core Architecture

### Three-Layer Structure

1. **Raw sources** — Immutable source documents (articles, papers, data files)
2. **The wiki** — LLM-generated markdown files (summaries, entity pages, concept pages)
3. **The schema** — Configuration document defining structure and workflows

### Core Operations

- **Ingest:** Process new sources and integrate them into the wiki
- **Query:** Answer questions using the wiki with citations
- **Lint:** Health-check the wiki for contradictions, orphans, and gaps

## Key Advantages

**Maintenance Solution:** The tedious part of maintaining a knowledge base is bookkeeping — updating cross-references, keeping summaries current, noting contradictions, maintaining consistency. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored and can touch 15 files in one pass, making the cost of maintenance near zero.

**Persistent Knowledge:** Unlike RAG which rediscoveres knowledge from scratch on every question, the LLM Wiki pattern maintains a persistent artifact that grows richer with every source. Cross-references are already there, contradictions are already flagged, and the synthesis already reflects everything that's been read.

**Human-LLM Division of Labor:** The human curates sources and asks questions; the LLM handles summarizing, cross-referencing, filing, and bookkeeping.

## Use Cases

- Personal knowledge management (goals, health, self-improvement)
- Research (deep-diving on topics over weeks/months)
- Reading companion (building character/theme wikis for books)
- Business/team internal wikis (fed by Slack, meetings, documents)
- Competitive analysis, due diligence, trip planning, course notes

## Related Pages

- [[llm-wiki-pattern-karpathy]] — Original source document
- [[Andrej-Karpathy]] — Author of the pattern
- [[RAG]] — Traditional retrieval-augmented generation approach
- [[Memex]] — Historical predecessor concept

## Implementation Notes

- **WikiLinks:** Use `[[page-name]]` format for internal links to enable graph view and backlink tracking
- **Tools:** Obsidian recommended for browsing (graph view, backlinks, search)
- **Index:** index.md serves as content catalog (works well up to ~100 sources)
- **Log:** log.md provides chronological record of operations