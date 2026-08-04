"""
Adaptive Context Intelligence Engine (ACIE)
Response Processor
"""

from datetime import datetime


class ResponseProcessor:

    def __init__(self):

        pass

    # --------------------------------------------------
    # Format Response
    # --------------------------------------------------

    def format_response(

        self,

        response,

        model=None,

        execution_time=None,

        retrieved_memories=None,

        metadata=None

    ):

        if retrieved_memories is None:
            retrieved_memories = []

        if metadata is None:
            metadata = {}

        return {

            "success": True,

            "timestamp": datetime.now().isoformat(),

            "model": model,

            "execution_time": execution_time,

            "response": response,

            "retrieved_memory_count": len(retrieved_memories),

            "retrieved_memories": retrieved_memories,

            "metadata": metadata

        }

    # --------------------------------------------------
    # Error Response
    # --------------------------------------------------

    def error_response(

        self,

        message,

        error=None

    ):

        return {

            "success": False,

            "timestamp": datetime.now().isoformat(),

            "message": message,

            "error": str(error)

        }

    # --------------------------------------------------
    # API Response
    # --------------------------------------------------

    def api_response(

        self,

        pipeline_result

    ):

        return self.format_response(

            response=pipeline_result.get(

                "response",

                ""

            ),

            model=pipeline_result.get(

                "model",

                None

            ),

            retrieved_memories=pipeline_result.get(

                "retrieval",

                []

            ),

            metadata={

                "reasoning": pipeline_result.get(

                    "reasoning"

                ),

                "memory": pipeline_result.get(

                    "memory"

                )

            }

        )


if __name__ == "__main__":

    processor = ResponseProcessor()

    sample = processor.format_response(

        response="Adaptive Context Compression improves context efficiency.",

        model="gemini",

        execution_time=0.82,

        retrieved_memories=[

            "Memory A",

            "Memory B"

        ],

        metadata={

            "tokens": 412

        }

    )

    print(sample)