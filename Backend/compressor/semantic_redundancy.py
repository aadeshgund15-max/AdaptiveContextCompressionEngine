"""
Adaptive Context Intelligence Engine (ACIE)
Semantic Redundancy Detector
"""

from Backend.services.embedding_service import EmbeddingService
import math


class SemanticRedundancy:

    def __init__(self):

        self.embedding_service = EmbeddingService()

    def cosine_similarity(self, vector1, vector2):

        dot = sum(a * b for a, b in zip(vector1, vector2))

        norm1 = math.sqrt(sum(a * a for a in vector1))

        norm2 = math.sqrt(sum(b * b for b in vector2))

        if norm1 == 0 or norm2 == 0:
            return 0

        return dot / (norm1 * norm2)

    def remove_similar(self, memories, threshold=0.85):

        unique = []

        embeddings = []

        for memory in memories:

            embedding = self.embedding_service.generate_embedding(memory)

            keep = True

            for previous in embeddings:

                similarity = self.cosine_similarity(
                    embedding,
                    previous
                )

                if similarity >= threshold:

                    keep = False

                    break

            if keep:

                unique.append(memory)

                embeddings.append(embedding)

        return unique


if __name__ == "__main__":

    detector = SemanticRedundancy()

    memories = [

        "Adaptive context compression improves prompt efficiency.",

        "Context compression reduces prompt size.",

        "Vector databases store embeddings.",

        "Embeddings are stored inside vector databases."
    ]

    result = detector.remove_similar(memories)

    print("\nUnique Memories\n")

    for memory in result:

        print("-", memory)