# Ingest Helper Guide

This document guides the LLM through the ingestion workflow.

## When to Use

When the user says:
- "ingest [filename]"
- "process the new source"
- "add this to the wiki"

## Standard Ingestion Flow

### Step 1: Read the Source

Read the file from `raw/sources/[filename]`

### Step 2: Discuss with User

Present key takeaways:
- Main topic/thesis
- Key entities (people, organizations, products)
- Key concepts (ideas, methods, frameworks)
- Notable data points or claims
- Potential contradictions with existing wiki content

Ask the user:
- What should be emphasized?
- Any specific aspects to focus on?
- Should this update the overview?

### Step 3: Create Source Summary

Create `wiki/sources/[source-name].md` following the template in AGENTS.md

### Step 4: Update/Create Entity Pages

For each significant entity mentioned:
- Check if `wiki/entities/[entity-name].md` exists
- If yes, add a section or bullet point about this source
- If no, create a new entity page

Entity page template:
```markdown
# [Entity Name]

**Type:** Person | Organization | Product | Place
**First mentioned:** [[source-name]]

## Overview

[Brief description]

## Mentions in Sources

### [[source-name]]

[How this entity is discussed in this source]

## Related Pages

- [[concept-name]] — Connection
- [[other-entity]] — Relationship
```

### Step 5: Update/Create Concept Pages

For each significant concept:
- Check if `wiki/concepts/[concept-name].md` exists
- If yes, add information from this source
- If no, create a new concept page

Concept page template:
```markdown
# [Concept Name]

**Category:** Theory | Method | Pattern | Phenomenon
**First mentioned:** [[source-name]]

## Definition

[Clear definition]

## Key Ideas

- Point 1
- Point 2
- Point 3

## Sources

### [[source-name]]

[How this source discusses this concept]

## Related Concepts

- [[related-concept]] — Connection
```

### Step 6: Add Cross-References

Update existing pages that should reference this new source:
- Add links from related entity pages
- Add links from related concept pages
- Add links from related source pages

### Step 7: Update Index

Update `wiki/index.md`:
- Add new source to Sources section
- Add new entities to Entities section
- Add new concepts to Concepts section
- Update stats at bottom

### Step 8: Update Log

Append to `wiki/log.md`:
```markdown
## [YYYY-MM-DD HH:MM] ingest | [Source Title]

- Created [[source-name]]
- Created [[entity-1]], [[entity-2]] (if new)
- Updated [[entity-3]] (if existing)
- Created [[concept-1]], [[concept-2]] (if new)
- Updated [[concept-3]] (if existing)
- Added N cross-references
```

### Step 9: Update Overview (if significant)

If this source significantly changes the big picture:
- Update `wiki/overview.md`
- Add to key themes
- Note any contradictions
- Update suggested next steps

### Step 10: Confirm with User

Show the user:
- Link to the new source summary
- List of pages created/updated
- Any contradictions or questions noted
- Suggested next sources or queries

## Example Session

```
User: ingest example-llm-wiki-pattern.md