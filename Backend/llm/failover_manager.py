"""
Adaptive Context Intelligence Engine (ACIE)
Failover Manager
"""

from Backend.llm.llm_client import LLMClient


class FailoverManager:

    def __init__(self):

        # Priority order
        self.providers = [

            "groq",
            "gemini",
            "ollama"

        ]

    # -------------------------------------------------
    # Generate Response
    # -------------------------------------------------

    def generate(

        self,

        prompt,

        preferred_provider=None

    ):

        providers = self.providers.copy()

        # Put preferred provider first
        if preferred_provider:

            preferred_provider = preferred_provider.lower()

            if preferred_provider in providers:

                providers.remove(preferred_provider)

                providers.insert(0, preferred_provider)

        last_error = None

        for provider in providers:

            print()

            print("=" * 60)
            print(f"Trying Provider : {provider.upper()}")
            print("=" * 60)

            try:

                client = LLMClient(

                    model=provider

                )

                response = client.generate(

                    prompt

                )

                # Success
                if isinstance(response, dict):

                    if response.get("success", True):

                        print(f"{provider.upper()} SUCCESS")

                        return response

                # Failure returned
                print(f"{provider.upper()} FAILED")

                last_error = response

            except Exception as e:

                print(f"{provider.upper()} EXCEPTION")

                print(e)

                last_error = str(e)

        return {

            "success": False,

            "provider": None,

            "response": "",

            "error": last_error

        }

    # -------------------------------------------------
    # Health Check
    # -------------------------------------------------

    def health_check(self):

        result = {}

        for provider in self.providers:

            try:

                client = LLMClient(

                    model=provider

                )

                result[provider] = client.provider.health_check()

            except Exception:

                result[provider] = False

        return result


if __name__ == "__main__":

    manager = FailoverManager()

    print()

    print("Provider Health")

    print("----------------")

    print(manager.health_check())

    print()

    response = manager.generate(

        "Explain Artificial Intelligence in 100 words."

    )

    print()

    print(response)