"""
Adaptive Context Intelligence Engine (ACIE)

Goal Manager

Responsible for:
- Goal creation
- Goal tracking
- Goal hierarchy
- Progress monitoring
- Goal completion
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


# ---------------------------------------------------------
# Goal Model
# ---------------------------------------------------------

@dataclass
class Goal:

    id: int

    title: str

    description: str = ""

    priority: int = 1

    status: str = "ACTIVE"

    progress: float = 0.0

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )

    completed_at: Optional[str] = None

    sub_goals: List[int] = field(default_factory=list)

    metadata: Dict = field(default_factory=dict)


# ---------------------------------------------------------
# Goal Manager
# ---------------------------------------------------------

class GoalManager:

    def __init__(self):

        self.goals: Dict[int, Goal] = {}

        self.current_goal: Optional[int] = None

        self.goal_counter = 0

    # -------------------------------------------------

    def create_goal(

        self,

        title: str,

        description: str = "",

        priority: int = 1

    ) -> Goal:

        self.goal_counter += 1

        goal = Goal(

            id=self.goal_counter,

            title=title,

            description=description,

            priority=priority

        )

        self.goals[goal.id] = goal

        self.current_goal = goal.id

        return goal

    # -------------------------------------------------

    def add_sub_goal(

        self,

        parent_id: int,

        title: str,

        description: str = "",

        priority: int = 1

    ) -> Goal:

        sub_goal = self.create_goal(

            title,

            description,

            priority

        )

        self.goals[parent_id].sub_goals.append(

            sub_goal.id

        )

        return sub_goal

    # -------------------------------------------------

    def set_current_goal(

        self,

        goal_id: int

    ):

        if goal_id in self.goals:

            self.current_goal = goal_id

    # -------------------------------------------------

    def get_current_goal(self):

        if self.current_goal is None:

            return None

        return self.goals[self.current_goal]

    # -------------------------------------------------

    def update_progress(

        self,

        goal_id: int,

        progress: float

    ):

        if goal_id not in self.goals:

            return

        progress = max(

            0.0,

            min(progress, 100.0)

        )

        self.goals[goal_id].progress = progress

        if progress >= 100:

            self.complete_goal(goal_id)

    # -------------------------------------------------

    def complete_goal(

        self,

        goal_id: int

    ):

        if goal_id not in self.goals:

            return

        goal = self.goals[goal_id]

        goal.status = "COMPLETED"

        goal.progress = 100

        goal.completed_at = datetime.now().isoformat()

    # -------------------------------------------------

    def fail_goal(

        self,

        goal_id: int

    ):

        if goal_id in self.goals:

            self.goals[goal_id].status = "FAILED"

    # -------------------------------------------------

    def remove_goal(

        self,

        goal_id: int

    ):

        if goal_id in self.goals:

            del self.goals[goal_id]

    # -------------------------------------------------

    def active_goals(self):

        return [

            goal

            for goal in self.goals.values()

            if goal.status == "ACTIVE"

        ]

    # -------------------------------------------------

    def completed_goals(self):

        return [

            goal

            for goal in self.goals.values()

            if goal.status == "COMPLETED"

        ]

    # -------------------------------------------------

    def export(self):

        return [

            {

                "id": goal.id,

                "title": goal.title,

                "status": goal.status,

                "progress": goal.progress,

                "priority": goal.priority,

                "sub_goals": goal.sub_goals

            }

            for goal in self.goals.values()

        ]

    # -------------------------------------------------

    def status(self):

        return {

            "current_goal": self.current_goal,

            "total_goals": len(self.goals),

            "active_goals": len(self.active_goals()),

            "completed_goals": len(self.completed_goals())

        }


# ---------------------------------------------------------
# Demo
# ---------------------------------------------------------

if __name__ == "__main__":

    manager = GoalManager()

    goal = manager.create_goal(

        "Build ACIE Agent",

        "Develop autonomous AI agent"

    )

    manager.add_sub_goal(

        goal.id,

        "Planner Module"

    )

    manager.add_sub_goal(

        goal.id,

        "Working Memory"

    )

    manager.update_progress(

        goal.id,

        35

    )

    print(manager.status())

    print()

    print(manager.export())