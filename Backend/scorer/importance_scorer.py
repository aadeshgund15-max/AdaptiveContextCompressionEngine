"""
Adaptive Context Intelligence Engine (ACIE)
Importance Scorer Module
"""


class ImportanceScorer:
    """
    Calculates the importance score of a given context.
    """

    def __init__(self):
        pass

    def calculate_score(self, context):
        """
        Calculate an importance score.

        Parameters:
            context (dict)

        Returns:
            int
        """

        score = 0

        # Query length
        query = context.get("query", "")
        score += min(len(query), 30)

        # Conversation history
        conversation = context.get("conversation", [])
        score += len(conversation) * 10

        # Documents
        documents = context.get("documents", [])
        score += len(documents) * 15

        # Maximum score = 100
        if score > 100:
            score = 100

        return score


if __name__ == "__main__":

    sample_context = {
        "query": "Explain semantic context compression.",
        "conversation": [
            "What is RAG?",
            "Explain vector databases."
        ],
        "documents": [
            "Paper 1",
            "Paper 2",
            "Paper 3"
        ]
    }

    scorer = ImportanceScorer()

    score = scorer.calculate_score(sample_context)

    print("Importance Score:", score)