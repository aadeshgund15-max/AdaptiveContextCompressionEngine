"""
Adaptive Context Intelligence Engine (ACIE)
Cache Manager
"""

from __future__ import annotations

from Backend.cache.memory_cache import MemoryCache
from Backend.cache.embedding_cache import EmbeddingCache


class CacheManager:

    def __init__(

        self

    ):

        self.memory_cache = MemoryCache(

            ttl=300

        )

        self.embedding_cache = EmbeddingCache(

            ttl=3600

        )

    # -------------------------------------------------
    # Memory Cache
    # -------------------------------------------------

    def cache_memory(

        self,

        key,

        value

    ):

        self.memory_cache.put(

            key,

            value

        )

    def get_memory(

        self,

        key

    ):

        return self.memory_cache.get(

            key

        )

    def remove_memory(

        self,

        key

    ):

        self.memory_cache.remove(

            key

        )

    # -------------------------------------------------
    # Embedding Cache
    # -------------------------------------------------

    def cache_embedding(

        self,

        text,

        embedding

    ):

        self.embedding_cache.put(

            text,

            embedding

        )

    def get_embedding(

        self,

        text

    ):

        return self.embedding_cache.get(

            text

        )

    def remove_embedding(

        self,

        text

    ):

        self.embedding_cache.remove(

            text

        )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def statistics(

        self

    ):

        return {

            "memory_cache":

            self.memory_cache.stats(),

            "embedding_cache":

            self.embedding_cache.stats()

        }

    # -------------------------------------------------
    # Clear All
    # -------------------------------------------------

    def clear_all(

        self

    ):

        self.memory_cache.clear()

        self.embedding_cache.clear()


if __name__ == "__main__":

    manager = CacheManager()

    manager.cache_memory(

        "query",

        "Explain ACIE"

    )

    manager.cache_embedding(

        "Explain ACIE",

        [

            0.21,

            0.45,

            0.76

        ]

    )

    print()

    print(

        manager.get_memory(

            "query"

        )

    )

    print()

    print(

        manager.get_embedding(

            "Explain ACIE"

        )

    )

    print()

    print(

        manager.statistics()

    )