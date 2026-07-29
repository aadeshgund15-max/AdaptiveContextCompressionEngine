"""
Adaptive Context Intelligence Engine (ACIE)
Main Entry Point
"""

from Backend.collector.context_collector import ContextCollector
from Backend.scorer.importance_scorer import ImportanceScorer
from Backend.scorer.confidence_calculator import ConfidenceCalculator
from Backend.decision_engine.decision_engine import DecisionEngine
from Backend.memory.memory_manager import MemoryManager
from Backend.retriever.retriever import Retriever


def main():

    print("=" * 60)
    print("Adaptive Context Intelligence Engine (ACIE)")
    print("=" * 60)

    collector = ContextCollector()
    scorer = ImportanceScorer()
    confidence_calculator = ConfidenceCalculator()
    decision_engine = DecisionEngine()
    memory_manager = MemoryManager()
    retriever = Retriever()

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

    importance = scorer.calculate_score(context)
    confidence = confidence_calculator.calculate_confidence(context)

    decision = decision_engine.decide(
        importance,
        confidence
    )

    if decision == "STORE":

        memory_id = memory_manager.store(
            context,
            importance,
            confidence,
            decision
        )

        print("\nMemory stored successfully.")
        print("Memory ID :", memory_id)

    print("\nCollected Context")
    print(context)

    print("\nImportance Score :", importance)
    print("Confidence Score :", confidence)
    print("Decision :", decision)

    print("\nSQLite Memories")

    for memory in memory_manager.get_all_memories():
        print(memory)

    print("\nKeyword Retrieval")

    results = retriever.retrieve("compression")

    for item in results:
        print(item)

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()