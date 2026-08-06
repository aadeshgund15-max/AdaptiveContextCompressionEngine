"""
Adaptive Context Intelligence Engine (ACIE)

Agent Orchestrator

Controls complete autonomous agent workflow.
"""


from Backend.agent.task_manager import TaskManager
from Backend.agent.state_manager import StateManager
from Backend.agent.execution_engine import ExecutionEngine
from Backend.agent.tool_router import ToolRouter
from Backend.agent.response_generator import ResponseGenerator


from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline


from Backend.llm.llm_client import LLMClient



class Orchestrator:


    def __init__(self):


        print("\n========== INITIALIZING ACIE AGENT ==========\n")


        # Core managers

        self.task_manager = TaskManager()

        self.state_manager = StateManager()

        self.tool_router = ToolRouter()



        # Pipelines

        self.memory_pipeline = MemoryPipeline()

        self.retrieval_pipeline = RetrievalPipeline()



        # LLM

        self.llm_client = LLMClient(
            model="gemini"
        )



        # Response generator

        self.response_generator = ResponseGenerator(
            llm_client=self.llm_client
        )



        # Execution Engine

        self.execution_engine = ExecutionEngine(

            task_manager=self.task_manager,

            state_manager=self.state_manager,

            tool_router=self.tool_router,

            llm_client=self.llm_client,

            response_generator=self.response_generator

        )



    # ------------------------------------------------

    # Create Agent Plan

    # ------------------------------------------------


    def create_plan(self):


        tasks = [

            "Collect Context",

            "Retrieve Memories",

            "Reason",

            "Generate Response"

        ]


        for task in tasks:

            self.task_manager.add_task(task)


        return tasks



    # ------------------------------------------------

    # Execute Agent

    # ------------------------------------------------


    def execute(

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
            "\n========== ACIE ORCHESTRATOR ==========\n"
        )



        # Start state


        self.state_manager.start()

        self.state_manager.set_goal(query)



        # Clear previous tasks

        task_clear = getattr(
            self.task_manager,
            "clear_tasks",
            None
        )

        if callable(task_clear):
            task_clear()



        # Create plan

        plan = self.create_plan()



        print(
            "Agent Plan:",
            plan
        )



        # ----------------------------
        # Memory Processing
        # ----------------------------


        memory_result = self.memory_pipeline.process(

            query=query,

            conversation=conversation,

            documents=documents

        )



        # ----------------------------
        # Retrieval
        # ----------------------------


        retrieval_result = self.retrieval_pipeline.retrieve(

            query=query,

            memories=
            memory_result.get(
                "consolidated_memories",
                []
            ),

            token_budget=100

        )



        # ----------------------------
        # Task Execution
        # ----------------------------


        execution_history=[]



        while True:


            task = self.task_manager.get_next_task()


            if task is None:

                break



            tool = self.tool_router.select_tool(task)


            self.state_manager.set_tool(tool)



            print(
                "\nExecuting:",
                task
            )


            result = self.execution_engine.execute_task(
                task
            )


            execution_history.append(result)




        # ----------------------------
        # Generate AI Answer
        # ----------------------------


        response_result = self.response_generator.generate(

            query=query,

            memory_result=memory_result,

            retrieval_result=retrieval_result

        )



        self.state_manager.stop()



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



            "agent_state":

            self.state_manager.get_state(),



            "task_status":

            self.task_manager.status(),



            "execution_history":

            execution_history

        }



if __name__=="__main__":



    agent = Orchestrator()



    result = agent.execute(

        query="Explain quantum computing"

    )


    print("\n========== FINAL OUTPUT ==========\n")


    print(result["response"])