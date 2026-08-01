"""
Adaptive Context Intelligence Engine (ACIE)
Query Expansion Engine
"""

import re


class QueryExpander:

    def __init__(self):

        self.synonyms = {

            "rag": [
                "retrieval augmented generation",
                "semantic retrieval",
                "vector search",
                "knowledge retrieval"
            ],

            "embedding": [
                "vector embedding",
                "semantic embedding",
                "dense vector"
            ],

            "compression": [
                "context compression",
                "memory compression",
                "token compression",
                "semantic compression"
            ],

            "memory": [
                "episodic memory",
                "working memory",
                "long term memory",
                "semantic memory"
            ],

            "retrieval": [
                "semantic retrieval",
                "hybrid retrieval",
                "graph retrieval"
            ],

            "graph": [
                "knowledge graph",
                "graph database",
                "entity graph"
            ],

            "context": [
                "conversation context",
                "chat history",
                "memory context"
            ],

            "attention": [
                "attention mechanism",
                "focus selection",
                "memory prioritization"
            ]
        }

    def normalize(self, query):

        query = query.lower()

        query = re.sub(

            r"[^a-z0-9 ]",

            "",

            query

        )

        return query

    def expand(self, query):

        normalized = self.normalize(query)

        expanded = []

        expanded.append(query)

        words = normalized.split()

        for word in words:

            if word in self.synonyms:

                expanded.extend(

                    self.synonyms[word]

                )

        unique = []

        for item in expanded:

            if item not in unique:

                unique.append(item)

        return unique


if __name__ == "__main__":

    engine = QueryExpander()

    queries = engine.expand(

        "Explain adaptive context compression using memory"

    )

    print("\nExpanded Queries\n")

    for q in queries:

        print("-", q)