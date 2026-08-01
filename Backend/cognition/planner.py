"""
Adaptive Context Intelligence Engine (ACIE)
Planner
"""


class Planner:

    def __init__(self):

        pass

    # ---------------------------------
    # Generate Tasks
    # ---------------------------------

    def generate_tasks(self, inference):

        tasks = []

        tasks.append({

            "step": 1,

            "task": "Analyze retrieved facts"

        })

        if inference["knowledge_gaps"]:

            tasks.append({

                "step": 2,

                "task": "Retrieve additional information"

            })

        tasks.append({

            "step": len(tasks) + 1,

            "task": "Generate final response"

        })

        return tasks

    # ---------------------------------
    # Estimate Complexity
    # ---------------------------------

    def estimate_complexity(self, tasks):

        count = len(tasks)

        if count <= 2:
            return "LOW"

        if count <= 4:
            return "MEDIUM"

        return "HIGH"

    # ---------------------------------
    # Build Plan
    # ---------------------------------

    def build_plan(self, inference):

        tasks = self.generate_tasks(

            inference

        )

        complexity = self.estimate_complexity(

            tasks

        )

        return {

            "goal": inference["query"],

            "complexity": complexity,

            "task_count": len(tasks),

            "tasks": tasks

        }

    # ---------------------------------
    # Complete Pipeline
    # ---------------------------------

    def process(self, inference):

        print("\n========== PLANNER ==========\n")

        return self.build_plan(

            inference

        )


if __name__ == "__main__":

    inference = {

        "query": "Explain Adaptive Context Compression",

        "facts": [

            "Adaptive Context Compression reduces tokens.",

            "Semantic Retrieval improves search."

        ],

        "knowledge_gaps": [

            "Need implementation details."

        ],

        "confidence": 0.82

    }

    planner = Planner()

    result = planner.process(

        inference

    )

    print("\n========== RESULT ==========\n")

    print(result)