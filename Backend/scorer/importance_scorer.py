"""
Adaptive Context Intelligence Engine (ACIE)
Importance Scorer Module
"""


class ImportanceScorer:
    """
    Calculates the importance score of a context.
    """

    def __init__(self):
        pass

    def calculate_score(self, context):
        """
        Calculate importance score.

        Returns:
            int (0 - 100)
        """

        score = 0

        # -------------------------
        # Query Length
        # -------------------------
        query = context.get("query", "")

        if len(query) > 15:
            score += 25
        elif len(query) > 5:
            score += 15

        # -------------------------
        # Conversation History
        # -------------------------
        conversation = context.get("conversation", [])

        score += min(len(conversation) * 10, 30)

        # -------------------------
        # Documents
        # -------------------------
        documents = context.get("documents", [])

        score += min(len(documents) * 10, 20)

        # -------------------------
        # Bonus Keywords
        # -------------------------
        keywords = [
            "context",
            "compression",
            "embedding",
            "retrieval",
            "semantic",
            "memory",
            "database",
            "vector",
            "rag",
            "agent"
        ]

        lower_query = query.lower()

        for word in keywords:
            if word in lower_query:
                score += 5

        # Maximum Score = 100
        score = min(score, 100)

        return score


if __name__ == "__main__":

    scorer = ImportanceScorer()

    sample_context = {
        "query": "Explain vector databases",
        "conversation": [
            "What is semantic search?",
            "How are embeddings created?"
        ],
        "documents": [
            "Research Paper A",
            "Research Paper B"
        ]
    }

    importance = scorer.calculate_score(sample_context)

    print("Importance Score :", importance)