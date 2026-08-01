"""
Adaptive Context Intelligence Engine (ACIE)
Task Manager
"""


class TaskManager:

    def __init__(self):

        self.pending_tasks = []

        self.completed_tasks = []

        self.failed_tasks = []

    # ---------------------------------

    def add_task(self, task):

        self.pending_tasks.append(task)

    # ---------------------------------

    def get_next_task(self):

        if not self.pending_tasks:
            return None

        return self.pending_tasks.pop(0)

    # ---------------------------------

    def complete_task(self, task):

        self.completed_tasks.append(task)

    # ---------------------------------

    def fail_task(self, task):

        self.failed_tasks.append(task)

    # ---------------------------------

    def status(self):

        return {

            "pending": len(self.pending_tasks),

            "completed": len(self.completed_tasks),

            "failed": len(self.failed_tasks)

        }


if __name__ == "__main__":

    manager = TaskManager()

    manager.add_task("Collect Context")
    manager.add_task("Retrieve Memory")
    manager.add_task("Reason")
    manager.add_task("Generate Response")

    while True:

        task = manager.get_next_task()

        if task is None:
            break

        print(task)

        manager.complete_task(task)

    print(manager.status())
