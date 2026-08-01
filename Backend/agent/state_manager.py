"""
Adaptive Context Intelligence Engine (ACIE)
State Manager
"""


from datetime import datetime


class StateManager:

    def __init__(self):

        self.state = {

            "agent_status": "IDLE",

            "current_goal": None,

            "current_task": None,

            "current_plan": None,

            "current_tool": None,

            "current_context": None,

            "reasoning_state": None,

            "started_at": None,

            "updated_at": None

        }

    # ---------------------------------

    def _update_timestamp(self):

        self.state["updated_at"] = datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

    # ---------------------------------

    def start(self):

        self.state["agent_status"] = "RUNNING"

        self.state["started_at"] = datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

        self._update_timestamp()

    # ---------------------------------

    def stop(self):

        self.state["agent_status"] = "IDLE"

        self._update_timestamp()

    # ---------------------------------

    def set_goal(self, goal):

        self.state["current_goal"] = goal

        self._update_timestamp()

    # ---------------------------------

    def set_task(self, task):

        self.state["current_task"] = task

        self._update_timestamp()

    # ---------------------------------

    def set_plan(self, plan):

        self.state["current_plan"] = plan

        self._update_timestamp()

    # ---------------------------------

    def set_tool(self, tool):

        self.state["current_tool"] = tool

        self._update_timestamp()

    # ---------------------------------

    def set_context(self, context):

        self.state["current_context"] = context

        self._update_timestamp()

    # ---------------------------------

    def set_reasoning(self, reasoning):

        self.state["reasoning_state"] = reasoning

        self._update_timestamp()

    # ---------------------------------

    def get_state(self):

        return self.state


if __name__ == "__main__":

    manager = StateManager()

    manager.start()

    manager.set_goal(

        "Answer user's question"

    )

    manager.set_task(

        "Retrieve memories"

    )

    manager.set_plan(

        [

            "Retrieve",

            "Reason",

            "Respond"

        ]

    )

    manager.set_tool(

        "Memory Pipeline"

    )

    manager.set_context(

        "Adaptive Context Compression"

    )

    manager.set_reasoning(

        "Reasoning in progress"

    )

    print(

        "\n========== AGENT STATE ==========\n"

    )

    print(

        manager.get_state()

    )

    manager.stop()