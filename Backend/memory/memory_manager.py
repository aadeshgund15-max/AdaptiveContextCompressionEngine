"""
Adaptive Context Intelligence Engine (ACIE)
Memory Manager
"""

from datetime import datetime

from Backend.database.database import Database
from Backend.database.chroma_database import ChromaDatabase
from Backend.core.service_registry import ServiceRegistry


class MemoryManager:

    def __init__(self):

        self.sqlite = Database()

        self.chroma = ChromaDatabase()

        self.embedding_service = ServiceRegistry.get_embedding_service()

    def store(
        self,
        context,
        importance,
        confidence,
        decision,
        lifecycle=None
    ):

        if lifecycle is None:

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            lifecycle = {

                "created_at": now,

                "last_accessed": now,

                "access_count": 1,

                "state": "ACTIVE"

            }

        memory_id = self.sqlite.insert_memory(

            query=context["query"],

            importance=importance,

            confidence=confidence,

            decision=decision,

            created_at=lifecycle["created_at"],

            last_accessed=lifecycle["last_accessed"],

            access_count=lifecycle["access_count"],

            state=lifecycle["state"]

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

    def get_memory(self, memory_id):

        return self.sqlite.fetch_by_id(memory_id)

    def update_access(self, memory_id):

        memory = self.sqlite.fetch_by_id(memory_id)

        if memory is None:

            return

        access_count = memory[7] + 1

        last_accessed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.sqlite.update_access(

            memory_id,

            last_accessed,

            access_count

        )

    def update_state(self, memory_id, state):

        self.sqlite.update_state(

            memory_id,

            state

        )

    def delete_memory(self, memory_id):

        self.sqlite.delete_memory(

            memory_id

        )


if __name__ == "__main__":

    manager = MemoryManager()

    print(manager.get_all_memories())