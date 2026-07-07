# LLM Wiki Schema

This document defines how to build and maintain a persistent knowledge base following the LLM Wiki pattern (Karpathy, 2026).

## Core Principle

You are a **wiki maintainer**, not just a chatbot. Your job is to incrementally build and maintain a structured, interlinked collection of markdown files that compounds over time. When sources are added, you extract key information and integrate it into the existing wiki — updating pages, adding cross-references, noting contradictions, and keeping everything consistent.

The wiki is a **persistent artifact** that grows richer with every source and every question. Cross-references are already there. Contradictions are already flagged. The synthesis already reflects everything that's been read.

## Architecture

### Three Layers

1. **raw/** — Immutable source documents
   - `raw/sources/` — Articles, papers, PDFs, text files, data
   - `raw/assets/` — Images, diagrams, media files
   - You READ from raw sources but NEVER modify them

2. **wiki/** — LLM-maintained markdown files
   - You OWN this layer entirely
   - Create pages, update them, maintain cross-references
   - Keep everything consistent as new sources arrive
   - All pages use markdown with WikiLinks: `[[page-name]]`

3. **tools/** — Optional CLI utilities
   - Search engines, parsers, converters
   - Build these as needed to help operate on the wiki

### Wiki Structure

```
wiki/
├── index.md           # Content catalog (updated on every ingest)
├── log.md             # Chronological record (append-only)
├── overview.md        # High-level synthesis of the entire wiki
├── entities/          # People, organizations, products, places
├── concepts/          # Ideas, theories, methods, frameworks
├── sources/           # One summary page per raw source
├── analyses/          # Comparisons, deep-dives, syntheses
└── queries/           # Answers to user questions worth preserving
```

## Operations

### 1. Ingest

When the user adds a new source to `raw/sources/`:

**Standard Flow:**
1. Read the source file
2. Discuss key takeaways with the user
3. Create a summary page in `wiki/sources/[source-name].md`
4. Update or create relevant entity pages in `wiki/entities/`
5. Update or create relevant concept pages in `wiki/concepts/`
6. Add cross-references between related pages
7. Update `wiki/index.md` with new entries
8. Append an entry to `wiki/log.md`
9. Update `wiki/overview.md` if the source changes the big picture

**Summary Page Format:**
```markdown
# [Source Title]

**Type:** Article | Paper | Book | Report | Data
**Date:** YYYY-MM-DD
**Source:** [URL or citation]
**Tags:** #tag1 #tag2 #tag3

## Summary

[2-3 paragraph summary of the main points]

## Key Takeaways

- Point 1
- Point 2
- Point 3

## Related Pages

- [[entity-name]] — How this source relates to this entity
- [[concept-name]] — How this source relates to this concept
- [[other-source]] — Comparison or connection

## Contradictions & Questions

[Note any contradictions with existing wiki content or open questions]

## Raw Notes

[Optional: detailed notes, quotes, data points]
```

**Ingestion Style:**
- Prefer one source at a time with user involvement
- Let the user guide what to emphasize
- A single source might touch 10-15 wiki pages
- Always maintain consistency across all affected pages

### 2. Query

When the user asks a question:

**Standard Flow:**
1. Read `wiki/index.md` to find relevant pages
2. Read the relevant pages
3. Synthesize an answer with citations
4. Ask the user if this answer should be filed in the wiki
5. If yes, create a new page in `wiki/queries/` or `wiki/analyses/`

**Answer Formats:**
- Markdown page (most common)
- Comparison table
- Timeline
- Concept map (as markdown with links)
- Chart or visualization (describe, then optionally generate with code)

**Citation Format:**
Always cite wiki pages: "According to [[source-name]], ..."

### 3. Lint

Periodically health-check the wiki:

**Check for:**
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps that could be filled with web search
- Broken or unclear links

**Output:**
- List of issues found
- Suggested fixes
- Suggested new questions to investigate
- Suggested new sources to look for

## Index and Log

### index.md Format

```markdown
# Wiki Index

Last updated: YYYY-MM-DD

## Overview

[[overview]] — High-level synthesis of the entire knowledge base

## Sources (N)

- [[source-1]] — One-line summary (YYYY-MM-DD)
- [[source-2]] — One-line summary (YYYY-MM-DD)

## Entities (N)

- [[entity-1]] — One-line description
- [[entity-2]] — One-line description

## Concepts (N)

- [[concept-1]] — One-line description
- [[concept-2]] — One-line description

## Analyses (N)

- [[analysis-1]] — One-line description
- [[analysis-2]] — One-line description

## Queries (N)

- [[query-1]] — One-line description
- [[query-2]] — One-line description
```

Update this file on EVERY ingest or new page creation.

### log.md Format

```markdown
# Wiki Log

Chronological record of all wiki operations.

## [YYYY-MM-DD HH:MM] ingest | Source Title

- Created [[source-name]]
- Updated [[entity-1]], [[entity-2]]
- Updated [[concept-1]]
- Added cross-references

## [YYYY-MM-DD HH:MM] query | Question asked

- Synthesized answer from [[page-1]], [[page-2]]
- Created [[query-name]]

## [YYYY-MM-DD HH:MM] lint | Health check

- Found 3 contradictions
- Suggested 5 new cross-references
- Identified 2 orphan pages
```

This is append-only. Use consistent `## [YYYY-MM-DD HH:MM]` prefix for parseability.

## Page Conventions

### WikiLinks

Always use `[[page-name]]` format for internal links. This enables:
- Obsidian graph view
- Easy refactoring (rename a page, all links update)
- Backlink tracking

### Cross-References

Every page should have a "Related Pages" section listing:
- Entities mentioned
- Concepts discussed
- Related sources
- Related analyses

Include a brief note on HOW they're related.

### Contradictions

When a new source contradicts existing wiki content:
1. Note it explicitly in the new source's summary
2. Update the contradicted page with a note
3. Create a comparison page in `wiki/analyses/` if significant
4. Update `wiki/overview.md` if it affects the big picture

### Tags

Use YAML frontmatter for tags:
```markdown
---
tags: [tag1, tag2, tag3]
date: YYYY-MM-DD
type: source | entity | concept | analysis | query
---
```

This enables Obsidian Dataview queries.

## Workflow Tips

### Batch Reading

When you need to check multiple pages, read them in parallel:
- Read `wiki/index.md` first to find relevant pages
- Then read all relevant pages in one batch
- Then synthesize

### Incremental Updates

Don't rewrite entire pages. Make targeted edits:
- Add a new bullet point
- Update a section
- Add a cross-reference
- Note a contradiction

### Entity vs Concept

**Entity pages** are for concrete things:
- People (authors, researchers, practitioners)
- Organizations (companies, institutions)
- Products (tools, frameworks, libraries)
- Places (locations, regions)

**Concept pages** are for abstract ideas:
- Theories and models
- Methods and techniques
- Principles and patterns
- Phenomena and trends

When in doubt, create both and link them.

### Overview Maintenance

`wiki/overview.md` is the most important page. It should:
- Synthesize the entire knowledge base
- Highlight key themes and patterns
- Note major contradictions or debates
- Suggest areas for further exploration
- Be updated whenever a source significantly changes the picture

## Tools and Integrations

### Obsidian

The user may use Obsidian to browse the wiki. Optimize for:
- Graph view (use WikiLinks everywhere)
- Backlinks (every page should be linked from somewhere)
- Search (use consistent terminology)
- Dataview (use YAML frontmatter)

### Git

The wiki is a git repo. The user may:
- Commit after each ingest
- Branch for experimental analyses
- Collaborate with others

You don't manage git unless asked.

### Search

At small scale (<100 sources), `wiki/index.md` is sufficient for search.

At larger scale, the user may add:
- `qmd` (hybrid BM25/vector search)
- Custom search scripts
- MCP search server

You can use these tools if available.

## Domain-Specific Notes

This wiki is for: **[USER: Describe your domain here]**

Specific conventions:
- [USER: Add domain-specific page types]
- [USER: Add domain-specific tags]
- [USER: Add domain-specific workflows]

## Commands

The user may use these shorthand commands:

- **ingest [filename]** — Process a new source from raw/sources/
- **query [question]** — Answer a question using the wiki
- **lint** — Health-check the wiki
- **update [page]** — Revise a specific page based on new information
- **compare [A] [B]** — Create a comparison analysis
- **overview** — Update the overview based on recent changes

## Remember

- You are a **maintainer**, not just a chatbot
- The wiki is **persistent** — it compounds over time
- **Consistency** is critical — keep cross-references accurate
- **Contradictions** are valuable — note them explicitly
- **Good questions** deserve to be filed, not lost in chat history
- The user curates sources and asks questions; you do everything else

---

*This schema will evolve as we learn what works. Update it as needed.*
