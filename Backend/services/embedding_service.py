"""
Adaptive Context Intelligence Engine (ACIE)
Embedding Service
"""

from Backend.core.model_registry import ModelRegistry


class EmbeddingService:

    def __init__(self):

        self.model = ModelRegistry.get_embedding_model()

    def generate_embedding(self, text):

        embedding = self.model.encode(text)

        return embedding.tolist()

    def generate_embeddings(self, texts):

        embeddings = self.model.encode(texts)

        return embeddings.tolist()


if __name__ == "__main__":

    service = EmbeddingService()

    text = "Adaptive Context Compression Engine"

    embedding = service.generate_embedding(text)

    print("Embedding Dimension :")

    print(len(embedding))

    print("\nFirst 10 Values :")

    print(embedding[:10])