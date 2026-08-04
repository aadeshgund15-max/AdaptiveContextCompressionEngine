"""
Adaptive Context Intelligence Engine (ACIE)
Embedding Cache
"""

from __future__ import annotations

import hashlib
from datetime import datetime, timedelta


class EmbeddingCache:

    def __init__(

        self,

        ttl=3600

    ):

        self.cache = {}

        self.ttl = ttl

    # -------------------------------------------------
    # Generate Cache Key
    # -------------------------------------------------

    def generate_key(

        self,

        text

    ):

        return hashlib.sha256(

            text.encode(

                "utf-8"

            )

        ).hexdigest()

    # -------------------------------------------------
    # Store Embedding
    # -------------------------------------------------

    def put(

        self,

        text,

        embedding

    ):

        key = self.generate_key(

            text

        )

        self.cache[key] = {

            "embedding": embedding,

            "created": datetime.now()

        }

    # -------------------------------------------------
    # Retrieve Embedding
    # -------------------------------------------------

    def get(

        self,

        text

    ):

        key = self.generate_key(

            text

        )

        item = self.cache.get(

            key

        )

        if item is None:

            return None

        age = datetime.now() - item["created"]

        if age > timedelta(seconds=self.ttl):

            self.cache.pop(

                key,

                None

            )

            return None

        return item["embedding"]

    # -------------------------------------------------
    # Exists
    # -------------------------------------------------

    def exists(

        self,

        text

    ):

        return self.get(text) is not None

    # -------------------------------------------------
    # Remove
    # -------------------------------------------------

    def remove(

        self,

        text

    ):

        key = self.generate_key(

            text

        )

        self.cache.pop(

            key,

            None

        )

    # -------------------------------------------------
    # Clear Cache
    # -------------------------------------------------

    def clear(self):

        self.cache.clear()

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def stats(self):

        return {

            "entries": len(self.cache),

            "ttl": self.ttl

        }


if __name__ == "__main__":

    cache = EmbeddingCache()

    vector = [

        0.12,

        0.45,

        0.98

    ]

    cache.put(

        "Explain ACIE",

        vector

    )

    print()

    print(

        cache.get(

            "Explain ACIE"

        )

    )

    print()

    print(

        cache.stats()

    )