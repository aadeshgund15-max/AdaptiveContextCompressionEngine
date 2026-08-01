"""
Adaptive Context Intelligence Engine (ACIE)
Tool Router
"""


class ToolRouter:

    def __init__(self):

        self.available_tools = {

            "memory": "Memory Pipeline",

            "retrieval": "Retrieval Pipeline",

            "reasoning": "Reasoning Engine",

            "planning": "Planner",

            "browser": "Browser Agent",

            "vision": "Vision Agent",

            "python": "Python Executor"

        }

    # ---------------------------------

    def select_tool(self, task):

        task = task.lower()

        if "memory" in task:

            return self.available_tools["memory"]

        elif "retrieve" in task:

            return self.available_tools["retrieval"]

        elif "reason" in task:

            return self.available_tools["reasoning"]

        elif "plan" in task:

            return self.available_tools["planning"]

        elif "browser" in task or "search" in task:

            return self.available_tools["browser"]

        elif "image" in task or "vision" in task:

            return self.available_tools["vision"]

        elif "python" in task or "code" in task:

            return self.available_tools["python"]

        return "Unknown Tool"

    # ---------------------------------

    def list_tools(self):

        return self.available_tools


if __name__ == "__main__":

    router = ToolRouter()

    tasks = [

        "Retrieve Memory",

        "Reason about context",

        "Plan solution",

        "Search browser",

        "Analyze image",

        "Run python code"

    ]

    print("\n========== TOOL ROUTER ==========\n")

    for task in tasks:

        tool = router.select_tool(task)

        print(f"{task} -> {tool}")