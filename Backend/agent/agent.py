"""
Adaptive Context Intelligence Engine (ACIE)

Autonomous AI Agent

Responsible for:
- Agent initialization
- User interaction
- Orchestrating complete reasoning cycle
- Returning final AI response
"""


from typing import Any


from Backend.agent.kernel import AgentKernel
from Backend.agent.orchestrator import Orchestrator



class ACIEAgent:


    def __init__(self):

        print(
            "\n========== INITIALIZING ACIE AGENT ==========\n"
        )


        # ----------------------------
        # Agent Kernel
        # ----------------------------

        self.kernel = AgentKernel()


        print(
            "Agent Kernel Ready"
        )


        # ----------------------------
        # Agent Orchestrator
        # ----------------------------

        self.orchestrator = Orchestrator()



    # ------------------------------------------------
    # Chat Interface
    # ------------------------------------------------


    def chat(

        self,

        query: str,

        conversation=None,

        documents=None

    ) -> dict[str,Any]:


        if conversation is None:

            conversation = []


        if documents is None:

            documents = []



        print(
            "\nUSER QUERY:"
        )


        print(query)



        # ----------------------------------
        # Run Agent
        # ----------------------------------


        result = self.orchestrator.execute(

            query=query,

            conversation=conversation,

            documents=documents

        )

        if result is None:
            result = {}


        # ----------------------------------
        # Prepare Final Output
        # ----------------------------------


        response = {


            "query":

            query,


            "answer":

            result.get(

                "response",

                {}

            ),


            "memory":

            result.get(

                "memory",

                {}

            ),


            "retrieval":

            result.get(

                "retrieval",

                {}

            ),


            "agent_state":

            result.get(

                "agent_state",

                {}

            ),


            "task_status":

            result.get(

                "task_status",

                {}

            ),


            "execution_history":

            result.get(

                "execution_history",

                []

            )


        }



        return response




    # ------------------------------------------------
    # Agent Status
    # ------------------------------------------------


    def status(self):


        return {


            "agent":

            "ACIE",


            "kernel":

            self.kernel.status(),


            "orchestrator":

            "READY"


        }




# ==================================================
# MAIN EXECUTION
# ==================================================


if __name__ == "__main__":



    agent = ACIEAgent()



    print(

        "\n========== ACIE AUTONOMOUS AGENT ==========\n"

    )



    result = agent.chat(


        query=

        "Explain quantum computing"



    )



    print(

        "\n========== FINAL ANSWER ==========\n"

    )


    answer = result.get(

        "answer",

        {}

    )


    if isinstance(answer,dict):


        print(

            answer.get(

                "answer",

                answer

            )

        )


    else:


        print(answer)



    print(

        "\n========== AGENT STATE ==========\n"

    )


    print(

        result["agent_state"]

    )