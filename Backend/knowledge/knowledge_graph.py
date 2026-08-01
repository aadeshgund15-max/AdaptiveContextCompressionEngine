"""
Adaptive Context Intelligence Engine (ACIE)
Knowledge Graph
"""


class KnowledgeGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = {}

    def add_node(self, memory_id, query):

        if memory_id not in self.nodes:

            self.nodes[memory_id] = {

                "id": memory_id,

                "query": query

            }

            self.edges[memory_id] = []

    def add_relationship(

        self,

        source,

        target,

        relationship

    ):

        if source not in self.edges:

            self.edges[source] = []

        self.edges[source].append({

            "target": target,

            "relationship": relationship

        })

    def get_neighbors(self, memory_id):

        return self.edges.get(

            memory_id,

            []

        )

    def get_node(self, memory_id):

        return self.nodes.get(

            memory_id,

            None

        )

    def get_all_nodes(self):

        return self.nodes

    def get_all_relationships(self):

        return self.edges

    def node_count(self):

        return len(

            self.nodes

        )

    def relationship_count(self):

        total = 0

        for node in self.edges:

            total += len(

                self.edges[node]

            )

        return total

    def print_graph(self):

        print("\n========== KNOWLEDGE GRAPH ==========\n")

        for node_id in self.nodes:

            print(

                f"Memory {node_id}"

            )

            print(

                self.nodes[node_id]["query"]

            )

            neighbors = self.edges[node_id]

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

    def clear(self):

        self.nodes.clear()

        self.edges.clear()


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