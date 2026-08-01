"""
Adaptive Context Intelligence Engine (ACIE)
Reasoning Engine
"""


class ReasoningEngine:

    def __init__(self):

        pass

    # ---------------------------------
    # Extract Important Memories
    # ---------------------------------

    def extract(self, memories):

        extracted = []

        for memory in memories:

            extracted.append(

                memory["text"]

            )

        return extracted

    # ---------------------------------
    # Build Context
    # ---------------------------------

    def build_context(self, memories):

        context = ""

        for memory in memories:

            context += "- " + memory + "\n"

        return context

    # ---------------------------------
    # Generate Reasoning
    # ---------------------------------

    def reason(

        self,

        query,

        context

    ):

        reasoning = {

            "query": query,

            "context": context,

            "conclusion":

                "Based on the retrieved memories, "

                "the available information is relevant "

                "to answering the query."

        }

        return reasoning

    # ---------------------------------
    # Complete Pipeline
    # ---------------------------------

    def process(

        self,

        query,

        memories

    ):

        print("\n========== REASONING ENGINE ==========\n")

        extracted = self.extract(

            memories

        )

        context = self.build_context(

            extracted

        )

        reasoning = self.reason(

            query,

            context

        )

        return reasoning


if __name__ == "__main__":

    memories = [

        {

            "text": "Adaptive Context Compression reduces token usage."

        },

        {

            "text": "Semantic Retrieval improves memory search."

        },

        {

            "text": "Knowledge Graph connects related memories."

        }

    ]

    engine = ReasoningEngine()

    result = engine.process(

        query="Explain Adaptive Context Compression",

        memories=memories

    )

    print("\n========== RESULT ==========\n")

    print(result)
    