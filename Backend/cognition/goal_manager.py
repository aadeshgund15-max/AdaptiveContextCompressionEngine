"""
Adaptive Context Intelligence Engine (ACIE)
Goal Manager
"""


from datetime import datetime


class GoalManager:

    def __init__(self):

        self.goals = []

    # ---------------------------------
    # Create Goal
    # ---------------------------------

    def create_goal(

        self,

        goal,

        priority="MEDIUM"

    ):

        item = {

            "id": len(self.goals) + 1,

            "goal": goal,

            "priority": priority,

            "status": "ACTIVE",

            "progress": 0,

            "created_at": datetime.now().strftime(

                "%Y-%m-%d %H:%M:%S"

            )

        }

        self.goals.append(item)

        return item

    # ---------------------------------
    # Update Progress
    # ---------------------------------

    def update_progress(

        self,

        goal_id,

        progress

    ):

        for goal in self.goals:

            if goal["id"] == goal_id:

                goal["progress"] = progress

                if progress >= 100:

                    goal["status"] = "COMPLETED"

                return goal

        return None

    # ---------------------------------
    # Get Active Goals
    # ---------------------------------

    def active_goals(self):

        return [

            goal

            for goal in self.goals

            if goal["status"] == "ACTIVE"

        ]

    # ---------------------------------
    # Get Completed Goals
    # ---------------------------------

    def completed_goals(self):

        return [

            goal

            for goal in self.goals

            if goal["status"] == "COMPLETED"

        ]

    # ---------------------------------
    # Build Goal from Planner
    # ---------------------------------

    def process(

        self,

        plan

    ):

        print("\n========== GOAL MANAGER ==========\n")

        goal = self.create_goal(

            goal=plan["goal"],

            priority=plan["complexity"]

        )

        return {

            "goal": goal,

            "active_goals": self.active_goals(),

            "completed_goals": self.completed_goals()

        }


if __name__ == "__main__":

    manager = GoalManager()

    plan = {

        "goal": "Explain Adaptive Context Compression",

        "complexity": "MEDIUM"

    }

    result = manager.process(

        plan

    )

    print("\n========== RESULT ==========\n")

    print(result)

    manager.update_progress(

        1,

        100

    )

    print("\nAfter Completion\n")

    print(manager.completed_goals())