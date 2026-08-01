"""
Adaptive Context Intelligence Engine (ACIE)
Response Generator
"""


class ResponseGenerator:

    def __init__(self):

        pass

    # --------------------------------------------------

    def generate(

        self,

        query,

        memory_result,

        retrieval_result

    ):

        print("\n========== RESPONSE GENERATOR ==========\n")

        response = {

            "query": query,

            "decision": memory_result["decision"],

            "importance": memory_result["importance"],

            "confidence": memory_result["confidence"],

            "memory_id": memory_result["memory_id"],

            "summary": memory_result["summary"],

            "context_window": retrieval_result["context_window"],

            "knowledge_graph": memory_result["knowledge_graph"],

            "retrieved_memories": retrieval_result["ranked_memories"]

        }

        return response

    # --------------------------------------------------

    def pretty_print(self, response):

        print("\n========== FINAL RESPONSE ==========\n")

        print(f"Query : {response['query']}")

        print(f"\nDecision : {response['decision']}")

        print(f"Importance : {response['importance']}")

        print(f"Confidence : {response['confidence']}")

        print(f"Memory ID : {response['memory_id']}")

        print("\nSummary")

        print(response["summary"])

        print("\nKnowledge Graph")

        print(response["knowledge_graph"])

        print("\nContext Window")

        print(response["context_window"])

        print("\nRetrieved Memories")

        for memory in response["retrieved_memories"]:

            print(memory)


if __name__ == "__main__":

    generator = ResponseGenerator()

    memory_result = {

        "memory_id": 1,

        "importance": 95,

        "confidence": 0.94,

        "decision": "STORE",

        "summary": "Adaptive Context Compression stores important memories.",

        "knowledge_graph": {

            "nodes": 8,

            "relationships": 5

        }

    }

    retrieval_result = {

        "context_window": {

            "selected_count": 2,

            "used_tokens": 18

        },

        "ranked_memories": [

            {

                "query": "Adaptive Context Compression",

                "ranking_score": 92

            },

            {

                "query": "Semantic Retrieval",

                "ranking_score": 88

            }

        ]

    }

    response = generator.generate(

        query="Explain Adaptive Context Compression",

        memory_result=memory_result,

        retrieval_result=retrieval_result

    )

    generator.pretty_print(

        response

    )