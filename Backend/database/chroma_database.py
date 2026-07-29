"""
Adaptive Context Intelligence Engine (ACIE)
ChromaDB Database Module
"""

import chromadb


class ChromaDatabase:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="chromadb")

        self.collection = self.client.get_or_create_collection(
            name="acie_memory"
        )

    def add_memory(self, memory_id, query, embedding):

        try:

            self.collection.add(

                ids=[str(memory_id)],

                documents=[query],

                embeddings=[embedding]

            )

        except Exception:

            # Ignore duplicate IDs
            pass

    def search(self, embedding, top_k=5):

        return self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k

        )

    def get_all_ids(self):

        return self.collection.get()["ids"]

    def count(self):

        return self.collection.count()