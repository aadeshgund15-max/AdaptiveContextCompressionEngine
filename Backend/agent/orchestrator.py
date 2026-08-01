"""
Adaptive Context Intelligence Engine (ACIE)
Agent Orchestrator
"""

from Backend.agent.task_manager import TaskManager
from Backend.agent.state_manager import StateManager
from Backend.agent.execution_engine import ExecutionEngine
from Backend.agent.tool_router import ToolRouter

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline


class Orchestrator:

    def __init__(
        self,
        task_manager=None,
        state_manager=None,
        execution_engine=None,
        tool_router=None,
        memory_pipeline=None,
        retrieval_pipeline=None,
    ):

        self.task_manager = task_manager or TaskManager()

        self.state_manager = state_manager or StateManager()

        self.execution_engine = execution_engine or ExecutionEngine(
            task_manager=self.task_manager,
            state_manager=self.state_manager,
        )

        self.tool_router = tool_router or ToolRouter()

        self.memory_pipeline = memory_pipeline or MemoryPipeline()

        self.retrieval_pipeline = retrieval_pipeline or RetrievalPipeline()

    # --------------------------------------------------

    def initialize(self, query):

        print("\n========== ORCHESTRATOR ==========\n")

        self.state_manager.start()

        self.state_manager.set_goal(query)

        self.task_manager.add_task("Collect Context")

        self.task_manager.add_task("Retrieve Memories")

        self.task_manager.add_task("Reason")

        self.task_manager.add_task("Generate Response")

    # --------------------------------------------------

    def execute(

        self,

        query,

        conversation,

        documents

    ):

        self.initialize(query)

        # ----------------------------
        # Memory Pipeline
        # ----------------------------

        print("\nRunning Memory Pipeline...\n")

        memory_result = self.memory_pipeline.process(

            query=query,

            conversation=conversation,

            documents=documents

        )

        # ----------------------------
        # Retrieval Pipeline
        # ----------------------------

        print("\nRunning Retrieval Pipeline...\n")

        retrieval_result = self.retrieval_pipeline.retrieve(

            query=query,

            memories=memory_result["consolidated_memories"],

            token_budget=100

        )

        # ----------------------------
        # Execute Tasks
        # ----------------------------

        print("\nExecuting Tasks...\n")

        while True:

            task = self.task_manager.get_next_task()

            if task is None:

                break

            tool = self.tool_router.select_tool(task)

            self.state_manager.set_tool(tool)

            print("------------------------------------")

            print("Task :", task)

            print("Tool :", tool)

            self.execution_engine.execute_task(task)

        self.state_manager.stop()

        return {

            "memory": memory_result,

            "retrieval": retrieval_result,

            "agent_state": self.state_manager.get_state(),

            "task_status": self.task_manager.status()

        }


if __name__ == "__main__":

    orchestrator = Orchestrator(
        task_manager=TaskManager(),
        state_manager=StateManager()
    )

    result = orchestrator.execute(

        query="Explain Adaptive Context Compression.",

        conversation=[

            "What is semantic retrieval?",

            "Explain vector databases."

        ],

        documents=[

            "Research Paper A",

            "Research Paper B"

        ]

    )

    print("\n========== FINAL RESULT ==========\n")

    print(result)