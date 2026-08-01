"""
Adaptive Context Intelligence Engine (ACIE)
Relationship Detector
"""


class RelationshipDetector:

    def __init__(self):

        self.relationship_keywords = {

            "embedding": "uses",

            "embeddings": "uses",

            "vector": "related_to",

            "database": "related_to",

            "retrieval": "depends_on",

            "memory": "part_of",

            "compression": "extends",

            "context": "related_to",

            "pipeline": "part_of",

            "graph": "connected_to"

        }

    def detect_relationship(self, query1, query2):

        text1 = query1.lower()

        text2 = query2.lower()

        for keyword, relation in self.relationship_keywords.items():

            if keyword in text1 and keyword in text2:

                return relation

        return None

    def build_relationships(self, memories):

        relationships = []

        total = len(memories)

        for i in range(total):

            for j in range(i + 1, total):

                relation = self.detect_relationship(

                    memories[i]["query"],

                    memories[j]["query"]

                )

                if relation is not None:

                    relationships.append({

                        "source": memories[i]["id"],

                        "target": memories[j]["id"],

                        "relationship": relation

                    })

        return relationships


if __name__ == "__main__":

    detector = RelationshipDetector()

    memories = [

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

        }

    ]

    results = detector.build_relationships(

        memories

    )

    print("\n========== DETECTED RELATIONSHIPS ==========\n")

    for relation in results:

        print(relation)