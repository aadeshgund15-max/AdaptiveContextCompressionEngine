"""
Adaptive Context Intelligence Engine (ACIE)

Tool Executor

Responsible for:
- Dynamic tool execution
- Tool registration
- Tool management
- Execution tracking
- Error handling
"""


from __future__ import annotations

from datetime import datetime
from typing import Any, Callable, Dict


class ToolExecutor:


    def __init__(self):

        self.tools: Dict[str, Callable] = {}

        self.execution_history = []


    # -------------------------------------------------
    # Register Tool
    # -------------------------------------------------

    def register_tool(

        self,

        name: str,

        function: Callable

    ):

        self.tools[name] = function


    # -------------------------------------------------
    # Remove Tool
    # -------------------------------------------------

    def remove_tool(

        self,

        name: str

    ):

        if name in self.tools:

            del self.tools[name]


    # -------------------------------------------------
    # Check Tool
    # -------------------------------------------------

    def available(

        self,

        name: str

    ) -> bool:

        return name in self.tools


    # -------------------------------------------------
    # Execute Tool
    # -------------------------------------------------

    def execute(

        self,

        tool_name: str,

        *args,

        **kwargs

    ) -> Dict[str,Any]:


        execution = {


            "tool":

            tool_name,


            "status":

            "started",


            "timestamp":

            datetime.now().isoformat()


        }


        try:


            if tool_name not in self.tools:


                raise Exception(

                    f"Tool '{tool_name}' not found"

                )


            result = self.tools[tool_name](

                *args,

                **kwargs

            )


            execution["result"] = result


            execution["status"] = "completed"



        except Exception as e:


            execution["status"] = "failed"

            execution["error"] = str(e)



        self.execution_history.append(

            execution

        )


        return execution



    # -------------------------------------------------
    # Execute Chain
    # -------------------------------------------------

    def execute_chain(

        self,

        chain:list[str]

    ):


        results = []


        for tool in chain:


            results.append(

                self.execute(tool)

            )


        return results



    # -------------------------------------------------
    # Tool List
    # -------------------------------------------------

    def list_tools(self):


        return list(

            self.tools.keys()

        )


    # -------------------------------------------------
    # History
    # -------------------------------------------------

    def history(self):


        return self.execution_history



    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    def status(self):


        return {


            "registered_tools":

            len(self.tools),


            "executions":

            len(self.execution_history)


        }



# -------------------------------------------------
# Example Tools
# -------------------------------------------------

def calculator_tool(a,b):

    return a+b



def memory_tool():

    return {

        "message":

        "Memory retrieved"

    }



# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__ == "__main__":


    executor = ToolExecutor()


    executor.register_tool(

        "calculator",

        calculator_tool

    )


    executor.register_tool(

        "memory",

        memory_tool

    )


    print(

        executor.status()

    )


    print(

        executor.execute(

            "calculator",

            10,

            20

        )

    )


    print(

        executor.execute(

            "memory"

        )

    )