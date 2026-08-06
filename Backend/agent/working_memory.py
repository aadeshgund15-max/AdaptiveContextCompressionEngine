"""
Adaptive Context Intelligence Engine (ACIE)

Working Memory

Responsible for:
- Short-term agent memory
- Current reasoning state
- Scratchpad
- Context management
- Tool outputs
- Intermediate results
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


# ---------------------------------------------------------
# Working Memory State
# ---------------------------------------------------------

@dataclass
class WorkingMemoryState:

    goal: str = ""

    current_task: str = ""

    plan: list[str] = field(default_factory=list)

    retrieved_memories: list[Any] = field(default_factory=list)

    context_window: dict = field(default_factory=dict)

    reasoning_notes: list[str] = field(default_factory=list)

    observations: list[str] = field(default_factory=list)

    tool_outputs: dict[str, Any] = field(default_factory=dict)

    intermediate_results: dict[str, Any] = field(default_factory=dict)

    final_response: str = ""

    token_usage: dict[str, int] = field(default_factory=lambda: {

        "input_tokens": 0,

        "output_tokens": 0,

        "total_tokens": 0

    })

    metadata: dict[str, Any] = field(default_factory=lambda: {

        "created_at": datetime.now().isoformat(),

        "updated_at": datetime.now().isoformat()

    })


# ---------------------------------------------------------
# Working Memory
# ---------------------------------------------------------

class WorkingMemory:

    def __init__(self):

        self.memory = WorkingMemoryState()

    # -------------------------------------------------

    def set_goal(self, goal: str):

        self.memory.goal = goal

        self._touch()

    # -------------------------------------------------

    def set_plan(self, plan: list[str]):

        self.memory.plan = plan

        self._touch()

    # -------------------------------------------------

    def set_current_task(self, task: str):

        self.memory.current_task = task

        self._touch()

    # -------------------------------------------------

    def set_context_window(self, context: dict):

        self.memory.context_window = context

        self._touch()

    # -------------------------------------------------

    def set_retrieved_memories(self, memories):

        self.memory.retrieved_memories = memories

        self._touch()

    # -------------------------------------------------

    def add_reasoning(self, note: str):

        self.memory.reasoning_notes.append(note)

        self._touch()

    # -------------------------------------------------

    def add_observation(self, observation: str):

        self.memory.observations.append(observation)

        self._touch()

    # -------------------------------------------------

    def add_tool_output(

        self,

        tool_name: str,

        output: Any

    ):

        self.memory.tool_outputs[tool_name] = output

        self._touch()

    # -------------------------------------------------

    def add_intermediate_result(

        self,

        key: str,

        value: Any

    ):

        self.memory.intermediate_results[key] = value

        self._touch()

    # -------------------------------------------------

    def set_final_response(

        self,

        response: str

    ):

        self.memory.final_response = response

        self._touch()

    # -------------------------------------------------

    def update_token_usage(

        self,

        input_tokens: int,

        output_tokens: int

    ):

        self.memory.token_usage["input_tokens"] = input_tokens

        self.memory.token_usage["output_tokens"] = output_tokens

        self.memory.token_usage["total_tokens"] = (

            input_tokens + output_tokens

        )

        self._touch()

    # -------------------------------------------------

    def clear(self):

        self.memory = WorkingMemoryState()

    # -------------------------------------------------

    def export(self):

        return {

            "goal": self.memory.goal,

            "current_task": self.memory.current_task,

            "plan": self.memory.plan,

            "retrieved_memories": self.memory.retrieved_memories,

            "context_window": self.memory.context_window,

            "reasoning_notes": self.memory.reasoning_notes,

            "observations": self.memory.observations,

            "tool_outputs": self.memory.tool_outputs,

            "intermediate_results": self.memory.intermediate_results,

            "final_response": self.memory.final_response,

            "token_usage": self.memory.token_usage,

            "metadata": self.memory.metadata

        }

    # -------------------------------------------------

    def status(self):

        return {

            "goal": self.memory.goal,

            "current_task": self.memory.current_task,

            "reasoning_steps": len(

                self.memory.reasoning_notes

            ),

            "observations": len(

                self.memory.observations

            ),

            "tools_used": len(

                self.memory.tool_outputs

            )

        }

    # -------------------------------------------------

    def _touch(self):

        self.memory.metadata["updated_at"] = (

            datetime.now().isoformat()

        )


# ---------------------------------------------------------
# Demo
# ---------------------------------------------------------

if __name__ == "__main__":

    wm = WorkingMemory()

    wm.set_goal(

        "Explain Quantum Computing"

    )

    wm.set_plan([

        "Collect Context",

        "Retrieve Memories",

        "Reason",

        "Generate Response"

    ])

    wm.set_current_task(

        "Retrieve Memories"

    )

    wm.add_reasoning(

        "Searching long-term memory."

    )

    wm.add_observation(

        "2 relevant memories found."

    )

    wm.add_tool_output(

        "Retriever",

        {

            "count": 2

        }

    )

    wm.add_intermediate_result(

        "similarity",

        0.92

    )

    wm.update_token_usage(

        420,

        210

    )

    print()

    print(wm.status())

    print()

    print(wm.export())