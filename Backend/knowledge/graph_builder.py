"""
Adaptive Context Intelligence Engine (ACIE)
Knowledge Graph Builder
"""

from Backend.knowledge.knowledge_graph import KnowledgeGraph
from Backend.knowledge.relationship_detector import RelationshipDetector


class GraphBuilder:

    def __init__(self):

        self.graph = KnowledgeGraph()

        self.detector = RelationshipDetector()

    def build(self, memories):

        self.graph.clear()

        # -----------------------------
        # Create Nodes
        # -----------------------------

        for memory in memories:

            self.graph.add_node(

                memory["id"],

                memory["query"]

            )

        # -----------------------------
        # Detect Relationships
        # -----------------------------

        relationships = self.detector.build_relationships(

            memories

        )

        # -----------------------------
        # Add Relationships
        # -----------------------------

        for relation in relationships:

            self.graph.add_relationship(

                relation["source"],

                relation["target"],

                relation["relationship"]

            )

        return self.graph

    def statistics(self):

        return {

            "nodes": self.graph.node_count(),

            "relationships": self.graph.relationship_count()

        }


if __name__ == "__main__":

    sample_memories = [

        {

            "id": 1,

            "query": "Explain vector databases."

        },

        {

            "id": 2,

            "query": "Explain vector embeddings."

        },

        {

            "id": 3,

            "query": "Hybrid Retrieval Pipeline"

        },

        {

            "id": 4,

            "query": "Context Compression"

        },

        {

            "id": 5,

            "query": "Memory Pipeline"

        }

    ]

    builder = GraphBuilder()

    graph = builder.build(

        sample_memories

    )

    graph.print_graph()

    print("\nStatistics\n")

    print(

        builder.statistics()

    )