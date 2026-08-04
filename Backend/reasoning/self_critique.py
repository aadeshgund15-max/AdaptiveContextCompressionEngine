"""
Adaptive Context Intelligence Engine (ACIE)
Self Critique
"""


class SelfCritique:

    def __init__(self):

        pass

    # ---------------------------------
    # Evaluate Response
    # ---------------------------------

    def critique(

        self,

        response,

        verifier_report

    ):

        print("\n========== SELF CRITIQUE ==========\n")

        score = 100

        improvements = []

        if not verifier_report["verified"]:

            score -= 40

            improvements.append(

                "Verification failed."

            )

        if verifier_report["confidence"] < 80:

            score -= 20

            improvements.append(

                "Confidence is low."

            )

        if len(response.strip()) < 40:

            score -= 20

            improvements.append(

                "Response is too short."

            )

        if len(response.split()) < 10:

            score -= 10

            improvements.append(

                "Response needs more details."

            )

        if len(improvements) == 0:

            improvements.append(

                "Response quality is excellent."

            )

        if score < 0:

            score = 0

        quality = "Excellent"

        if score < 90:

            quality = "Good"

        if score < 75:

            quality = "Average"

        if score < 60:

            quality = "Poor"

        return {

            "quality": quality,

            "score": score,

            "improvements": improvements

        }

    # ---------------------------------

    def pretty_print(

        self,

        report

    ):

        print("\n========== CRITIQUE REPORT ==========\n")

        print("Quality :", report["quality"])

        print("Score   :", report["score"])

        print()

        print("Suggestions")

        for suggestion in report["improvements"]:

            print("-", suggestion)


if __name__ == "__main__":

    response = (

        "Adaptive Context Compression reduces "

        "token usage while preserving "

        "important information."

    )

    verifier = {

        "verified": True,

        "confidence": 95

    }

    critique = SelfCritique()

    result = critique.critique(

        response,

        verifier

    )

    critique.pretty_print(

        result

    )