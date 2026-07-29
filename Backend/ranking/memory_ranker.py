"""
Adaptive Context Intelligence Engine (ACIE)
Memory Ranker
"""

from Backend.compressor.token_estimator import TokenEstimator


class MemoryRanker:

    def __init__(self):

        self.estimator = TokenEstimator()

    def rank(self, memories):

        ranked = []

        for memory in memories:

            score = len(memory)

            tokens = self.estimator.estimate_tokens(memory)

            ranked.append({

                "memory": memory,

                "score": score,

                "tokens": tokens

            })

        ranked.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return ranked

    def select_under_budget(

        self,

        ranked_memories,

        token_budget

    ):

        selected = []

        used_tokens = 0

        for memory in ranked_memories:

            if used_tokens + memory["tokens"] <= token_budget:

                selected.append(memory)

                used_tokens += memory["tokens"]

        return selected


if __name__ == "__main__":

    ranker = MemoryRanker()

    memories = [

        "Adaptive context compression improves prompt efficiency.",

        "Vector databases store embeddings.",

        "Context compression removes redundant memories.",

        "Embeddings enable semantic retrieval."
    ]

    ranked = ranker.rank(memories)

    selected = ranker.select_under_budget(

        ranked,

        token_budget=20

    )

    print("\nSelected Memories\n")

    for memory in selected:

        print(memory)