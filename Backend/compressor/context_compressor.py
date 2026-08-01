"""
Adaptive Context Intelligence Engine (ACIE)
Context Compressor
"""

from Backend.compressor.token_estimator import TokenEstimator
from Backend.compressor.redundancy_detector import RedundancyDetector
from Backend.compressor.semantic_compressor import SemanticCompressor


class ContextCompressor:

    def __init__(self):

        self.detector = RedundancyDetector()
        self.estimator = TokenEstimator()
        self.semantic = SemanticCompressor()

    def compress(self, memories):

        print("\nStarting Context Compression...\n")

        # -----------------------------
        # Original Statistics
        # -----------------------------

        original_count = len(memories)

        original_tokens = 0

        for memory in memories:
            original_tokens += self.estimator.estimate(memory)

        # -----------------------------
        # Remove Exact Duplicates
        # -----------------------------

        unique_memories = self.detector.remove_duplicates(memories)

        # -----------------------------
        # Remove Semantic Duplicates
        # -----------------------------

        compressed_memories = self.semantic.compress(unique_memories)

        # -----------------------------
        # Compressed Statistics
        # -----------------------------

        compressed_count = len(compressed_memories)

        compressed_tokens = 0

        for memory in compressed_memories:
            compressed_tokens += self.estimator.estimate(memory)

        tokens_saved = original_tokens - compressed_tokens

        if original_tokens == 0:
            compression_ratio = 0
        else:
            compression_ratio = round(
                (tokens_saved / original_tokens) * 100,
                2
            )

        return {

            "original_count": original_count,

            "compressed_count": compressed_count,

            "original_tokens": original_tokens,

            "compressed_tokens": compressed_tokens,

            "tokens_saved": tokens_saved,

            "compression_ratio": compression_ratio,

            "compressed_memories": compressed_memories

        }


if __name__ == "__main__":

    memories = [

        "Explain adaptive context compression.",

        "Explain adaptive context compression.",

        "Explain semantic compression.",

        "Semantic compression is used to reduce redundant context.",

        "Memory optimization techniques.",

        "Memory optimization techniques.",

        "Vector databases store embeddings.",

        "Embeddings are stored inside vector databases."

    ]

    compressor = ContextCompressor()

    result = compressor.compress(memories)

    print("\n======================================")
    print("Compression Report")
    print("======================================")

    print("Original Memories      :", result["original_count"])
    print("Compressed Memories    :", result["compressed_count"])
    print("Original Tokens        :", result["original_tokens"])
    print("Compressed Tokens      :", result["compressed_tokens"])
    print("Tokens Saved           :", result["tokens_saved"])
    print("Compression Ratio      :", result["compression_ratio"], "%")

    print("\nCompressed Memories\n")

    for memory in result["compressed_memories"]:
        print("-", memory)