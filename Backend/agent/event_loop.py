"""
Adaptive Context Intelligence Engine (ACIE)
Event Loop
"""

import time

from Backend.agent.task_manager import TaskManager
from Backend.agent.state_manager import StateManager
from Backend.agent.execution_engine import ExecutionEngine


class EventLoop:

    def __init__(self):

        self.task_manager = TaskManager()

        self.state_manager = StateManager()

        self.execution_engine = ExecutionEngine(self.task_manager, self.state_manager)

        self.running = False

    # ---------------------------------

    def start(self):

        print("\n========== EVENT LOOP STARTED ==========\n")

        self.running = True

        self.state_manager.start()

        while self.running:

            task = self.task_manager.get_next_task()

            if task is None:

                time.sleep(1)

                continue

            self.execution_engine.execute_task(task)

            if task.lower() == "shutdown":

                self.stop()

    # ---------------------------------

    def stop(self):

        print("\n========== EVENT LOOP STOPPED ==========\n")

        self.running = False

        self.state_manager.stop()

    # ---------------------------------

    def add_task(self, task):

        self.task_manager.add_task(task)


if __name__ == "__main__":

    loop = EventLoop()

    loop.add_task("Collect Context")

    loop.add_task("Retrieve Memories")

    loop.add_task("Reason")

    loop.add_task("Generate Response")

    loop.add_task("Shutdown")

    loop.start()