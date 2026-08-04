"""
Adaptive Context Intelligence Engine (ACIE)
Decision Tree
"""


class DecisionTree:

    def __init__(self):

        pass

    # ---------------------------------
    # Decide Execution Strategy
    # ---------------------------------

    def decide(self, query):

        print("\n========== DECISION TREE ==========\n")

        query = query.lower()

        strategy = {

            "task_type": "General",

            "pipeline": "Memory + Retrieval + Response"

        }

        # -----------------------------
        # Coding
        # -----------------------------

        if any(word in query for word in [

            "code",

            "python",

            "java",

            "c++",

            "program",

            "algorithm"

        ]):

            strategy = {

                "task_type": "Coding",

                "pipeline":

                "Planner -> Retrieval -> Code Generator -> Verification"

            }

        # -----------------------------
        # Research
        # -----------------------------

        elif any(word in query for word in [

            "research",

            "paper",

            "survey",

            "citation",

            "patent"

        ]):

            strategy = {

                "task_type": "Research",

                "pipeline":

                "Planner -> Retrieval -> Reasoning -> Verification"

            }

        # -----------------------------
        # Mathematics
        # -----------------------------

        elif any(word in query for word in [

            "solve",

            "equation",

            "integral",

            "matrix",

            "math"

        ]):

            strategy = {

                "task_type": "Mathematics",

                "pipeline":

                "Reasoning -> Verification"

            }

        # -----------------------------
        # Search
        # -----------------------------

        elif any(word in query for word in [

            "search",

            "latest",

            "news",

            "browser",

            "internet"

        ]):

            strategy = {

                "task_type": "Search",

                "pipeline":

                "Browser -> Retrieval -> Verification"

            }

        # -----------------------------
        # Vision
        # -----------------------------

        elif any(word in query for word in [

            "image",

            "photo",

            "diagram",

            "picture"

        ]):

            strategy = {

                "task_type": "Vision",

                "pipeline":

                "Vision -> Reasoning -> Response"

            }

        return strategy

    # ---------------------------------
    # Pretty Print
    # ---------------------------------

    def pretty_print(self, strategy):

        print("\n========== DECISION ==========\n")

        print("Task Type :",

              strategy["task_type"])

        print()

        print("Pipeline")

        print(strategy["pipeline"])


if __name__ == "__main__":

    tree = DecisionTree()

    examples = [

        "Write Python code",

        "Explain Adaptive Context Compression",

        "Research vector databases",

        "Solve matrix multiplication",

        "Search latest AI news",

        "Analyze this image"

    ]

    for query in examples:

        print("\n--------------------------------")

        print("Query :", query)

        result = tree.decide(query)

        tree.pretty_print(result)