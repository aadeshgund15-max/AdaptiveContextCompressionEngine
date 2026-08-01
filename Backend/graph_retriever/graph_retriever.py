"""
Adaptive Context Intelligence Engine (ACIE)
Graph Retriever
"""

from Backend.hybrid.hybrid_retriever import HybridRetriever
from Backend.knowledge.graph_builder import GraphBuilder


class GraphRetriever:

    def __init__(self):

        self.hybrid = HybridRetriever()

        self.graph_builder = GraphBuilder()

    def retrieve(

        self,

        query,

        memories,

        top_k=5

    ):

        print("\n========== GRAPH RETRIEVER ==========\n")

        hybrid_results = self.hybrid.retrieve(

            query,

            top_k

        )

        graph = self.graph_builder.build(

            memories

        )

        expanded = []

        visited = set()

        for memory in memories:

            if memory["id"] not in visited:

                expanded.append(memory)

                visited.add(memory["id"])

            neighbours = graph.get_neighbors(

                memory["id"]

            )

            for neighbour in neighbours:

                target = neighbour["target"]

                for item in memories:

                    if item["id"] == target:

                        if target not in visited:

                            expanded.append(item)

                            visited.add(target)

        return {

            "hybrid_results": hybrid_results,

            "expanded_memories": expanded,

            "graph_statistics": {

                "nodes": graph.node_count(),

                "relationships": graph.relationship_count()

            }

        }


if __name__ == "__main__":

    retriever = GraphRetriever()

    sample = [

        {

            "id": 1,

            "query": "Explain vector databases.",

            "importance": 90

        },

        {

            "id": 2,

            "query": "Explain embeddings.",

            "importance": 88

        },

        {

            "id": 3,

            "query": "Semantic Retrieval",

            "importance": 85

        }

    ]

    result = retriever.retrieve(

        "vector database",

        sample

    )

    print(result)