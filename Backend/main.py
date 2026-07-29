"""
Adaptive Context Intelligence Engine (ACIE)
Main Entry Point
"""

from Backend.collector.context_collector import ContextCollector
from Backend.scorer.importance_scorer import ImportanceScorer
from Backend.scorer.confidence_calculator import ConfidenceCalculator
from Backend.decision_engine.decision_engine import DecisionEngine


def main():

    print("=" * 60)
    print("Adaptive Context Intelligence Engine (ACIE)")
    print("=" * 60)

    collector = ContextCollector()
    scorer = ImportanceScorer()
    confidence_calculator = ConfidenceCalculator()
    decision_engine = DecisionEngine()

    context = collector.collect(
        query="Explain adaptive context compression.",
        conversation=[
            "What is RAG?",
            "Explain vector databases."
        ],
        documents=[
            "Research Paper A",
            "Research Paper B"
        ]
    )

    importance = scorer.calculate_score(context)

    confidence = confidence_calculator.calculate_confidence(context)

    decision = decision_engine.decide(
        importance,
        confidence
    )

    print("\nCollected Context")
    print(context)

    print("\nImportance Score :", importance)
    print("Confidence Score :", confidence)
    print("Decision :", decision)

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()