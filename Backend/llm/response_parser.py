"""
Adaptive Context Intelligence Engine (ACIE)
Response Parser
"""


class ResponseParser:

    def __init__(self):

        pass

    # -----------------------------------------
    # Parse Response
    # -----------------------------------------

    def parse(self, llm_response):

        print("\n========== RESPONSE PARSER ==========\n")

        parsed = {

            "model": llm_response.get(

                "model",

                "Unknown"

            ),

            "response": llm_response.get(

                "response",

                ""

            ),

            "tokens_used": llm_response.get(

                "tokens_used",

                0

            ),

            "status": llm_response.get(

                "status",

                "UNKNOWN"

            )

        }

        return parsed

    # -----------------------------------------
    # Pretty Print
    # -----------------------------------------

    def pretty_print(self, parsed):

        print("\n========== PARSED RESPONSE ==========\n")

        print("Model        :", parsed["model"])

        print("Status       :", parsed["status"])

        print("Tokens Used  :", parsed["tokens_used"])

        print()

        print("Response")

        print("--------------------------------")

        print(parsed["response"])


if __name__ == "__main__":

    response = {

        "model": "gpt-5.5",

        "response":

        "Adaptive Context Compression reduces token usage while preserving important information.",

        "tokens_used": 52,

        "status": "SUCCESS"

    }

    parser = ResponseParser()

    parsed = parser.parse(

        response

    )

    parser.pretty_print(

        parsed

    )