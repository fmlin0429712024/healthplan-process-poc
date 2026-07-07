# Quick Start Guide

## 30-Second Start

1. **Add a source:** Place a file in `raw/sources/`
2. **Ingest it:** Tell your LLM agent: `ingest [filename]`
3. **Browse:** Open `wiki/` in Obsidian or your editor
4. **Query:** Ask questions: `query: [your question]`

## Commands Cheat Sheet

```bash
# Ingestion
ingest [filename]          # Process a new source
ingest [filename] --batch  # Process without discussion

# Querying
query: [question]          # Answer using the wiki
compare [A] [B]           # Create comparison analysis

# Maintenance
lint                      # Health-check the wiki
update [page]            # Revise a specific page
overview                 # Update the big picture

# Navigation
show index               # View the content catalog
show log                 # View recent operations
show overview           # View the synthesis
```

## First Session Example

```
You: I've added a paper to raw/sources/transformer-paper.pdf

Agent: I'll ingest it. Let me read the paper first...

[Agent reads the paper]

Agent: This is the "Attention Is All You Need" paper by Vaswani et al. 
Key takeaways:
- Introduces the Transformer architecture
- Replaces recurrence with self-attention
- Achieves state-of-the-art on translation tasks

Should I emphasize any particular aspects?

You: Focus on the self-attention mechanism and how it differs from RNNs.

Agent: Got it. Processing...

[Agent creates pages]

Agent: Done! Created:
- wiki/sources/attention-is-all-you-need.md
- wiki/entities/vaswani.md (and 7 other authors)
- wiki/concepts/transformer-architecture.md
- wiki/concepts/self-attention.md
- wiki/concepts/multi-head-attention.md
- Updated wiki/index.md and wiki/log.md

You can browse the results in wiki/. Would you like me to update the overview?

You: Yes, update the overview.

Agent: Updated wiki/overview.md to reflect that we're building knowledge 
around neural network architectures, specifically attention mechanisms.

You: query: How does self-attention work?

Agent: Based on [[attention-is-all-you-need]], self-attention computes...
[detailed answer with citations]

Should I file this answer in the wiki?

You: Yes, save it.

Agent: Created wiki/queries/how-self-attention-works.md
```

## File Structure at a Glance

```
raw/sources/          ← You put files here
wiki/                 ← LLM maintains this
  ├── index.md       ← Start here to navigate
  ├── overview.md    ← Big picture synthesis
  ├── sources/       ← One summary per source
  ├── entities/      ← People, orgs, products
  └── concepts/      ← Ideas, methods, theories
```

## Tips

### For Ingestion
- One source at a time = more control
- Batch ingestion = faster but less precise
- Always review the summary page

### For Queries
- Start with `show index` to see what's available
- Good answers should be filed in the wiki
- Use `compare` for side-by-side analysis

### For Maintenance
- Run `lint` every 10-20 sources
- Fix contradictions as they're found
- Update `overview` when themes shift

## Common Workflows

### Research Deep-Dive
1. Collect 10-20 papers/articles on a topic
2. Ingest them one by one
3. Run `lint` to find gaps
4. Query to synthesize findings
5. Create analysis pages for key comparisons

### Book Reading
1. Add each chapter as a source
2. Ingest as you read
3. Entity pages = characters
4. Concept pages = themes
5. End with a rich companion wiki

### Team Knowledge Base
1. Add meeting notes, docs, Slack threads
2. Ingest regularly (daily/weekly)
3. Query for "what's the status of X?"
4. Lint to keep it current
5. Team browses in Obsidian

## Troubleshooting

**Q: The LLM isn't following the schema**
- Make sure AGENTS.md is in the project root
- Remind the LLM: "Follow the schema in AGENTS.md"
- Update AGENTS.md with specific instructions

**Q: Too many entity pages**
- Adjust the threshold in AGENTS.md
- Only create pages for significant entities
- Merge minor entities into source summaries

**Q: Can't find information**
- Check wiki/index.md first
- Use Obsidian search
- Run a query to synthesize across pages

**Q: Contradictions between sources**
- This is valuable! Don't hide them
- Create a comparison page
- Note them in the overview

## Next Steps

1. Try the example: `ingest example-llm-wiki-pattern.md`
2. Add your own source
3. Query it
4. Watch the wiki grow

See README.md for full documentation.
