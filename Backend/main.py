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

    # Initialize modules
    collector = ContextCollector()
    scorer = ImportanceScorer()
    confidence_calculator = ConfidenceCalculator()
    decision_engine = DecisionEngine()
    memory_manager = MemoryManager()
    retriever = Retriever()

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

    # Decision
    decision = decision_engine.decide(
        importance,
        confidence
    )

    # Store memory if required
    if decision == "STORE":
        memory_manager.store(
            context,
            importance,
            confidence,
            decision
        )

    # Display collected context
    print("\nCollected Context")
    print(context)

    # Display scores
    print("\nImportance Score :", importance)
    print("Confidence Score :", confidence)
    print("Decision :", decision)

    # Display all stored memories
    print("\nStored Memories")

    memories = memory_manager.get_all_memories()

    if len(memories) == 0:
        print("No memories stored.")

    else:
        for memory in memories:
            print(memory)

    # Retrieve memories using keyword search
    print("\nRetrieved Memories")

    keyword = "compression"

    retrieved = retriever.retrieve(keyword)

    if len(retrieved) == 0:
        print("No matching memories found.")

    else:
        for memory in retrieved:
            print(memory)

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()