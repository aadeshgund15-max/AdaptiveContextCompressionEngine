"""
Adaptive Context Intelligence Engine (ACIE)
Semantic Compressor
"""

import numpy as np
from Backend.services.embedding_service import EmbeddingService
from sklearn.metrics.pairwise import cosine_similarity


class SemanticCompressor:

    def __init__(self):

        self.embedding_service = EmbeddingService()

    def compress(self, sentences, threshold=0.85):

        if len(sentences) <= 1:
            return sentences

        embeddings = []

        for sentence in sentences:
            embeddings.append(
                self.embedding_service.generate_embedding(sentence)
            )

        embeddings = np.vstack(embeddings)

        compressed = []

        for i in range(len(sentences)):

            duplicate = False

            for kept in compressed:

                kept_index = sentences.index(kept)

                similarity = cosine_similarity(
                    embeddings[i:i+1],
                    embeddings[kept_index:kept_index+1]
                )[0][0]

                if similarity >= threshold:
                    duplicate = True
                    break

            if not duplicate:
                compressed.append(sentences[i])

        return compressed


if __name__ == "__main__":

    compressor = SemanticCompressor()

    sample = [

        "Vector databases store embeddings.",

        "Embeddings are stored inside vector databases.",

        "Adaptive Context Compression reduces token usage.",

        "Context compression helps LLMs."
    ]

    result = compressor.compress(sample)

    print("\nOriginal Sentences\n")

    for sentence in sample:
        print("-", sentence)

    print("\nCompressed Sentences\n")

    for sentence in result:
        print("-", sentence)