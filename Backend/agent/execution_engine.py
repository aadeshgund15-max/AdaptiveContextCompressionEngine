"""
Adaptive Context Intelligence Engine (ACIE)
Execution Engine
"""


class ExecutionEngine:

    def __init__(

        self,

        task_manager,

        state_manager

    ):

        self.task_manager = task_manager

        self.state_manager = state_manager

    # ---------------------------------
    # Execute One Task
    # ---------------------------------

    def execute_task(self, task):

        print(f"\nExecuting -> {task}")

        self.state_manager.set_task(task)

        # Simulated execution

        print(f"Completed -> {task}")

        self.task_manager.complete_task(task)

    # ---------------------------------
    # Execute All Tasks
    # ---------------------------------

    def run(self):

        print("\n========== EXECUTION ENGINE ==========\n")

        self.state_manager.start()

        while True:

            task = self.task_manager.get_next_task()

            if task is None:

                break

            self.execute_task(task)

        self.state_manager.stop()

        return {

            "task_status": self.task_manager.status(),

            "agent_state": self.state_manager.get_state()

        }