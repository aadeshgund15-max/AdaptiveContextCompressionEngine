"""
Adaptive Context Intelligence Engine (ACIE)
Reflection Reasoner
"""


class ReflectionReasoner:

    def __init__(self):

        pass

    # ---------------------------------
    # Reflect on Reasoning
    # ---------------------------------

    def reflect(self, reasoning):

        print("\n========== REFLECTION ==========\n")

        issues = []

        suggestions = []

        steps = reasoning.get("reasoning_steps", [])

        if len(steps) == 0:

            issues.append("No reasoning steps found.")

            suggestions.append("Generate reasoning before reflection.")

        else:

            if len(steps) < 3:

                issues.append("Reasoning contains very few steps.")

                suggestions.append("Increase reasoning depth.")

            else:

                suggestions.append(

                    "Reasoning structure looks complete."

                )

        final_reasoning = reasoning.get(

            "final_reasoning",

            ""

        )

        if final_reasoning.strip() == "":

            issues.append("Final conclusion missing.")

            suggestions.append(

                "Generate a final conclusion."

            )

        confidence = 100

        confidence -= len(issues) * 20

        if confidence < 0:

            confidence = 0

        return {

            "issues": issues,

            "suggestions": suggestions,

            "reflection_score": confidence

        }

    # ---------------------------------
    # Pretty Print
    # ---------------------------------

    def pretty_print(self, report):

        print("\n========== REFLECTION REPORT ==========\n")

        print("Reflection Score :", report["reflection_score"])

        print()

        print("Issues")

        if report["issues"]:

            for issue in report["issues"]:

                print("-", issue)

        else:

            print("None")

        print()

        print("Suggestions")

        for suggestion in report["suggestions"]:

            print("-", suggestion)


if __name__ == "__main__":

    reasoning = {

        "reasoning_steps": [

            {

                "step": 1,

                "title": "Understand Query",

                "result": "User asked about ACIE."

            },

            {

                "step": 2,

                "title": "Retrieve Memories",

                "result": "Relevant memories found."

            },

            {

                "step": 3,

                "title": "Analyze",

                "result": "Analyzed retrieved memories."

            }

        ],

        "final_reasoning":

            "Adaptive Context Compression improves memory efficiency."

    }

    engine = ReflectionReasoner()

    report = engine.reflect(

        reasoning

    )

    engine.pretty_print(

        report

    )