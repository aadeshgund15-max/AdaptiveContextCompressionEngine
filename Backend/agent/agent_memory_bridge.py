"""
Adaptive Context Intelligence Engine (ACIE)

Agent Memory Bridge

Responsible for:
- Connecting short-term memory
- Connecting long-term memory
- Syncing conversation state
- Context preparation
- Memory retrieval
- Memory storage
"""


from datetime import datetime
from typing import Any



class AgentMemoryBridge:


    def __init__(

        self,

        working_memory=None,

        conversation_manager=None,

        memory_pipeline=None,

        retrieval_pipeline=None

    ):


        self.working_memory = working_memory

        self.conversation_manager = conversation_manager

        self.memory_pipeline = memory_pipeline

        self.retrieval_pipeline = retrieval_pipeline



    # -------------------------------------------------
    # Load Context
    # -------------------------------------------------

    def load_context(

        self,

        query:str,

        conversation=None

    ):


        context = {


            "query":

            query,


            "conversation":

            conversation or [],


            "timestamp":

            datetime.now().isoformat()


        }


        # Store in working memory

        if self.working_memory:


            self.working_memory.set_goal(

                query

            )


            self.working_memory.set_context_window(

                context

            )


        return context



    # -------------------------------------------------
    # Retrieve Long Term Memory
    # -------------------------------------------------

    def retrieve_memory(

        self,

        query:str

    ):


        if not self.retrieval_pipeline:


            return []



        result = (

            self.retrieval_pipeline.retrieve(

                query=query,

                memories=[],

                token_budget=200

            )

        )


        memories = result.get(

            "ranked_memories",

            []

        )


        if self.working_memory:


            self.working_memory.set_retrieved_memories(

                memories

            )


        return memories



    # -------------------------------------------------
    # Store Important Memory
    # -------------------------------------------------

    def store_memory(

        self,

        data:dict

    ):


        if not self.memory_pipeline:


            return None



        result = self.memory_pipeline.process(

            query=data.get(

                "query",

                ""

            ),

            conversation=data.get(

                "conversation",

                []

            ),

            documents=data.get(

                "documents",

                []

            )

        )


        return result



    # -------------------------------------------------
    # Synchronize
    # -------------------------------------------------

    def synchronize(self):


        state = {}



        if self.working_memory:


            state["working_memory"] = (

                self.working_memory.export()

            )



        if self.conversation_manager:


            state["conversation"] = (

                self.conversation_manager.export()

            )


        return state



    # -------------------------------------------------
    # Build Agent Context
    # -------------------------------------------------

    def build_agent_context(

        self

    ):


        context = {}



        if self.working_memory:


            wm = self.working_memory.export()


            context.update({


                "goal":

                wm["goal"],


                "plan":

                wm["plan"],


                "reasoning":

                wm["reasoning_notes"],


                "retrieved_memories":

                wm["retrieved_memories"]

            })



        return context



    # -------------------------------------------------
    # Status
    # -------------------------------------------------

    def status(self):


        return {


            "working_memory":

            self.working_memory is not None,


            "conversation_manager":

            self.conversation_manager is not None,


            "memory_pipeline":

            self.memory_pipeline is not None,


            "retrieval_pipeline":

            self.retrieval_pipeline is not None


        }



# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__=="__main__":


    bridge = AgentMemoryBridge()


    print(

        bridge.status()

    )


    print(

        bridge.load_context(

            "Explain quantum computing"

        )

    )