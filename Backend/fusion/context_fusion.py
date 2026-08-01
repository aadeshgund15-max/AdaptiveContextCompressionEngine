"""
Adaptive Context Intelligence Engine (ACIE)
Context Fusion Engine
"""


class ContextFusion:

    def __init__(self):

        pass

    # ---------------------------------
    # Remove Duplicate Memories
    # ---------------------------------

    def remove_duplicates(self, memories):

        unique = []

        seen = set()

        for memory in memories:

            text = memory["text"].strip().lower()

            if text not in seen:

                seen.add(text)

                unique.append(memory)

        return unique

    # ---------------------------------
    # Sort by Ranking Score
    # ---------------------------------

    def sort_memories(self, memories):

        return sorted(

            memories,

            key=lambda memory: memory["ranking_score"],

            reverse=True

        )

    # ---------------------------------
    # Merge Memories
    # ---------------------------------

    def merge(self, memories):

        merged_text = ""

        total_score = 0

        for memory in memories:

            merged_text += memory["text"] + " "

            total_score += memory["ranking_score"]

        average_score = 0

        if len(memories) > 0:

            average_score = total_score / len(memories)

        return {

            "text": merged_text.strip(),

            "ranking_score": round(average_score, 2),

            "source_count": len(memories)

        }

    # ---------------------------------
    # Complete Fusion Pipeline
    # ---------------------------------

    def fuse(self, memories):

        print("\n========== CONTEXT FUSION ==========\n")

        unique = self.remove_duplicates(

            memories

        )

        ranked = self.sort_memories(

            unique

        )

        fused = self.merge(ranked)

        return {

            "unique_memories": unique,

            "fused_context": [

                fused

            ]

        }


if __name__ == "__main__":

    memories = [

        {

            "text": "Adaptive Context Compression improves context handling.",

            "ranking_score": 94

        },

        {

            "text": "Adaptive Context Compression reduces token usage.",

            "ranking_score": 88

        },

        {

            "text": "Adaptive Context Compression improves context handling.",

            "ranking_score": 94

        },

        {

            "text": "Important memories are preserved.",

            "ranking_score": 82

        }

    ]

    fusion = ContextFusion()

    result = fusion.fuse(

        memories

    )

    print("\n========== RESULT ==========\n")

    print(result)