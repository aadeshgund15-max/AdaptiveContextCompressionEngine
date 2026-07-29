"""
Adaptive Context Intelligence Engine (ACIE)
Memory Manager
"""

from Backend.database.database import Database


class MemoryManager:

    def __init__(self):

        self.database = Database()

    def store(self, context, importance, confidence, decision):

        self.database.insert_memory(

            context["query"],

            importance,

            confidence,

            decision
        )

    def get_all_memories(self):

        return self.database.fetch_all()


if __name__ == "__main__":

    manager = MemoryManager()

    sample = {

        "query": "Explain semantic compression."
    }

    manager.store(

        sample,

        85,

        0.90,

        "STORE"
    )

    print(manager.get_all_memories())