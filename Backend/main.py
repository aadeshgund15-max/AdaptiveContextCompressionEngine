"""
Adaptive Context Intelligence Engine (ACIE)
Main Entry Point
"""

from Backend.collector.context_collector import ContextCollector
from Backend.scorer.importance_scorer import ImportanceScorer
from Backend.scorer.confidence_calculator import ConfidenceCalculator
from Backend.decision_engine.decision_engine import DecisionEngine
from Backend.memory.memory_manager import MemoryManager


def main():

    print("=" * 60)
    print("Adaptive Context Intelligence Engine (ACIE)")
    print("=" * 60)

    # Initialize all modules
    collector = ContextCollector()
    scorer = ImportanceScorer()
    confidence_calculator = ConfidenceCalculator()
    decision_engine = DecisionEngine()
    memory_manager = MemoryManager()

    # Collect context
    context = collector.collect(
        query="Explain adaptive context compression.",
        conversation=[
            "What is Retrieval-Augmented Generation?",
            "Explain vector databases."
        ],
        documents=[
            "Research Paper A",
            "Research Paper B"
        ]
    )

    # Calculate importance
    importance = scorer.calculate_score(context)

    # Calculate confidence
    confidence = confidence_calculator.calculate_confidence(context)

    # Make decision
    decision = decision_engine.decide(
        importance,
        confidence
    )

    # Store in memory if needed
    if decision == "STORE":
        memory_manager.store(
            context,
            importance,
            confidence,
            decision
        )

    # Display results
    print("\nCollected Context")
    print(context)

    print("\nImportance Score :", importance)
    print("Confidence Score :", confidence)
    print("Decision :", decision)

    print("\nStored Memories")
    memories = memory_manager.get_all_memories()

    if len(memories) == 0:
        print("No memories stored.")
    else:
        for memory in memories:
            print(memory)

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()