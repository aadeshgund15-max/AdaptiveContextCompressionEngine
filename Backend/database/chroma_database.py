"""
Adaptive Context Intelligence Engine (ACIE)
ChromaDB Database Module
"""

import chromadb
import shutil
import os


class ChromaDatabase:

    def __init__(self):

        self.db_path = "chromadb"

        self.client = chromadb.PersistentClient(
            path=self.db_path
        )

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

    def get_all_memories(self):

        return self.collection.get()

    def get_all_ids(self):

        return self.collection.get()["ids"]

    def count(self):

        return self.collection.count()

    def delete_all(self):

        ids = self.get_all_ids()

        if len(ids) > 0:

            self.collection.delete(
                ids=ids
            )

    def reset_database(self):

        try:

            self.client.delete_collection(
                "acie_memory"
            )

        except Exception:
            pass

        if os.path.exists(self.db_path):

            shutil.rmtree(self.db_path)

        self.client = chromadb.PersistentClient(
            path=self.db_path
        )

        self.collection = self.client.get_or_create_collection(
            name="acie_memory"
        )


if __name__ == "__main__":

    chroma = ChromaDatabase()

    print("Total Memories :", chroma.count())

    print("\nMemory IDs :")
    print(chroma.get_all_ids())