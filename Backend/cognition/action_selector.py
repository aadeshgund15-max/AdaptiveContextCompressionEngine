"""
Adaptive Context Intelligence Engine (ACIE)
Action Selector
"""


class ActionSelector:

    def __init__(self):

        pass

    # ---------------------------------
    # Decide Next Action
    # ---------------------------------

    def decide(self, inference, plan, goal):

        confidence = inference["confidence"]

        gaps = inference["knowledge_gaps"]

        if confidence < 0.60:

            return {

                "action": "RETRIEVE_MORE",

                "reason": "Low confidence."

            }

        if len(gaps) > 0:

            return {

                "action": "SEARCH",

                "reason": "Knowledge gaps detected."

            }

        if plan["task_count"] > 3:

            return {

                "action": "PLAN",

                "reason": "Complex task."

            }

        if goal["goal"]["status"] == "ACTIVE":

            return {

                "action": "RESPOND",

                "reason": "Enough information available."

            }

        return {

            "action": "IDLE",

            "reason": "No action required."

        }

    # ---------------------------------
    # Execute Pipeline
    # ---------------------------------

    def process(

        self,

        inference,

        plan,

        goal

    ):

        print("\n========== ACTION SELECTOR ==========\n")

        decision = self.decide(

            inference,

            plan,

            goal

        )

        return decision


if __name__ == "__main__":

    inference = {

        "confidence": 0.91,

        "knowledge_gaps": []

    }

    plan = {

        "task_count": 2

    }

    goal = {

        "goal": {

            "status": "ACTIVE"

        }

    }

    selector = ActionSelector()

    result = selector.process(

        inference,

        plan,

        goal

    )

    print("\n========== RESULT ==========\n")

    print(result)