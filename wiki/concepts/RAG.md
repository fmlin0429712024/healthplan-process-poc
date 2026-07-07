---
tags: [llm, retrieval, generation, ai]
date: 2026-07-07
type: concept
---

# RAG (Retrieval-Augmented Generation)

**Type:** AI Architecture/Method
**Domain:** Natural Language Processing

## Summary

Retrieval-Augmented Generation (RAG) is an AI architecture that enhances large language models by retrieving relevant information from external knowledge sources before generating responses. Unlike the [[LLM-Wiki-Pattern]], traditional RAG systems retrieve and synthesize information from scratch on every query.

## How It Works

1. **Query Processing:** User submits a question or prompt
2. **Retrieval:** System searches a knowledge base for relevant documents
3. **Context Assembly:** Retrieved documents are assembled as context for the LLM
4. **Generation:** LLM generates a response based on the retrieved context
5. **Response Returned:** Answer is provided to the user

## Key Characteristics

**Ephemeral Processing:** Each query starts fresh — the system doesn't maintain persistent knowledge structures between queries. The retrieval and synthesis happen independently for each question.

**Direct Source Access:** The system works directly with raw source documents rather than with pre-processed summaries or structured knowledge.

**Scalability:** Can handle large document collections without manual curation, as retrieval is automated.

## Comparison with LLM Wiki Pattern

| Aspect | RAG | LLM Wiki Pattern |
|--------|-----|------------------|
| Knowledge persistence | Ephemeral (per query) | Persistent (wiki) |
| Processing approach | Retrieve from scratch | Incremental updates |
| Knowledge structure | Raw sources | Structured summaries |
| Maintenance burden | Low (automated retrieval) | Near zero (LLM maintenance) |
| Cross-references | Rebuilt each query | Maintained persistently |
| Contradiction tracking | Per query only | Tracked over time |

## Advantages

- **No manual curation:** Works with raw documents directly
- **Scalable:** Can handle large document collections
- **Fresh retrieval:** Always uses the most recent source versions
- **Simple setup:** Less configuration than structured wikis

## Limitations

- **No persistent synthesis:** Insights aren't accumulated over time
- **Repetitive processing:** Same documents may be retrieved repeatedly
- **Limited context:** Constrained by retrieval window and context length
- **No contradiction tracking:** Can't maintain awareness of conflicts across sources

## Related Pages

- [[LLM-Wiki-Pattern]] — Alternative approach with persistent knowledge maintenance
- [[llm-wiki-pattern-karpathy]] — Source document comparing the approaches