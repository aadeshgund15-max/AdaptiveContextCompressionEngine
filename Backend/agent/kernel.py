"""
Adaptive Context Intelligence Engine (ACIE)

Agent Kernel

Central nervous system of ACIE agent.

Responsible for:
- Initializing agent modules
- Connecting pipelines
- Running complete agent cycle
- Managing execution flow
"""


from Backend.agent.task_manager import TaskManager
from Backend.agent.state_manager import StateManager
from Backend.agent.tool_router import ToolRouter
from Backend.agent.execution_engine import ExecutionEngine
from Backend.agent.response_generator import ResponseGenerator

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline

from Backend.reasoning.reasoning_engine import ReasoningEngine

from Backend.llm.llm_client import LLMClient



class AgentKernel:



    def __init__(self):


        print(
            "\n========== INITIALIZING ACIE AGENT ==========\n"
        )


        # -----------------------------
        # Core Managers
        # -----------------------------


        self.task_manager = TaskManager()


        self.state_manager = StateManager()


        self.tool_router = ToolRouter()



        # -----------------------------
        # Intelligence Modules
        # -----------------------------


        self.memory_pipeline = MemoryPipeline()


        self.retrieval_pipeline = RetrievalPipeline()


        self.reasoning_engine = ReasoningEngine()



        # -----------------------------
        # LLM Layer
        # -----------------------------


        self.llm_client = LLMClient(

            model="gemini"

        )


        self.response_generator = ResponseGenerator(

            llm_client=self.llm_client

        )



        # -----------------------------
        # Execution Layer
        # -----------------------------


        self.execution_engine = ExecutionEngine(

            task_manager=self.task_manager,

            state_manager=self.state_manager,

            tool_router=self.tool_router,

            llm_client=self.llm_client,

            response_generator=self.response_generator

        )


        print(
            "Agent Kernel Ready"
        )



    # =================================================
    # MAIN AGENT EXECUTION
    # =================================================


    def run(

        self,

        query,

        conversation=None,

        documents=None

    ):



        if conversation is None:

            conversation=[]


        if documents is None:

            documents=[]



        print(

            "\n========== ACIE KERNEL RUN ==========\n"

        )



        # ---------------------------------
        # Memory Processing
        # ---------------------------------


        memory_result = self.memory_pipeline.process(

            query=query,

            conversation=conversation,

            documents=documents

        )



        # ---------------------------------
        # Retrieval
        # ---------------------------------


        retrieval_result = self.retrieval_pipeline.retrieve(

            query=query,

            memories=

            memory_result.get(

                "consolidated_memories",

                []

            ),

            token_budget=100

        )



        # ---------------------------------
        # Reasoning
        # ---------------------------------


        reasoning_result = self.reasoning_engine.process(

            query=query,

            retrieved_memories=retrieval_result.get("memories", []),

            draft_response=""

        )



        # ---------------------------------
        # Generate Answer
        # ---------------------------------


        response_result = self.response_generator.generate(

            query=query,

            memory_result=memory_result,

            retrieval_result=retrieval_result,

            reasoning_result=reasoning_result

        )



        return {


            "status":

            "SUCCESS",


            "query":

            query,


            "response":

            response_result,


            "memory":

            memory_result,


            "retrieval":

            retrieval_result,


            "reasoning":

            reasoning_result,


            "agent_state":

            self.state_manager.get_state()

        }




    # =================================================
    # STATUS
    # =================================================


    def status(self):


        return {


            "agent":

            "READY",


            "components":

            {


            "task_manager":

            "READY",


            "state_manager":

            "READY",


            "tool_router":

            "READY",


            "memory_pipeline":

            "READY",


            "retrieval_pipeline":

            "READY",


            "reasoning_engine":

            "READY",


            "execution_engine":

            "READY",


            "llm":

            "READY"

            }

        }





if __name__=="__main__":


    kernel=AgentKernel()


    result = kernel.run(

        query="Explain quantum computing"

    )


    print(result)