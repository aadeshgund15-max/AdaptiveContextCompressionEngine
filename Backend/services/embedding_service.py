"""
Adaptive Context Intelligence Engine (ACIE)
Embedding Service (Singleton)
"""

from sentence_transformers import SentenceTransformer


class EmbeddingService:

    _instance = None
    _model = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            print("Loading embedding model...")

            cls._model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

            print("Embedding model loaded successfully.")

        return cls._instance

    def generate_embedding(self, text):

        embedding = self._model.encode(text)

        return embedding.tolist()


if __name__ == "__main__":

    service1 = EmbeddingService()

    service2 = EmbeddingService()

    print(service1 is service2)

    embedding = service1.generate_embedding(
        "Adaptive Context Compression"
    )

    print(len(embedding))