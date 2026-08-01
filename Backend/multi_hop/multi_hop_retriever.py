"""
Adaptive Context Intelligence Engine (ACIE)
Multi-Hop Retriever
"""

from collections import deque


class MultiHopRetriever:

    def __init__(self):

        self.graph = {}

    # ---------------------------------
    # Load Graph
    # ---------------------------------

    def load_graph(self, graph):

        self.graph = graph

    # ---------------------------------
    # Breadth First Search
    # ---------------------------------

    def retrieve(

        self,

        start_node,

        max_hops=3

    ):

        print("\n========== MULTI-HOP RETRIEVAL ==========\n")

        if start_node not in self.graph:

            return {

                "visited_nodes": [],

                "paths": [],

                "hop_count": 0

            }

        visited = set()

        queue = deque()

        queue.append(

            (

                start_node,

                0,

                [start_node]

            )

        )

        visited.add(start_node)

        paths = []

        visited_nodes = []

        while queue:

            node, depth, path = queue.popleft()

            visited_nodes.append(node)

            paths.append(path)

            if depth >= max_hops:

                continue

            neighbours = self.graph.get(

                node,

                []

            )

            for neighbour in neighbours:

                if neighbour not in visited:

                    visited.add(neighbour)

                    queue.append(

                        (

                            neighbour,

                            depth + 1,

                            path + [neighbour]

                        )

                    )

        return {

            "visited_nodes": visited_nodes,

            "paths": paths,

            "hop_count": max_hops

        }


if __name__ == "__main__":

    graph = {

        "Adaptive Context Compression": [

            "Semantic Retrieval",

            "Memory Compression"

        ],

        "Semantic Retrieval": [

            "Embeddings",

            "Vector Database"

        ],

        "Memory Compression": [

            "Token Compression"

        ],

        "Embeddings": [

            "Sentence Transformer"

        ],

        "Vector Database": [

            "ChromaDB"

        ],

        "Sentence Transformer": [],

        "ChromaDB": [],

        "Token Compression": []

    }

    retriever = MultiHopRetriever()

    retriever.load_graph(graph)

    result = retriever.retrieve(

        start_node="Adaptive Context Compression",

        max_hops=3

    )

    print("\nVisited Nodes\n")

    for node in result["visited_nodes"]:

        print("-", node)

    print("\nPaths\n")

    for path in result["paths"]:

        print(" -> ".join(path))