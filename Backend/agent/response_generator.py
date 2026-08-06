"""
Adaptive Context Intelligence Engine (ACIE)

Response Generator

Responsible for:
- Creating final user response
- Building LLM prompt
- Connecting AI providers
- Returning agent output
"""


from typing import Any



class ResponseGenerator:


    def __init__(

        self,

        llm_client=None

    ):


        self.llm_client = llm_client



    # --------------------------------------------------
    # Generate Final Response
    # --------------------------------------------------


    def generate(

        self,

        query: str,

        memory_result: dict,

        retrieval_result: dict,

        reasoning_result: dict = None # type: ignore

    ) -> dict[str,Any]:


        print(

            "\n========== RESPONSE GENERATOR ==========\n"

        )



        prompt = self.build_prompt(

            query,

            memory_result,

            retrieval_result,

            reasoning_result

        )



        # ----------------------------------
        # LLM Generation
        # ----------------------------------


        if self.llm_client:


            llm_response = (

                self.llm_client.generate(

                    prompt

                )

            )


            answer = (

                llm_response.get(

                    "response",

                    ""

                )

            )


        else:


            answer = (

                "ACIE processed your query using "

                "memory and retrieval pipelines."

            )




        return {


            "query":

            query,


            "answer":

            answer,


            "metadata":{


                "memory_decision":

                memory_result.get(
                    "decision"
                ),


                "importance":

                memory_result.get(
                    "importance"
                ),


                "confidence":

                memory_result.get(
                    "confidence"
                ),


                "memory_id":

                memory_result.get(
                    "memory_id"
                ),



                "retrieved_memories":

                retrieval_result.get(
                    "ranked_memories",
                    []
                ),


                "context_window":

                retrieval_result.get(
                    "context_window",
                    {}
                )

            }

        }



    # --------------------------------------------------
    # Prompt Builder
    # --------------------------------------------------


    def build_prompt(

        self,

        query,

        memory_result,

        retrieval_result,

        reasoning_result=None

    ):


        context = retrieval_result.get(

            "context_window",

            {}

        )


        memories = retrieval_result.get(

            "ranked_memories",

            []

        )


        reasoning = reasoning_result or {}



        prompt = f"""

You are ACIE
(Adaptive Context Intelligence Engine).

Answer the user query using the provided context.

USER QUERY:

{query}


RETRIEVED MEMORY:

{memories}


CONTEXT WINDOW:

{context}


REASONING:

{reasoning}


Provide a clear, accurate and helpful answer.

"""


        return prompt



    # --------------------------------------------------
    # Pretty Print
    # --------------------------------------------------


    def pretty_print(

        self,

        response

    ):


        print(

            "\n========== FINAL RESPONSE ==========\n"

        )


        print(

            response["answer"]

        )


        print(

            "\n========== ACIE METADATA ==========\n"

        )


        for key,value in response["metadata"].items():

            print(

                key,

                ":",

                value

            )




if __name__=="__main__":



    generator = ResponseGenerator()



    result = generator.generate(

        query=

        "Explain Adaptive Context Compression.",


        memory_result={

            "decision":"STORE",

            "importance":90,

            "confidence":0.95,

            "memory_id":1

        },


        retrieval_result={

            "context_window":{

                "tokens":100

            },


            "ranked_memories":[

                "Semantic compression memory"

            ]

        }

    )


    generator.pretty_print(result)