"""
Adaptive Context Intelligence Engine (ACIE)
Knowledge Graph
"""

from Backend.data_structures.graph import Graph


class KnowledgeGraph:

    def __init__(self):

        # DSA Graph
        self.graph = Graph(True)

        # Stores memory information
        self.nodes = {}

        # Stores relationship labels
        self.relationships = {}

    # -------------------------------------------------

    def add_node(self, memory_id, query):

        if memory_id not in self.nodes:

            self.nodes[memory_id] = {

                "id": memory_id,

                "query": query

            }

            self.relationships[memory_id] = []

    # -------------------------------------------------

    def add_relationship(

        self,

        source,

        target,

        relationship

    ):

        # Graph edge
        self.graph.add_edge(source, target)

        # Relationship label
        self.relationships[source].append({

            "target": target,

            "relationship": relationship

        })

    # -------------------------------------------------

    def get_neighbors(self, memory_id):

        return self.relationships.get(

            memory_id,

            []

        )

    # -------------------------------------------------

    def get_node(self, memory_id):

        return self.nodes.get(

            memory_id,

            None

        )

    # -------------------------------------------------

    def get_all_nodes(self):

        return self.nodes

    # -------------------------------------------------

    def get_all_relationships(self):

        return self.relationships

    # -------------------------------------------------

    def bfs(self, start):

        return self.graph.bfs(start)

    # -------------------------------------------------

    def dfs(self, start):

        return self.graph.dfs(start)

    # -------------------------------------------------

    def shortest_path(

        self,

        start,

        end

    ):

        return self.graph.shortest_path(

            start,

            end

        )

    # -------------------------------------------------

    def node_count(self):

        return len(

            self.nodes

        )

    # -------------------------------------------------

    def relationship_count(self):

        total = 0

        for node in self.relationships:

            total += len(

                self.relationships[node]

            )

        return total

    # -------------------------------------------------

    def print_graph(self):

        print("\n========== KNOWLEDGE GRAPH ==========\n")

        for node_id in self.nodes:

            print(

                f"Memory {node_id}"

            )

            print(

                self.nodes[node_id]["query"]

            )

            neighbors = self.relationships[node_id]

            if len(neighbors) == 0:

                print("No relationships")

            else:

                for edge in neighbors:

                    print(

                        "  └──",

                        edge["relationship"],

                        "→",

                        edge["target"]

                    )

            print()

    # -------------------------------------------------

    def clear(self):

        self.nodes.clear()

        self.relationships.clear()

        self.graph = Graph(True)


if __name__ == "__main__":

    graph = KnowledgeGraph()

    graph.add_node(

        1,

        "Explain vector databases."

    )

    graph.add_node(

        2,

        "Explain embeddings."

    )

    graph.add_node(

        3,

        "Hybrid Retrieval"

    )

    graph.add_relationship(

        1,

        2,

        "uses"

    )

    graph.add_relationship(

        3,

        2,

        "depends_on"

    )

    graph.print_graph()

    print(

        "Nodes :",

        graph.node_count()

    )

    print(

        "Relationships :",

        graph.relationship_count()

    )

    print(

        "\nBFS :",

        graph.bfs(1)

    )

    print(

        "DFS :",

        graph.dfs(1)

    )

    print(

        "Shortest Path :",

        graph.shortest_path(

            1,

            2

        )

    )