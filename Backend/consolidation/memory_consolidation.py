"""
Adaptive Context Intelligence Engine (ACIE)
Memory Consolidation Engine
"""


class MemoryConsolidation:

    def __init__(self):

        self.importance_threshold = 70

    def remove_duplicates(self, memories):

        unique = []

        seen = set()

        for memory in memories:

            query = memory.get("query", "").strip().lower()

            if query not in seen:

                seen.add(query)

                unique.append(memory)

        return unique

    def filter_low_importance(self, memories):

        filtered = []

        for memory in memories:

            importance = memory.get("importance", 0)

            if importance >= self.importance_threshold:

                filtered.append(memory)

        return filtered

    def merge_memories(self, memories):

        merged = {}

        for memory in memories:

            query = memory.get("query", "").strip()

            if query not in merged:

                merged[query] = memory

            else:

                merged[query]["importance"] = max(

                    merged[query]["importance"],

                    memory["importance"]

                )

        return list(merged.values())

    def consolidate(self, memories):

        memories = self.remove_duplicates(memories)

        memories = self.filter_low_importance(memories)

        memories = self.merge_memories(memories)

        return memories


if __name__ == "__main__":

    consolidator = MemoryConsolidation()

    sample_memories = [

        {

            "query": "Explain RAG",

            "importance": 85

        },

        {

            "query": "Explain RAG",

            "importance": 90

        },

        {

            "query": "Explain embeddings",

            "importance": 65

        },

        {

            "query": "Explain vector database",

            "importance": 95

        }

    ]

    result = consolidator.consolidate(

        sample_memories

    )

    print("\n========== CONSOLIDATED MEMORIES ==========\n")

    for memory in result:

        print(memory)