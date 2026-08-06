"""
Adaptive Context Intelligence Engine (ACIE)

Planner

Responsible for:
- Goal decomposition
- Task planning
- Task prioritization
- Dependency management
- Dynamic replanning
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional


# ---------------------------------------------------------
# Task Model
# ---------------------------------------------------------

@dataclass
class PlanTask:

    id: int

    name: str

    priority: int = 1

    status: str = "PENDING"

    depends_on: List[int] = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)


# ---------------------------------------------------------
# Planner
# ---------------------------------------------------------

class Planner:

    def __init__(self):

        self.goal: str = ""

        self.tasks: List[PlanTask] = []

        self.plan_history: List[Dict] = []

    # -----------------------------------------------------

    def set_goal(self, goal: str):

        self.goal = goal

    # -----------------------------------------------------

    def create_plan(self, goal: str) -> List[PlanTask]:

        self.goal = goal

        self.tasks = [

            PlanTask(
                id=1,
                name="Collect Context",
                priority=1
            ),

            PlanTask(
                id=2,
                name="Retrieve Memories",
                priority=2,
                depends_on=[1]
            ),

            PlanTask(
                id=3,
                name="Reason",
                priority=3,
                depends_on=[2]
            ),

            PlanTask(
                id=4,
                name="Generate Response",
                priority=4,
                depends_on=[3]
            )

        ]

        self.plan_history.append({

            "goal": goal,

            "created_at": datetime.now().isoformat(),

            "task_count": len(self.tasks)

        })

        return self.tasks

    # -----------------------------------------------------

    def add_task(

        self,

        name: str,

        priority: int = 5,

        depends_on: Optional[List[int]] = None

    ):

        if depends_on is None:
            depends_on = []

        task = PlanTask(

            id=len(self.tasks) + 1,

            name=name,

            priority=priority,

            depends_on=depends_on

        )

        self.tasks.append(task)

    # -----------------------------------------------------

    def remove_task(self, task_id: int):

        self.tasks = [

            task

            for task in self.tasks

            if task.id != task_id

        ]

    # -----------------------------------------------------

    def update_status(

        self,

        task_id: int,

        status: str

    ):

        for task in self.tasks:

            if task.id == task_id:

                task.status = status

                return

    # -----------------------------------------------------

    def next_task(self):

        for task in sorted(

            self.tasks,

            key=lambda t: t.priority

        ):

            if task.status == "PENDING":

                return task

        return None

    # -----------------------------------------------------

    def completed(self):

        return all(

            task.status == "COMPLETED"

            for task in self.tasks

        )

    # -----------------------------------------------------

    def replan(self):

        """
        Placeholder for future dynamic replanning.
        """

        pending = [

            task

            for task in self.tasks

            if task.status == "PENDING"

        ]

        pending.sort(

            key=lambda t: t.priority

        )

        self.tasks = pending

    # -----------------------------------------------------

    def export(self):

        return [

            {

                "id": task.id,

                "name": task.name,

                "priority": task.priority,

                "status": task.status,

                "depends_on": task.depends_on

            }

            for task in self.tasks

        ]

    # -----------------------------------------------------

    def status(self):

        return {

            "goal": self.goal,

            "task_count": len(self.tasks),

            "completed": self.completed()

        }


# ---------------------------------------------------------
# Demo
# ---------------------------------------------------------

if __name__ == "__main__":

    planner = Planner()

    planner.create_plan(

        "Explain Quantum Computing"

    )

    print()

    print(planner.status())

    print()

    for task in planner.export():

        print(task)