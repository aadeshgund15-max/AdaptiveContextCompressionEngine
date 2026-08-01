"""
Adaptive Context Intelligence Engine (ACIE)
Hybrid Retriever
"""

from Backend.database.database import Database
from Backend.retriever.retriever import Retriever
from Backend.ranking.memory_ranking import MemoryRanking


class HybridRetriever:

    def __init__(self):

        self.sqlite = Database()
        self.semantic = Retriever()
        self.ranker = MemoryRanking()

    def keyword_search(self, query):

        all_memories = self.sqlite.fetch_all()

        results = []

        query = query.lower()

        for memory in all_memories:

            text = memory[1]

            if query in text.lower():

                results.append({
                    "text": text,
                    "semantic_score": 1.0,
                    "importance": memory[2],
                    "confidence": memory[3]
                })

        return results

    def semantic_search(self, query, top_k=5):

        results = self.semantic.retrieve(query, top_k)

        documents = results.get("documents", [[]])
        distances = results.get("distances", [[]])

        semantic_results = []

        if not documents or len(documents) == 0 or not distances or len(distances) == 0:
            return semantic_results

        for i in range(len(documents[0])):

            distance = distances[0][i]

            similarity = max(0, 1 - distance)

            semantic_results.append({

                "text": documents[0][i],

                "semantic_score": similarity,

                "importance": 70,

                "confidence": 0.90

            })

        return semantic_results

    def retrieve(self, query, top_k=5):

        keyword_results = self.keyword_search(query)

        semantic_results = self.semantic_search(query, top_k)

        merged = {}

        for memory in keyword_results:

            merged[memory["text"]] = memory

        for memory in semantic_results:

            if memory["text"] not in merged:

                merged[memory["text"]] = memory

        ranked = self.ranker.rank(

            list(merged.values())

        )

        return ranked[:top_k]


if __name__ == "__main__":

    retriever = HybridRetriever()

    results = retriever.retrieve(

        "adaptive context compression",

        5

    )

    print("\nRanked Hybrid Retrieval\n")

    for memory in results:

        print(memory)