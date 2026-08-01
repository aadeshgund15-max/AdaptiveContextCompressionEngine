"""
Adaptive Context Intelligence Engine (ACIE)
Memory Ranking Engine
"""


class MemoryRanking:

    def __init__(self):

        pass

    def calculate_score(

        self,

        semantic_score,

        importance,

        confidence

    ):

        semantic_component = semantic_score * 50

        importance_component = importance * 0.30

        confidence_component = confidence * 100 * 0.20

        final_score = (

            semantic_component

            + importance_component

            + confidence_component

        )

        return round(final_score, 2)

    def rank(self, memories):

        ranked = []

        for memory in memories:

            score = self.calculate_score(

                memory["semantic_score"],

                memory["importance"],

                memory["confidence"]

            )

            memory["ranking_score"] = score

            ranked.append(memory)

        ranked.sort(

            key=lambda x: x["ranking_score"],

            reverse=True

        )

        return ranked


if __name__ == "__main__":

    memories = [

        {

            "text": "Vector databases store embeddings.",

            "semantic_score": 0.92,

            "importance": 88,

            "confidence": 0.97

        },

        {

            "text": "Memory optimization techniques.",

            "semantic_score": 0.73,

            "importance": 75,

            "confidence": 0.91

        },

        {

            "text": "Python while loop.",

            "semantic_score": 0.25,

            "importance": 40,

            "confidence": 0.80

        }

    ]

    ranking = MemoryRanking()

    ranked = ranking.rank(memories)

    print("\nRanked Memories\n")

    for memory in ranked:

        print(

            memory["ranking_score"],

            "-",

            memory["text"]

        )