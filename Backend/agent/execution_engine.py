"""
Adaptive Context Intelligence Engine (ACIE)

Execution Engine

Responsible for:
- Executing agent actions
- Connecting tools
- Managing LLM execution
- Tracking history
"""


from datetime import datetime
from typing import Any
from Backend.data_structures.linked_list import LinkedList



class ExecutionEngine:


    def __init__(

        self,

        task_manager,

        state_manager,

        tool_router=None,

        llm_client=None,

        response_generator=None

    ):


        self.task_manager = task_manager

        self.state_manager = state_manager

        self.tool_router = tool_router

        self.llm_client = llm_client

        self.response_generator = response_generator


        self.execution_history = LinkedList()



    # ==================================================
    # Execute Task
    # ==================================================


    def execute_task(

        self,

        task:str,

        context=None

    )->dict[str,Any]:


        print(
            f"\nExecuting Task : {task}"
        )


        self.state_manager.set_task(task)



        result: dict[str, Any] = {

            "task": task,

            "timestamp":
            datetime.now().isoformat(),

            "status": "started"

        }



        try:


            tool=None


            if self.tool_router:

                tool=self.tool_router.select_tool(task)



            result["tool"]=tool



            output=self.execute_action(

                task,

                context

            )


            result["output"]=output


            result["status"]="completed"



            self.task_manager.complete_task(task)



        except Exception as e:


            result["status"]="failed"

            result["error"]=str(e)



        self.execution_history.append(
            result["task"],
            result
            )



        return result





    # ==================================================
    # Action Router
    # ==================================================


    def execute_action(

        self,

        task,

        context=None

    ):


        task=task.lower()



        # ------------------------------
        # Context Collection
        # ------------------------------

        if "context" in task:


            return {

                "action":
                "context_collection",

                "status":
                "completed"

            }




        # ------------------------------
        # Retrieval
        # ------------------------------


        if "retrieve" in task:


            return {

                "action":
                "memory_retrieval",

                "status":
                "completed"

            }





        # ------------------------------
        # Reasoning
        # ------------------------------


        if "reason" in task:


            return {


                "action":
                "reasoning",


                "status":
                "completed"


            }





        # ------------------------------
        # Response
        # ------------------------------


        if "response" in task:

            return self.call_llm(
                context
            )

        return {
            "action": "generic",
            "message": task
        }

    # ==================================================
    # Execution History
    # ==================================================

    def get_execution_history(self):

        return self.execution_history.to_list()






    # ==================================================
    # LLM Execution
    # ==================================================


    def call_llm(self, context=None):
        context = context or {}

        if not self.response_generator:
            return {
                "response": "Response generator unavailable"
            }

        response = self.response_generator.generate(
            query=context.get("query"),
            memory_result=context.get("memory"),
            retrieval_result=context.get("retrieval"),
            reasoning_result=context.get("reasoning")
        )

        return response






    # ==================================================
    # Run All Tasks
    # ==================================================


    def run(self, context=None):

        results = []

        self.state_manager.start()

        try:

            while True:

                task = self.task_manager.get_next_task()

                if task is None:
                    break

                result = self.execute_task(task, context)

                results.append(result)

        finally:

            self.state_manager.stop()

        return {

    "results": results,

    "history": self.get_execution_history(),

    "state": self.state_manager.get_state()

}