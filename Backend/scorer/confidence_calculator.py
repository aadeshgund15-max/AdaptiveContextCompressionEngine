"""
Adaptive Context Intelligence Engine (ACIE)
Confidence Calculator Module
"""


class ConfidenceCalculator:
    """
    Calculates the confidence score for a given context.
    """

    def __init__(self):
        pass

    def calculate_confidence(self, context):
        """
        Calculate confidence score.

        Parameters:
            context (dict)

        Returns:
            float
        """

        confidence = 0.0

        # Query available
        if context.get("query"):
            confidence += 0.40

        # Conversation history available
        if len(context.get("conversation", [])) > 0:
            confidence += 0.30

        # Documents available
        if len(context.get("documents", [])) > 0:
            confidence += 0.30

        return round(confidence, 2)


if __name__ == "__main__":

    sample_context = {
        "query": "Explain adaptive context compression.",
        "conversation": [
            "What is Retrieval-Augmented Generation?"
        ],
        "documents": [
            "Research Paper 1",
            "Research Paper 2"
        ]
    }

    calculator = ConfidenceCalculator()

    confidence = calculator.calculate_confidence(sample_context)

    print("Confidence Score:", confidence)