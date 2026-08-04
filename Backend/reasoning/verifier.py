"""
Adaptive Context Intelligence Engine (ACIE)
Verifier
"""


class Verifier:

    def __init__(self):

        pass

    # ---------------------------------
    # Verify Reasoning
    # ---------------------------------

    def verify(

        self,

        reasoning,

        retrieved_memories

    ):

        print("\n========== VERIFIER ==========\n")

        report = {

            "verified": True,

            "confidence": 100,

            "checks": []

        }

        # -----------------------------
        # Check reasoning exists
        # -----------------------------

        if len(reasoning.get("reasoning_steps", [])) == 0:

            report["verified"] = False

            report["confidence"] -= 40

            report["checks"].append({

                "check": "Reasoning",

                "status": "FAILED",

                "message": "No reasoning steps found."

            })

        else:

            report["checks"].append({

                "check": "Reasoning",

                "status": "PASSED",

                "message": "Reasoning available."

            })

        # -----------------------------
        # Check retrieved memories
        # -----------------------------

        if len(retrieved_memories) == 0:

            report["verified"] = False

            report["confidence"] -= 30

            report["checks"].append({

                "check": "Memory",

                "status": "FAILED",

                "message": "No supporting memories."

            })

        else:

            report["checks"].append({

                "check": "Memory",

                "status": "PASSED",

                "message": f"{len(retrieved_memories)} supporting memories."

            })

        # -----------------------------
        # Check conclusion
        # -----------------------------

        conclusion = reasoning.get(

            "final_reasoning",

            ""

        )

        if conclusion.strip() == "":

            report["verified"] = False

            report["confidence"] -= 30

            report["checks"].append({

                "check": "Conclusion",

                "status": "FAILED",

                "message": "Conclusion missing."

            })

        else:

            report["checks"].append({

                "check": "Conclusion",

                "status": "PASSED",

                "message": "Conclusion generated."

            })

        if report["confidence"] < 0:

            report["confidence"] = 0

        return report

    # ---------------------------------
    # Pretty Print
    # ---------------------------------

    def pretty_print(

        self,

        report

    ):

        print("\n========== VERIFICATION REPORT ==========\n")

        print("Verified :", report["verified"])

        print("Confidence :", report["confidence"])

        print()

        for item in report["checks"]:

            print(

                f"[{item['status']}] {item['check']}"

            )

            print(

                item["message"]

            )

            print()


if __name__ == "__main__":

    reasoning = {

        "reasoning_steps": [

            {

                "step": 1,

                "title": "Understand Query"

            }

        ],

        "final_reasoning":

            "Adaptive Context Compression improves memory efficiency."

    }

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

    verifier = Verifier()

    result = verifier.verify(

        reasoning,

        memories

    )

    verifier.pretty_print(

        result

    )