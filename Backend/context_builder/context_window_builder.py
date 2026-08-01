"""
Adaptive Context Intelligence Engine (ACIE)
Context Window Builder
"""

from Backend.compressor.token_estimator import TokenEstimator


class ContextWindowBuilder:

    def __init__(self):

        self.token_estimator = TokenEstimator()

    def build(self, ranked_memories, token_budget=100):

        selected_memories = []

        used_tokens = 0

        for memory in ranked_memories:

            text = memory["text"]

            tokens = self.token_estimator.estimate_tokens(text)

            if used_tokens + tokens > token_budget:
                continue

            selected_memories.append({

                "text": text,

                "ranking_score": memory["ranking_score"],

                "tokens": tokens

            })

            used_tokens += tokens

        return {

            "token_budget": token_budget,

            "used_tokens": used_tokens,

            "remaining_tokens": token_budget - used_tokens,

            "selected_count": len(selected_memories),

            "selected_memories": selected_memories

        }


if __name__ == "__main__":

    memories = [

        {
            "text": "Adaptive Context Compression Engine architecture using semantic retrieval and vector databases.",
            "ranking_score": 100
        },

        {
            "text": "Explain adaptive context compression.",
            "ranking_score": 75.3
        },

        {
            "text": "Memory optimization techniques.",
            "ranking_score": 65.2
        }

    ]

    builder = ContextWindowBuilder()

    result = builder.build(
        memories,
        token_budget=20
    )

    print("\nContext Window\n")

    print(result)