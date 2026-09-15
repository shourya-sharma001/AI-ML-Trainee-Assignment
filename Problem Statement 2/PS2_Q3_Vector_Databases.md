# Problem Statement 2 — Question 3

**Question:** Please explain vector databases. If you were to select a vector database for a hypothetical problem (you may define the problem) which one will you choose, and why?

---

## What is a Vector Database?

A vector database is built to store and search embeddings — numerical representations of data (text, images, audio, whatever) that capture the underlying meaning rather than the raw content itself. A regular database like SQLite matches things exactly — `WHERE title = 'Harry Potter'` only works if the title matches exactly. A vector database instead finds things that are *similar* in meaning, even when the wording is completely different.

This is really what makes them useful for AI systems — they let you search based on meaning instead of exact keywords.

---

## How Similarity Gets Determined

When something gets stored, it first passes through a machine learning model that turns it into an embedding. To compare two embeddings, the database uses similarity techniques (cosine similarity being the common one) to figure out how close they are — closer meaning more similar. That's what makes "find me something similar to this" possible, which a plain keyword search just can't do.

---

## Types of Vector Databases

These roughly fall into three buckets:

**Dedicated, purpose-built vector databases** — built from scratch specifically for storing and searching embeddings at scale:
- Qdrant — open-source, written in Rust, can be self-hosted, focused on speed
- Pinecone — fully managed, easy to set up, but not self-hosted
- Weaviate — open-source, supports hybrid search (keyword + vector together)
- Milvus — open-source, meant for very large-scale similarity search

**Vector search libraries** — not full databases, just libraries offering fast similarity-search algorithms, leaving things like persistence and access control up to you:
- FAISS (Facebook AI Similarity Search) — fast, good for smaller projects or experimentation

**Traditional databases with vector-search bolted on** — useful if a team doesn't want to introduce a whole new piece of infrastructure:
- PostgreSQL with the `pgvector` extension
- Elasticsearch, which now supports vector search alongside its usual keyword search

---

## Hypothetical Problem

In QA teams, it's common to run into a bug that feels familiar — like something you've seen before on a past project — but you can't quite place where or when. Bug trackers usually rely on keyword search, so if you don't use the exact terminology from an old report, you can easily miss a relevant fix that already exists, even if the underlying issue is basically the same.

This is especially relevant for a company like AccuKnox, given that its core product, KubeArmor, and the broader Zero Trust CNAPP platform involve fast-moving, fairly technical documentation — runtime policy enforcement, container security configs, Kubernetes-specific behavior, and so on. Engineers working across a platform like that would regularly need to pull up old bug reports and incident resolutions where the terminology used can vary a lot even when describing the same underlying issue.

For example, someone testing KubeArmor's policy enforcement might log a bug as "policy not blocking a process in a specific namespace," while an older, already-resolved report described the same root issue as "AppArmor profile not applying to a pod's runtime." Different words, same bug — a keyword search would completely miss the connection.

**Proposed solution:** Convert internal bug reports, KubeArmor documentation, and past incident resolutions into embeddings and store them in a vector database. An engineer could then describe a new issue in their own words and get back semantically similar past reports, regardless of the exact terminology used. It would cut down on duplicate investigation and help newer engineers get up to speed faster on KubeArmor and CNAPP-specific issues.

## Chosen Vector Database: Qdrant

I'd go with Qdrant here:

1. **Open-source and self-hostable** — bug reports can reference internal product details, so keeping that data on infrastructure the company controls, rather than a third-party managed service, makes sense.
2. **Performance** — it's written in Rust, so it stays fast and memory-efficient even as the volume of historical reports grows.
3. **Relevance to AccuKnox** — Qdrant is explicitly called out as a bonus skill in the job description, which suggests it's already part of the stack the team is exploring.
4. **Filtering support** — Qdrant supports metadata filtering (say, narrowing results to a specific product like KubeArmor, or a specific time range), which would help for a knowledge-retrieval tool spanning multiple products and teams.

---

## Flow

```
Past Bug Reports (with resolutions)
        |
        v
  Text Chunking / Preparation
        |
        v
  Embedding Model
        |
        v
  Stored in Qdrant


[New bug encountered]
        |
        v
  Bug Description --> Embedding Model
        |
        v
  Similarity Search against stored embeddings
        |
        v
  Most similar past reports retrieved
        |
        v
  Engineer reviews and applies the past resolution
```
