"""
Adaptive Context Intelligence Engine (ACIE)
Chain of Thought Reasoning
"""


class ChainOfThought:

    def __init__(self):

        self.steps = []

    # ---------------------------------
    # Start Reasoning
    # ---------------------------------

    def reason(self, query, memories):

        print("\n========== CHAIN OF THOUGHT ==========\n")

        self.steps = []

        self.steps.append({

            "step": 1,

            "title": "Understand Query",

            "result": f"User asked: {query}"

        })

        if memories:

            self.steps.append({

                "step": 2,

                "title": "Retrieve Memories",

                "result": f"{len(memories)} relevant memories found."

            })

        else:

            self.steps.append({

                "step": 2,

                "title": "Retrieve Memories",

                "result": "No relevant memories found."

            })

        memory_summary = []

        for memory in memories:

            if isinstance(memory, dict):

                if "query" in memory:

                    memory_summary.append(memory["query"])

                elif "text" in memory:

                    memory_summary.append(memory["text"])

        self.steps.append({

            "step": 3,

            "title": "Analyze Information",

            "result": memory_summary

        })

        self.steps.append({

            "step": 4,

            "title": "Draw Conclusion",

            "result": "Relevant knowledge has been identified."

        })

        return {

            "reasoning_steps": self.steps,

            "final_reasoning":

                "Reasoning completed successfully."

        }

    # ---------------------------------
    # Display Reasoning
    # ---------------------------------

    def pretty_print(self, reasoning):

        print("\n========== REASONING ==========\n")

        for step in reasoning["reasoning_steps"]:

            print(

                f"Step {step['step']} : {step['title']}"

            )

            print(

                step["result"]

            )

            print()

        print(

            "Final:",

            reasoning["final_reasoning"]

        )


if __name__ == "__main__":

    memories = [

        {

            "query":

                "Adaptive Context Compression"

        },

        {

            "query":

                "Semantic Retrieval"

        }

    ]

    cot = ChainOfThought()

    result = cot.reason(

        "Explain Adaptive Context Compression.",

        memories

    )

    cot.pretty_print(result)