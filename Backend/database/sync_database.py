"""
Synchronize SQLite memories to ChromaDB
"""

from Backend.database.database import Database
from Backend.database.chroma_database import ChromaDatabase
from Backend.services.embedding_service import EmbeddingService


def main():

    sqlite = Database()

    chroma = ChromaDatabase()

    embedding_service = EmbeddingService()

    chroma_ids = set(chroma.get_all_ids())

    memories = sqlite.fetch_all()

    added = 0

    for memory in memories:

        memory_id = str(memory[0])

        query = memory[1]

        if memory_id not in chroma_ids:

            embedding = embedding_service.generate_embedding(query)

            chroma.add_memory(

                memory_id,

                query,

                embedding

            )

            added += 1

            print(f"Added Memory {memory_id}")

    print()

    print("Synchronization Complete")

    print("New Memories Added :", added)

    print("Total ChromaDB Memories :", chroma.count())


if __name__ == "__main__":

    main()