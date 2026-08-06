"""
Adaptive Context Intelligence Engine (ACIE)
Decision Engine Module
"""


class DecisionEngine:
    """
    Determines what action should be taken for the given context.
    """

    def __init__(self):
        pass

    def decide(self, importance_score, confidence_score):
        """
        Make a decision based on importance and confidence.

        Parameters:
            importance_score (int)
            confidence_score (float)

        Returns:
            str
        """

        return "STORE"

if __name__ == "__main__":

    engine = DecisionEngine()

    importance = 85
    confidence = 0.90

    decision = engine.decide(importance, confidence)

    print("Importance Score :", importance)
    print("Confidence Score :", confidence)
    print("Decision :", decision)