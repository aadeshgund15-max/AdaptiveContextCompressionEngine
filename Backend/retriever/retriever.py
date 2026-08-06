"""
Adaptive Context Intelligence Engine (ACIE)
Semantic Retriever
"""

from Backend.database.chroma_database import ChromaDatabase
from Backend.services.embedding_service import EmbeddingService
from Backend.data_structures.hash_table import HashTable


class Retriever:

    def __init__(self):

        self.chroma = ChromaDatabase()

        self.embedding_service = EmbeddingService()

        # DSA: Hash Table Cache
        self.cache = HashTable()

    # ============================================
    # Semantic Retrieval
    # ============================================

    def retrieve(self, query, top_k=5):

        # Check cache first
        cached_result = self.cache.get(query)

        if cached_result is not None:

            print("Retrieved from Hash Table Cache")

            return cached_result

        # Generate embedding
        embedding = self.embedding_service.generate_embedding(query)

        # Search ChromaDB
        results = self.chroma.search(

            embedding,

            top_k

        )

        # Store in cache
        self.cache.insert(query, results)

        return results

    # ============================================
    # Clear Cache
    # ============================================

    def clear_cache(self):

        self.cache = HashTable()

    # ============================================
    # Cache Size
    # ============================================

    def cache_size(self):

        return self.cache.size

    # ============================================
    # Display Cache
    # ============================================

    def display_cache(self):

        self.cache.display()


if __name__ == "__main__":

    retriever = Retriever()

    print("\nFirst Search\n")

    results = retriever.retrieve(

        "memory optimization"

    )

    print(results)

    print("\nSecond Search (Cached)\n")

    results = retriever.retrieve(

        "memory optimization"

    )

    print(results)

    print("\nCache Size :", retriever.cache_size())

    retriever.display_cache()