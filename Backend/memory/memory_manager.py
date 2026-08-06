"""
Adaptive Context Intelligence Engine (ACIE)
Memory Manager
"""

from datetime import datetime

from Backend.database.database import Database
from Backend.database.chroma_database import ChromaDatabase
from Backend.core.service_registry import ServiceRegistry
from Backend.data_structures.linked_list import LinkedList
from Backend.data_structures.hash_table import HashTable


class MemoryManager:

    def __init__(self):

        self.sqlite = Database()

        self.chroma = ChromaDatabase()

        self.conversation_history = LinkedList()

        self.memory_cache = HashTable()

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

        print("=" * 60)
        print("Memory ID:", memory_id)
        print("Current database contents:")
        print(self.sqlite.fetch_all())
        print("=" * 60)

        self.conversation_history.append(
            context["query"],
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

        self.memory_cache.insert(
            memory_id,
            {
                "query": context["query"],
                "importance": importance,
                "confidence": confidence,
                "decision": decision
            }
        )

        return memory_id

    def get_all_memories(self):

        return self.sqlite.fetch_all()

    def get_conversation_history(self):

        return self.conversation_history.to_list()

    def get_memory(self, memory_id):

        cached = self.memory_cache.get(memory_id)

        if cached is not None:
            return cached

        memory = self.sqlite.fetch_by_id(memory_id)

        if memory:
            self.memory_cache.insert(memory_id, memory)

        return memory

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

        self.sqlite.delete_memory(memory_id)
        self.memory_cache.delete(memory_id)


if __name__ == "__main__":

    manager = MemoryManager()

    print(manager.get_all_memories())