# Database Design

# Adaptive Context Intelligence Engine (ACIE)

---

# Overview

The Adaptive Context Intelligence Engine (ACIE) requires structured storage for contextual information, metadata, decision history, and retrieval records.

The database design separates contextual data from decision metadata, making the system modular and scalable.

---

# Database Objectives

The database should:

- Store contextual information
- Maintain memory history
- Record compression decisions
- Support efficient retrieval
- Preserve explainability
- Enable adaptive forgetting

---

# Main Entities

The logical database consists of the following entities:

1. Context
2. Memory
3. Decision
4. Compression
5. Retrieval
6. User Session

---

# Entity 1 — Context

## Description

Stores raw contextual information collected from the user or external sources.

### Fields

| Field | Type | Description |
|------|------|-------------|
| ContextID | UUID | Unique identifier |
| SessionID | UUID | Associated session |
| ContextText | Text | Original context |
| Source | String | User, Document, API |
| Timestamp | DateTime | Creation time |

---

# Entity 2 — Memory

## Description

Stores processed contextual memories.

### Fields

| Field | Type | Description |
|------|------|-------------|
| MemoryID | UUID | Unique identifier |
| ContextID | UUID | Linked context |
| ImportanceScore | Integer | 0–100 |
| ConfidenceScore | Integer | 0–100 |
| CompressionStatus | String | Compressed / Original |
| LastAccessed | DateTime | Last retrieval |
| AccessCount | Integer | Number of accesses |

---

# Entity 3 — Decision

## Description

Stores every decision made by the Decision Engine.

### Fields

| Field | Type | Description |
|------|------|-------------|
| DecisionID | UUID | Unique identifier |
| MemoryID | UUID | Related memory |
| DecisionType | String | Store / Compress / Merge / Forget / Retrieve |
| Reason | Text | Explanation for decision |
| Timestamp | DateTime | Decision time |

---

# Entity 4 — Compression

## Description

Tracks compression activities.

### Fields

| Field | Type | Description |
|------|------|-------------|
| CompressionID | UUID | Unique identifier |
| MemoryID | UUID | Related memory |
| Strategy | String | Semantic / Prompt / Token / Memory |
| CompressionRatio | Float | Compression ratio |
| Timestamp | DateTime | Compression time |

---

# Entity 5 — Retrieval

## Description

Records retrieval operations.

### Fields

| Field | Type | Description |
|------|------|-------------|
| RetrievalID | UUID | Unique identifier |
| Query | Text | User query |
| RetrievedMemory | UUID | Memory returned |
| SimilarityScore | Float | Similarity value |
| RetrievalTime | DateTime | Retrieval timestamp |

---

# Entity 6 — User Session

## Description

Stores conversation session information.

### Fields

| Field | Type | Description |
|------|------|-------------|
| SessionID | UUID | Unique identifier |
| UserID | UUID | User identifier |
| StartTime | DateTime | Session start |
| EndTime | DateTime | Session end |

---

# Entity Relationships

```
User Session
      │
      ▼
Context
      │
      ▼
Memory
 ├──────────────┐
 ▼              ▼
Decision   Compression
      │
      ▼
Retrieval
```

---

# Indexing Strategy

Recommended indexes:

- ContextID
- MemoryID
- SessionID
- ImportanceScore
- ConfidenceScore
- Timestamp

These indexes improve retrieval speed and ranking performance.

---

# Future Extensions

The schema can be extended to include:

- Vector embeddings
- Multimodal context
- User preferences
- Knowledge graph links
- Multi-agent memory
- Version history

---

# Advantages

The proposed database design provides:

- Modular storage
- Explainable decisions
- Efficient retrieval
- Scalable architecture
- Support for adaptive memory management

---

# Conclusion

The database design separates context, memory, decision-making, compression, and retrieval into dedicated entities. This modular organization supports ACIE's adaptive decision layer and provides a flexible foundation for future implementations using relational, document, or vector databases.