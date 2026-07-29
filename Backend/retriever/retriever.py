"""
Adaptive Context Intelligence Engine (ACIE)
Retriever Module
"""

from Backend.memory.memory_manager import MemoryManager


class Retriever:

    def __init__(self):
        self.memory_manager = MemoryManager()

    def retrieve(self, keyword):
        """
        Retrieve memories containing the given keyword.
        """

        memories = self.memory_manager.get_all_memories()

        results = []

        for memory in memories:

            query = memory[1]

            if keyword.lower() in query.lower():
                results.append(memory)

        return results


if __name__ == "__main__":

    retriever = Retriever()

    keyword = "compression"

    results = retriever.retrieve(keyword)

    print("Retrieved Memories")

    if len(results) == 0:
        print("No matching memories found.")

    else:

        for item in results:
            print(item)