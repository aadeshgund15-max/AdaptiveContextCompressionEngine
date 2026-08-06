"""
Adaptive Context Intelligence Engine (ACIE)

Agent Controller

Main entry point for:
- User interaction
- Agent lifecycle
- Query processing
- Pipeline coordination
- Response handling
"""


from typing import Any

from Backend.agent.kernel import AgentKernel
from Backend.agent.reasoning_engine import ReasoningEngine
from Backend.agent.working_memory import WorkingMemory
from Backend.agent.conversation_manager import ConversationManager
from Backend.agent.action_history import ActionHistory



class AgentController:


    def __init__(self):


        print(
            "\n========== ACIE CONTROLLER INITIALIZED ==========\n"
        )


        # Core Kernel

        self.kernel = AgentKernel()


        # Intelligence Modules

        self.reasoning_engine = ReasoningEngine()


        self.working_memory = WorkingMemory()


        self.conversation_manager = ConversationManager()


        self.action_history = ActionHistory()



        self.status_state = "READY"



    # -------------------------------------------------
    # Process User Query
    # -------------------------------------------------


    def chat(

        self,

        query:str,

        conversation=None,

        documents=None

    )->dict[str,Any]:


        print(

            "\n========== ACIE AGENT REQUEST ==========\n"

        )


        if conversation is None:

            conversation=[]


        if documents is None:

            documents=[]



        try:


            self.status_state="RUNNING"



            # ---------------------------------
            # Store Conversation
            # ---------------------------------


            self.conversation_manager.add_message(

                "user",

                query

            )



            # ---------------------------------
            # Working Memory
            # ---------------------------------


            self.working_memory.set_context_window(

                {

                    "query": query,

                    "documents": documents

                }

            )



            # ---------------------------------
            # Reasoning
            # ---------------------------------


            reasoning_result = (

                self.reasoning_engine.reason(

                    query=query,

                    context=conversation

                )

            )



            # ---------------------------------
            # Run ACIE Kernel
            # ---------------------------------


            agent_result = self.kernel.execution_engine.run(

                context=conversation

            )



            # ---------------------------------
            # Save History
            # ---------------------------------


            self.action_history.record(

                action="query_processed",

                component="agent_controller",

                input_data=query,

                output_data=agent_result,

                metadata={

                    "reasoning": reasoning_result

                }

            )



            self.status_state="COMPLETED"



            return {


                "status":

                "SUCCESS",


                "query":

                query,


                "reasoning":

                reasoning_result,


                "agent_result":

                agent_result,


                "controller_status":

                self.status_state

            }



        except Exception as e:



            self.status_state="FAILED"



            return {


                "status":

                "ERROR",


                "error":

                str(e),


                "controller_status":

                self.status_state

            }




    # -------------------------------------------------
    # Agent Status
    # -------------------------------------------------


    def status(self):


        return {


            "controller":

            self.status_state,


            "kernel":

            self.kernel.status(),


            "reasoning":

            self.reasoning_engine.status()


        }




    # -------------------------------------------------
    # Reset Agent
    # -------------------------------------------------


    def reset(self):


        self.working_memory.clear()


        self.conversation_manager.sessions = {}


        self.conversation_manager.current_session = None


        self.status_state="READY"



        return {


            "message":

            "Agent reset successfully"


        }




# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__=="__main__":


    agent = AgentController()



    response = agent.chat(

        "Explain quantum computing"

    )



    print(

        response

    )


    print()


    print(

        agent.status()

    )