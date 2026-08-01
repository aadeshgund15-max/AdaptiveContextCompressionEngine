"""
Adaptive Context Intelligence Engine (ACIE)
Attention Manager
"""


class AttentionManager:

    def __init__(self):

        self.minimum_attention = 0.05

    # ---------------------------------
    # Normalize Ranking Scores
    # ---------------------------------

    def normalize(self, memories):

        if not memories:
            return []

        total = sum(
            memory["ranking_score"]
            for memory in memories
        )

        if total == 0:
            total = 1

        result = []

        for memory in memories:

            attention = memory["ranking_score"] / total

            memory_copy = memory.copy()

            memory_copy["attention"] = round(
                attention,
                4
            )

            result.append(
                memory_copy
            )

        return result

    # ---------------------------------
    # Remove Low Attention Memories
    # ---------------------------------

    def filter_attention(

        self,

        memories

    ):

        filtered = []

        for memory in memories:

            if memory["attention"] >= self.minimum_attention:

                filtered.append(memory)

        return filtered

    # ---------------------------------
    # Sort by Attention
    # ---------------------------------

    def rank(self, memories):

        return sorted(

            memories,

            key=lambda x: x["attention"],

            reverse=True

        )

    # ---------------------------------
    # Complete Pipeline
    # ---------------------------------

    def compute(

        self,

        memories

    ):

        print("\n========== ATTENTION MANAGER ==========\n")

        normalized = self.normalize(

            memories

        )

        filtered = self.filter_attention(

            normalized

        )

        ranked = self.rank(

            filtered

        )

        return ranked


if __name__ == "__main__":

    memories = [

        {

            "text": "Adaptive Context Compression",

            "ranking_score": 95

        },

        {

            "text": "Semantic Retrieval",

            "ranking_score": 80

        },

        {

            "text": "Knowledge Graph",

            "ranking_score": 55

        },

        {

            "text": "Conversation History",

            "ranking_score": 20

        }

    ]

    manager = AttentionManager()

    result = manager.compute(

        memories

    )

    print("\n========== RESULT ==========\n")

    for memory in result:

        print(memory)