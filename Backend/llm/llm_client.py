"""
Adaptive Context Intelligence Engine (ACIE)
LLM Client
"""

from Backend.llm.providers.provider_factory import ProviderFactory


class LLMClient:

    def __init__(

        self,

        model="gemini"

    ):

        self.provider = ProviderFactory.create(

            model

        )

    # ----------------------------------------
    # Generate Response
    # ----------------------------------------

    def generate(

        self,

        prompt,

        temperature=0.3,

        max_tokens=2048

    ):

        return self.provider.generate(

            prompt=prompt,

            temperature=temperature,

            max_tokens=max_tokens

        )

    # ----------------------------------------
    # Streaming
    # ----------------------------------------

    def stream(

        self,

        prompt,

        temperature=0.3,

        max_tokens=2048

    ):

        return self.provider.stream(

            prompt=prompt,

            temperature=temperature,

            max_tokens=max_tokens

        )

    # ----------------------------------------
    # Health Check
    # ----------------------------------------

    def health_check(self):

        return self.provider.health_check()

    # ----------------------------------------
    # Provider Information
    # ----------------------------------------

    def info(self):

        return self.provider.info()


if __name__ == "__main__":

    client = LLMClient()

    print()

    print(client.info())

    print()

    response = client.generate(

        "Explain Adaptive Context Compression in simple words."

    )

    print(response)

    print()

    print("Streaming")

    print("-" * 40)

    for chunk in client.stream(

        "What is Artificial Intelligence?"

    ):

        print(

            chunk,

            end="",

            flush=True

        )