"""
Adaptive Context Intelligence Engine (ACIE)
Context Optimizer
"""


class ContextOptimizer:

    def __init__(self):

        pass

    # ------------------------------------------
    # Optimize Context
    # ------------------------------------------

    def optimize(

        self,

        retrieved_memories,

        max_memories=5

    ):

        print("\n========== CONTEXT OPTIMIZER ==========\n")

        if not retrieved_memories:

            return []

        # -----------------------------
        # Sort by ranking score
        # -----------------------------

        ranked = sorted(

            retrieved_memories,

            key=lambda memory: memory.get(

                "ranking_score",

                0

            ),

            reverse=True

        )

        optimized = ranked[:max_memories]

        return optimized

    # ------------------------------------------
    # Build Optimized Context Window
    # ------------------------------------------

    def build_context(

        self,

        optimized_memories

    ):

        context = []

        for memory in optimized_memories:

            if "text" in memory:

                context.append(

                    memory["text"]

                )

            elif "query" in memory:

                context.append(

                    memory["query"]

                )

        return "\n".join(context)


if __name__ == "__main__":

    memories = [

        {

            "text": "Adaptive Context Compression",

            "ranking_score": 95

        },

        {

            "text": "Semantic Retrieval",

            "ranking_score": 91

        },

        {

            "text": "Knowledge Graph",

            "ranking_score": 82

        },

        {

            "text": "Vector Database",

            "ranking_score": 76

        },

        {

            "text": "Memory Consolidation",

            "ranking_score": 70

        },

        {

            "text": "Reflection",

            "ranking_score": 65

        }

    ]

    optimizer = ContextOptimizer()

    optimized = optimizer.optimize(

        memories,

        max_memories=4

    )

    context = optimizer.build_context(

        optimized

    )

    print("\n========== OPTIMIZED ==========\n")

    print(optimized)

    print("\n========== CONTEXT ==========\n")

    print(context)