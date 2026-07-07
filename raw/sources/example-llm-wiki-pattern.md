# The LLM Wiki Pattern

**Author:** Andrej Karpathy  
**Date:** April 4, 2026  
**Source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Summary

The LLM Wiki pattern is a new approach to building personal knowledge bases using Large Language Models. Unlike traditional RAG (Retrieval-Augmented Generation) systems that retrieve and synthesize information on every query, the LLM Wiki pattern has the LLM incrementally build and maintain a persistent wiki — a structured, interlinked collection of markdown files.

## Key Concepts

### The Core Difference

Traditional RAG systems rediscover knowledge from scratch on every question. The LLM Wiki pattern is different: the LLM incrementally builds and maintains a persistent wiki that sits between you and raw sources. When you add a new source, the LLM reads it, extracts key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting contradictions, and maintaining cross-references.

### Three-Layer Architecture

1. **Raw sources** — Immutable source documents (articles, papers, data files)
2. **The wiki** — LLM-generated markdown files (summaries, entity pages, concept pages)
3. **The schema** — Configuration document (AGENTS.md or CLAUDE.md) defining structure and workflows

### Core Operations

- **Ingest:** Process new sources and integrate them into the wiki
- **Query:** Answer questions using the wiki with citations
- **Lint:** Health-check the wiki for contradictions, orphans, and gaps

### Why It Works

The tedious part of maintaining a knowledge base is bookkeeping — updating cross-references, keeping summaries current, noting contradictions, maintaining consistency. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

## Use Cases

- Personal knowledge management (goals, health, self-improvement)
- Research (deep-diving on topics over weeks/months)
- Reading companion (building character/theme wikis for books)
- Business/team internal wikis (fed by Slack, meetings, documents)
- Competitive analysis, due diligence, trip planning, course notes

## Tools and Workflow

- **Obsidian** recommended for browsing (graph view, backlinks, search)
- **WikiLinks** format `[[page-name]]` for internal references
- **index.md** for content catalog (works well up to ~100 sources)
- **log.md** for chronological record of operations
- Optional: qmd for search, Marp for slides, Dataview for queries

## Philosophy

The human's job is to curate sources, direct analysis, ask good questions, and think about meaning. The LLM's job is everything else — summarizing, cross-referencing, filing, bookkeeping.

Related to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails. The part Bush couldn't solve was who does the maintenance. The LLM handles that.
