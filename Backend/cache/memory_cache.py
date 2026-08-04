"""
Adaptive Context Intelligence Engine (ACIE)
Memory Cache
"""

from __future__ import annotations

from datetime import datetime, timedelta
from threading import Lock


class MemoryCache:

    def __init__(

        self,

        ttl=300,

        max_entries=1000

    ):

        self.cache = {}

        self.ttl = ttl

        self.max_entries = max_entries

        self.lock = Lock()

    # -------------------------------------------------
    # Store
    # -------------------------------------------------

    def put(

        self,

        key,

        value

    ):

        with self.lock:

            if len(self.cache) >= self.max_entries:

                oldest = min(

                    self.cache,

                    key=lambda item: self.cache[item]["created"]

                )

                self.cache.pop(

                    oldest,

                    None

                )

            self.cache[key] = {

                "value": value,

                "created": datetime.now(),

                "last_accessed": datetime.now(),

                "hits": 0

            }

    # -------------------------------------------------
    # Retrieve
    # -------------------------------------------------

    def get(

        self,

        key

    ):

        with self.lock:

            item = self.cache.get(key)

            if item is None:

                return None

            age = datetime.now() - item["created"]

            if age > timedelta(seconds=self.ttl):

                self.cache.pop(

                    key,

                    None

                )

                return None

            item["last_accessed"] = datetime.now()

            item["hits"] += 1

            return item["value"]

    # -------------------------------------------------
    # Exists
    # -------------------------------------------------

    def exists(

        self,

        key

    ):

        return self.get(key) is not None

    # -------------------------------------------------
    # Remove
    # -------------------------------------------------

    def remove(

        self,

        key

    ):

        with self.lock:

            self.cache.pop(

                key,

                None

            )

    # -------------------------------------------------
    # Clear
    # -------------------------------------------------

    def clear(self):

        with self.lock:

            self.cache.clear()

    # -------------------------------------------------
    # Cleanup Expired
    # -------------------------------------------------

    def cleanup(self):

        with self.lock:

            expired = []

            now = datetime.now()

            for key, value in self.cache.items():

                age = now - value["created"]

                if age > timedelta(seconds=self.ttl):

                    expired.append(key)

            for key in expired:

                self.cache.pop(

                    key,

                    None

                )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    def stats(self):

        total_hits = sum(

            value["hits"]

            for value in self.cache.values()

        )

        return {

            "entries": len(self.cache),

            "ttl": self.ttl,

            "max_entries": self.max_entries,

            "total_hits": total_hits

        }

    # -------------------------------------------------
    # Keys
    # -------------------------------------------------

    def keys(self):

        return list(

            self.cache.keys()

        )

    # -------------------------------------------------
    # Values
    # -------------------------------------------------

    def values(self):

        return [

            item["value"]

            for item in self.cache.values()

        ]

    # -------------------------------------------------
    # Length
    # -------------------------------------------------

    def __len__(self):

        return len(

            self.cache

        )


if __name__ == "__main__":

    cache = MemoryCache()

    cache.put(

        "query",

        "Explain ACIE"

    )

    print()

    print(

        cache.get(

            "query"

        )

    )

    print()

    print(

        cache.stats()

    )

    print()

    print(

        cache.keys()

    )