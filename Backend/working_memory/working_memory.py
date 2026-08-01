"""
Adaptive Context Intelligence Engine (ACIE)
Working Memory
"""

from Backend.working_memory.memory_buffer import MemoryBuffer


class WorkingMemory:

    def __init__(self, capacity=10):

        self.buffer = MemoryBuffer(capacity)

    def add_context(

        self,

        query,

        importance=0,

        source="conversation"

    ):

        memory = {

            "query": query,

            "importance": importance,

            "source": source

        }

        self.buffer.add_memory(memory)

    def get_recent_context(self):

        return self.buffer.get_memories()

    def get_latest_context(self):

        return self.buffer.get_latest()

    def clear(self):

        self.buffer.clear()

    def size(self):

        return self.buffer.size()

    def is_empty(self):

        return self.buffer.is_empty()

    def is_full(self):

        return self.buffer.is_full()


if __name__ == "__main__":

    wm = WorkingMemory(capacity=5)

    wm.add_context(

        "Explain adaptive context compression.",

        importance=95

    )

    wm.add_context(

        "Explain semantic retrieval.",

        importance=80

    )

    wm.add_context(

        "Explain vector databases.",

        importance=85

    )

    print("\n========== WORKING MEMORY ==========\n")

    for memory in wm.get_recent_context():

        print(memory)

    print("\nLatest Context\n")

    print(wm.get_latest_context())

    print("\nBuffer Size :", wm.size())