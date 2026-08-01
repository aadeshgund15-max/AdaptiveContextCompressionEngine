"""
Adaptive Context Intelligence Engine (ACIE)
Retrieval Ranking Engine
"""

from datetime import datetime


class RetrievalRanker:

    def __init__(self):

        self.importance_weight = 0.40
        self.confidence_weight = 0.30
        self.access_weight = 0.20
        self.recency_weight = 0.10

    def calculate_recency_score(self, last_accessed):

        try:

            last_time = datetime.strptime(

                last_accessed,

                "%Y-%m-%d %H:%M:%S"

            )

            now = datetime.now()

            hours = (now - last_time).total_seconds() / 3600

            score = max(0, 100 - hours)

            return score

        except Exception:

            return 50

    def calculate_score(self, memory):

        importance = memory.get(

            "importance",

            0

        )

        confidence = memory.get(

            "confidence",

            0

        ) * 100

        access_count = min(

            memory.get(

                "access_count",

                0

            ),

            100

        )

        recency = self.calculate_recency_score(

            memory.get(

                "last_accessed",

                ""

            )

        )

        score = (

            importance * self.importance_weight +

            confidence * self.confidence_weight +

            access_count * self.access_weight +

            recency * self.recency_weight

        )

        return round(score, 2)

    def rank(self, memories):

        ranked = []

        for memory in memories:

            memory["ranking_score"] = self.calculate_score(

                memory

            )

            ranked.append(memory)

        ranked.sort(

            key=lambda x: x["ranking_score"],

            reverse=True

        )

        return ranked


if __name__ == "__main__":

    ranker = RetrievalRanker()

    memories = [

        {

            "query": "Explain RAG",

            "importance": 95,

            "confidence": 0.91,

            "access_count": 12,

            "last_accessed": "2026-08-01 10:00:00"

        },

        {

            "query": "Explain Vector DB",

            "importance": 80,

            "confidence": 0.88,

            "access_count": 4,

            "last_accessed": "2026-07-28 15:00:00"

        },

        {

            "query": "Explain Embeddings",

            "importance": 73,

            "confidence": 0.84,

            "access_count": 20,

            "last_accessed": "2026-08-01 09:30:00"

        }

    ]

    results = ranker.rank(

        memories

    )

    print("\n========== RANKED MEMORIES ==========\n")

    for memory in results:

        print(memory)