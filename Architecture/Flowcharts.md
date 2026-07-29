# Flowcharts

# Adaptive Context Intelligence Engine (ACIE)

---

# Flowchart 1: Overall ACIE Workflow

```mermaid
flowchart TD
    A[User Query] --> B[Context Collector]
    B --> C[Context Importance Scorer]
    C --> D[Confidence Calculator]
    D --> E[Decision Engine]

    E -->|Store| F[Memory Database]
    E -->|Compress| G[Compression Engine]
    E -->|Merge| H[Merge Existing Memory]
    E -->|Forget| I[Discard Context]
    E -->|Retrieve| J[Context Retriever]

    G --> F
    H --> F

    F --> J
    J --> K[Large Language Model]
    K --> L[Final Response]
```

---

# Flowchart 2: Context Importance Scoring

```mermaid
flowchart TD
    A[Receive Context] --> B[Analyze Semantic Relevance]
    B --> C[Evaluate Recency]
    C --> D[Evaluate Frequency]
    D --> E[Evaluate Task Relevance]
    E --> F[Evaluate User Priority]
    F --> G[Generate Importance Score]
```

---

# Flowchart 3: Confidence Score Calculation

```mermaid
flowchart TD
    A[Stored Context] --> B[Check Source Reliability]
    B --> C[Check Historical Accuracy]
    C --> D[Check Retrieval Consistency]
    D --> E[Check User Confirmation]
    E --> F[Generate Confidence Score]
```

---

# Flowchart 4: Decision Engine

```mermaid
flowchart TD
    A[Context Received] --> B{Importance Score?}

    B -->|High| C[Store Memory]

    B -->|Medium| D[Compress]

    B -->|Low| E{Confidence Score?}

    E -->|Low| F[Forget]

    E -->|High| G[Merge with Existing Memory]

    C --> H[Memory Database]
    D --> H
    G --> H
```

---

# Flowchart 5: Adaptive Forgetting

```mermaid
flowchart TD
    A[Stored Memory] --> B[Check Age]
    B --> C[Check Importance]
    C --> D[Check Confidence]
    D --> E{Forget?}

    E -->|Yes| F[Delete Memory]

    E -->|No| G[Keep Memory]
```

---

# Flowchart 6: Memory Retrieval

```mermaid
flowchart TD
    A[User Query] --> B[Similarity Search]
    B --> C[Importance Ranking]
    C --> D[Confidence Ranking]
    D --> E[Recency Ranking]
    E --> F[Top-K Memory Selection]
    F --> G[LLM]
```

---

# Flowchart 7: Compression Strategy Selection

```mermaid
flowchart TD
    A[Context] --> B{Context Type}

    B -->|Short| C[Semantic Compression]

    B -->|Conversation| D[Memory Compression]

    B -->|Prompt| E[Prompt Compression]

    B -->|Document| F[Token Compression]

    C --> G[Compressed Output]
    D --> G
    E --> G
    F --> G
```

---

# Summary

These flowcharts illustrate the complete processing pipeline of the Adaptive Context Intelligence Engine (ACIE), including context evaluation, adaptive decision-making, memory management, retrieval, and compression strategy selection. They provide a high-level visual representation of the system architecture and support the algorithmic descriptions presented in the accompanying documentation.
