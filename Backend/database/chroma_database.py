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

        self.collection.add(
            ids=[str(memory_id)],
            documents=[query],
            embeddings=[embedding]
        )

    def search(self, embedding, top_k=5):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

    def count(self):

        return self.collection.count()


if __name__ == "__main__":

    db = ChromaDatabase()

    print("Collection Size :", db.count())