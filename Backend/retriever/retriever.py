"""
Adaptive Context Intelligence Engine (ACIE)
Semantic Retriever
"""

from Backend.database.chroma_database import ChromaDatabase
from Backend.services.embedding_service import EmbeddingService


class Retriever:

    def __init__(self):

        self.chroma = ChromaDatabase()
        self.embedding_service = EmbeddingService()

    def retrieve(self, query, top_k=5):

        embedding = self.embedding_service.generate_embedding(query)

        results = self.chroma.search(
            embedding,
            top_k
        )

        return results


if __name__ == "__main__":

    retriever = Retriever()

    results = retriever.retrieve(
        "memory optimization"
    )

    print("\nSemantic Search Results\n")

    print(results)