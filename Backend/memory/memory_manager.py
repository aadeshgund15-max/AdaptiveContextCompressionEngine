"""
Adaptive Context Intelligence Engine (ACIE)
Memory Manager
"""

from Backend.database.database import Database
from Backend.database.chroma_database import ChromaDatabase
from Backend.services.embedding_service import EmbeddingService


class MemoryManager:

    def __init__(self):

        self.sqlite = Database()
        self.chroma = ChromaDatabase()
        self.embedding_service = EmbeddingService()

    def store(self, context, importance, confidence, decision):

        memory_id = self.sqlite.insert_memory(
            context["query"],
            importance,
            confidence,
            decision
        )

        embedding = self.embedding_service.generate_embedding(
            context["query"]
        )

        self.chroma.add_memory(
            memory_id,
            context["query"],
            embedding
        )

        return memory_id

    def get_all_memories(self):

        return self.sqlite.fetch_all()