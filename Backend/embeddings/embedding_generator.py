"""
Adaptive Context Intelligence Engine (ACIE)
Embedding Generator Module
"""

from Backend.services.embedding_service import EmbeddingService


class EmbeddingGenerator:

    def __init__(self):

        self.service = EmbeddingService()

    def generate_embedding(self, text):

        return self.service.generate_embedding(text)


if __name__ == "__main__":

    generator = EmbeddingGenerator()

    sentence = "Explain adaptive context compression."

    embedding = generator.generate_embedding(sentence)

    print("\nSentence:")
    print(sentence)

    print("\nEmbedding Dimension:")
    print(len(embedding))

    print("\nFirst 10 Values:")
    print(embedding[:10])