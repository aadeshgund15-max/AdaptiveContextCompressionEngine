"""
Adaptive Context Intelligence Engine (ACIE)
Memory Summarizer
"""

from Backend.compressor.token_estimator import TokenEstimator


class MemorySummarizer:

    def __init__(self):

        self.token_estimator = TokenEstimator()

    def summarize(self, memories):

        if len(memories) == 0:

            return {

                "summary": "",

                "original_count": 0,

                "summary_tokens": 0,

                "compression_ratio": 0

            }

        unique = []

        seen = set()

        for memory in memories:

            normalized = memory.lower().strip()

            if normalized not in seen:

                seen.add(normalized)

                unique.append(memory)

        summary = " ".join(unique)

        original_tokens = 0

        for memory in memories:

            original_tokens += self.token_estimator.estimate_tokens(memory)

        summary_tokens = self.token_estimator.estimate_tokens(summary)

        if original_tokens == 0:

            ratio = 0

        else:

            ratio = round(

                ((original_tokens - summary_tokens)

                / original_tokens) * 100,

                2

            )

        return {

            "summary": summary,

            "original_count": len(memories),

            "unique_count": len(unique),

            "original_tokens": original_tokens,

            "summary_tokens": summary_tokens,

            "compression_ratio": ratio

        }


if __name__ == "__main__":

    memories = [

        "Vector databases store embeddings.",

        "Embeddings are stored inside vector databases.",

        "Vector databases store embeddings.",

        "Semantic search uses embeddings.",

        "Semantic search uses embeddings."

    ]

    summarizer = MemorySummarizer()

    result = summarizer.summarize(memories)

    print("\nSummary Report\n")

    for key, value in result.items():

        print(f"{key}: {value}")