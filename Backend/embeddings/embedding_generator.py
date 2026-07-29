"""
Adaptive Context Intelligence Engine (ACIE)
Embedding Generator Module
"""

from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Model loaded successfully.")

    def generate_embedding(self, text):

        embedding = self.model.encode(text)

        return embedding.tolist()


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