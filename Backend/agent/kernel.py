"""
Adaptive Context Intelligence Engine (ACIE)
Agent Kernel
"""

from Backend.agent.task_manager import TaskManager
from Backend.agent.state_manager import StateManager
from Backend.agent.tool_router import ToolRouter
from Backend.agent.execution_engine import ExecutionEngine

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline


class AgentKernel:

    def __init__(self):

        print("\n========== INITIALIZING ACIE ==========\n")

        # Shared Managers

        self.task_manager = TaskManager()

        self.state_manager = StateManager()

        self.tool_router = ToolRouter()

        # Shared Pipelines

        self.memory_pipeline = MemoryPipeline()

        self.retrieval_pipeline = RetrievalPipeline()

        # Execution Engine (provide shared managers required by ExecutionEngine)

        self.execution_engine = ExecutionEngine(self.task_manager, self.state_manager)

    # ---------------------------------------

    def status(self):

        return {

            "task_manager": "READY",

            "state_manager": "READY",

            "tool_router": "READY",

            "memory_pipeline": "READY",

            "retrieval_pipeline": "READY",

            "execution_engine": "READY"

        }


if __name__ == "__main__":

    kernel = AgentKernel()

    print(kernel.status())