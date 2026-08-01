"""
Adaptive Context Intelligence Engine (ACIE)
Memory Pipeline
"""

from Backend.collector.context_collector import ContextCollector
from Backend.scorer.importance_scorer import ImportanceScorer
from Backend.scorer.confidence_calculator import ConfidenceCalculator
from Backend.decision_engine.decision_engine import DecisionEngine

from Backend.memory.memory_manager import MemoryManager

from Backend.compressor.context_compressor import ContextCompressor
from Backend.summarizer.memory_summarizer import MemorySummarizer

from Backend.context_builder.context_window_builder import ContextWindowBuilder

from Backend.reflection.reflection_engine import ReflectionEngine

from Backend.knowledge.graph_builder import GraphBuilder

from Backend.graph_retriever.graph_retriever import GraphRetriever

from Backend.episodic.episodic_memory import EpisodicMemory

from Backend.working_memory.working_memory import WorkingMemory
from Backend.consolidation.memory_consolidation import MemoryConsolidation



class MemoryPipeline:

    def __init__(self):

        self.collector = ContextCollector()

        self.importance_scorer = ImportanceScorer()

        self.confidence_calculator = ConfidenceCalculator()

        self.decision_engine = DecisionEngine()

        self.memory_manager = MemoryManager()

        self.compressor = ContextCompressor()

        self.summarizer = MemorySummarizer()

        self.context_builder = ContextWindowBuilder()

        self.reflection_engine = ReflectionEngine()

        self.graph_builder = GraphBuilder()

        self.graph_retriever = GraphRetriever()

        self.episodic_memory = EpisodicMemory()

        self.working_memory = WorkingMemory()

        self.memory_consolidation = MemoryConsolidation()

    def process(

        self,

        query,

        conversation,

        documents

    ):

        print("\n========== ACIE MEMORY PIPELINE ==========\n")

        # ---------------------------------
        # Context Collection
        # ---------------------------------

        context = self.collector.collect(

            query=query,

            conversation=conversation,

            documents=documents

        )

        # ---------------------------------
        # Working Memory
        # ---------------------------------

        self.working_memory.add_context(

            query=query,

            importance=0,

            source="user"

        )

        # ---------------------------------
        # Scoring
        # ---------------------------------

        importance = self.importance_scorer.calculate_score(

            context

        )

        confidence = self.confidence_calculator.calculate_confidence(

            context

        )

        # ---------------------------------
        # Decision
        # ---------------------------------

        decision = self.decision_engine.decide(

            importance,

            confidence

        )

        # ---------------------------------
        # Store Memory
        # ---------------------------------

        memory_id = None

        if decision == "STORE":

            memory_id = self.memory_manager.store(

                context,

                importance,

                confidence,

                decision

            )

        # ---------------------------------
        # Read SQLite Memories
        # ---------------------------------

        memories = self.memory_manager.get_all_memories()

        texts = []

        reflection_memories = []

        for memory in memories:

            texts.append(memory[1])

            reflection_memories.append({

                "id": memory[0],

                "query": memory[1],

                "importance": memory[2],

                "confidence": memory[3],

                "decision": memory[4],

                "created_at": memory[5],

                "last_accessed": memory[6],

                "access_count": memory[7],

                "state": memory[8]

            })

        # ---------------------------------
        # Memory Consolidation
        # ---------------------------------

        consolidated_memories = self.memory_consolidation.consolidate(

            reflection_memories

        )

        # ---------------------------------
        # Compression
        # ---------------------------------

        texts = []

        for memory in consolidated_memories:

            texts.append(

                memory["query"]

            )

        compression = self.compressor.compress(

            texts

        )

        # ---------------------------------
        # Summary
        # ---------------------------------

        summary = self.summarizer.summarize(

            compression["compressed_memories"]

        )

        # ---------------------------------
        # Reflection
        # ---------------------------------

        reflection = self.reflection_engine.generate_report(

            consolidated_memories

        )

        # ---------------------------------
        # Knowledge Graph
        # ---------------------------------

        graph = self.graph_builder.build(

            consolidated_memories

        )

        graph_statistics = self.graph_builder.statistics()

        # ---------------------------------
        # Graph Retrieval
        # ---------------------------------

        graph_results = self.graph_retriever.retrieve(

            query,

            consolidated_memories,

            top_k=5

        )

        expanded_memories = graph_results["expanded_memories"]

        ranking = []

        for memory in expanded_memories:

            ranking.append({

                "text": memory["query"],

                "ranking_score": memory["importance"]

            })

        # ---------------------------------
        # Context Window
        # ---------------------------------

        context_window = self.context_builder.build(

            ranking,

            token_budget=100

        )

        # ---------------------------------
        # Episodic Memory
        # ---------------------------------

        episode = self.episodic_memory.create_episode(

            query=query,

            conversation=conversation,

            documents=documents,

            importance=importance,

            confidence=confidence,

            decision=decision,

            outcome=(

                "Memory Stored"

                if memory_id is not None

                else "Memory Not Stored"

            )

        )

        # ---------------------------------
        # Return
        # ---------------------------------

        return {

            "memory_id": memory_id,

            "importance": importance,

            "confidence": confidence,

            "decision": decision,

            "working_memory": self.working_memory.get_recent_context(),

            "episode": episode,

            "consolidated_memories": consolidated_memories,

            "compression": compression,

            "summary": summary,

            "reflection": reflection,

            "knowledge_graph": {

                "nodes": graph_statistics["nodes"],

                "relationships": graph_statistics["relationships"]

            },

            "graph_retrieval": graph_results,

            "context_window": context_window

        }


if __name__ == "__main__":

    pipeline = MemoryPipeline()

    result = pipeline.process(

        query="Explain adaptive context compression.",

        conversation=[

            "What is semantic search?",

            "Explain embeddings."

        ],

        documents=[

            "Research Paper A",

            "Research Paper B"

        ]

    )

    print("\n========== PIPELINE RESULT ==========\n")

    print(result)