# LLM Wiki Setup

A persistent, LLM-maintained knowledge base following the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by Andrej Karpathy.

## What is This?

This is **not** a traditional RAG system. Instead of retrieving from raw documents on every query, an LLM incrementally builds and maintains a **persistent wiki** — a structured, interlinked collection of markdown files that compounds over time.

### Key Differences from RAG

- **RAG:** Retrieves chunks → synthesizes answer → forgets everything
- **LLM Wiki:** Reads source → integrates into wiki → knowledge persists

The wiki is a **compounding artifact**. Cross-references are already there. Contradictions are already flagged. The synthesis already reflects everything you've read.

## Directory Structure

```
.
├── AGENTS.md              # Schema: how the LLM should maintain the wiki
├── README.md              # This file
├── raw/                   # Your source materials (immutable)
│   ├── sources/          # Documents, articles, papers, data
│   └── assets/           # Images, diagrams, media
├── wiki/                  # LLM-maintained knowledge base
│   ├── index.md          # Content catalog
│   ├── log.md            # Chronological record
│   ├── overview.md       # High-level synthesis
│   ├── entities/         # People, organizations, products
│   ├── concepts/         # Ideas, theories, methods
│   ├── sources/          # One summary per raw source
│   ├── analyses/         # Comparisons, deep-dives
│   └── queries/          # Preserved answers
└── tools/                 # Optional helper scripts
    └── ingest-helper.md  # Ingestion workflow guide
```

## Quick Start

### 1. Initialize (Already Done!)

The wiki structure is already set up and ready to use.

### 2. Add Your First Source

Place a document in `raw/sources/`:

```bash
# Example: download an article
curl -o raw/sources/my-article.md "https://example.com/article"

# Or: copy a file
cp ~/Documents/paper.pdf raw/sources/
```

### 3. Ingest the Source

Tell your LLM agent:

```
ingest my-article.md
```

The LLM will:
1. Read the source
2. Discuss key takeaways with you
3. Create a summary in `wiki/sources/`
4. Extract and create entity pages
5. Extract and create concept pages
6. Add cross-references
7. Update the index and log
8. Update the overview if significant

### 4. Query the Wiki

Ask questions:

```
query: What are the main themes across all sources?
query: How does [concept A] relate to [concept B]?
query: What do we know about [entity]?
```

The LLM will search the wiki, synthesize an answer with citations, and optionally file the answer as a new page.

### 5. Maintain the Wiki

Periodically run:

```
lint
```

The LLM will check for:
- Contradictions between pages
- Stale claims
- Orphan pages
- Missing cross-references
- Suggested new sources or questions

## Commands

Your LLM agent understands these shorthand commands:

- **`ingest [filename]`** — Process a new source from `raw/sources/`
- **`query [question]`** — Answer a question using the wiki
- **`lint`** — Health-check the wiki
- **`update [page]`** — Revise a specific page
- **`compare [A] [B]`** — Create a comparison analysis
- **`overview`** — Update the overview based on recent changes

## Workflow Tips

### Ingestion Style

**Recommended:** One source at a time with your involvement
- Read the summary
- Check the updates
- Guide what to emphasize

**Alternative:** Batch-ingest many sources with less supervision

Document your preferred style in `AGENTS.md`.

### Good Answers Should Be Filed

When you ask a good question and get a good answer, file it in the wiki:
- Comparisons → `wiki/analyses/`
- Specific queries → `wiki/queries/`

This way your explorations compound in the knowledge base.

### Contradictions Are Valuable

When sources contradict each other:
1. Note it explicitly in both source summaries
2. Create a comparison page in `wiki/analyses/`
3. Update `wiki/overview.md` if significant

Don't hide contradictions — they're often the most interesting part.

### Use WikiLinks Everywhere

Always use `[[page-name]]` format for internal links. This enables:
- Obsidian graph view
- Easy refactoring
- Backlink tracking

## Tools and Integrations

### Obsidian (Recommended)

Open this directory in Obsidian to browse the wiki with:
- **Graph view** — See connections between pages
- **Backlinks** — See what links to each page
- **Search** — Find content across all pages
- **Dataview** — Query page metadata

### Obsidian Web Clipper

Browser extension that converts web articles to markdown:
1. Install the extension
2. Clip articles directly to `raw/sources/`
3. Ingest them into the wiki

### Git

The wiki is just markdown files. You can:
- Commit after each ingest
- Branch for experimental analyses
- Collaborate with others
- Track version history

```bash
git init
git add .
git commit -m "Initial wiki setup"
```

### Search Tools (Optional)

At small scale (<100 sources), `wiki/index.md` is sufficient.

At larger scale, consider:
- **qmd** — Hybrid BM25/vector search for markdown
- Custom search scripts
- MCP search server

## Example: Ingesting the Example Source

An example source is already in `raw/sources/example-llm-wiki-pattern.md`.

Try ingesting it:

```
ingest example-llm-wiki-pattern.md
```

The LLM will create:
- `wiki/sources/llm-wiki-pattern.md` — Summary
- `wiki/entities/andrej-karpathy.md` — Entity page
- `wiki/concepts/llm-wiki-pattern.md` — Concept page
- `wiki/concepts/rag.md` — Concept page
- Cross-references between all pages
- Updated index and log

Then try querying:

```
query: What is the difference between RAG and the LLM Wiki pattern?
```

## Customization

### Domain-Specific Setup

Edit `AGENTS.md` to add:
- Domain-specific page types
- Domain-specific tags
- Domain-specific workflows
- Preferred ingestion style

### Page Templates

Modify the templates in `AGENTS.md`:
- Source summary format
- Entity page format
- Concept page format
- Analysis page format

### Directory Structure

Add subdirectories as needed:
- `wiki/timelines/` — Chronological views
- `wiki/comparisons/` — Side-by-side comparisons
- `wiki/visualizations/` — Charts and diagrams

Document changes in `AGENTS.md`.

## Philosophy

### Division of Labor

**Your job:**
- Curate sources
- Direct analysis
- Ask good questions
- Think about meaning

**LLM's job:**
- Summarizing
- Cross-referencing
- Filing
- Bookkeeping
- Maintaining consistency

### Why This Works

The tedious part of maintaining a knowledge base is bookkeeping. Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

### Persistent vs Ephemeral

Traditional chat with LLMs is ephemeral — every conversation starts from scratch. This wiki is persistent — knowledge compounds over time. The more you use it, the more valuable it becomes.

## Inspiration

This pattern is inspired by:
- **Vannevar Bush's Memex (1945)** — Personal knowledge store with associative trails
- **Zettelkasten** — Slip-box method for note-taking
- **Personal wikis** — Obsidian, Roam, TiddlyWiki
- **Fan wikis** — Tolkien Gateway, Wookieepedia

The part these systems couldn't solve was maintenance. The LLM handles that.

## Next Steps

1. **Add your first real source** to `raw/sources/`
2. **Ingest it** with your LLM agent
3. **Browse the results** in Obsidian or your text editor
4. **Ask questions** and file good answers
5. **Keep adding sources** and watch the wiki grow

## Resources

- [Original LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by Andrej Karpathy
- [Obsidian](https://obsidian.md/) — Recommended wiki browser
- [qmd](https://github.com/example/qmd) — Optional search tool
- [Marp](https://marp.app/) — Markdown presentations

## Support

This is a pattern, not a product. Customize it to fit your needs. The `AGENTS.md` file is your configuration — evolve it as you learn what works.

---

**Status:** Initialized and ready for first source ingest.

**Last updated:** 2026-07-07
