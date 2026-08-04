"""
Adaptive Context Intelligence Engine (ACIE)
Token Budget Manager
"""


class TokenBudgetManager:

    def __init__(self):

        self.default_context = 32000

        self.default_reserved_output = 4000

    # -----------------------------------------
    # Estimate Tokens
    # -----------------------------------------

    def estimate_tokens(

        self,

        text

    ):

        if text is None:

            return 0

        return len(str(text).split())

    # -----------------------------------------
    # Calculate Budget
    # -----------------------------------------

    def calculate(

        self,

        prompt,

        max_context,

        reserved_output=1000

    ):

        print("\n========== TOKEN BUDGET ==========\n")

        prompt_tokens = self.estimate_tokens(

            prompt

        )

        available = (

            max_context
            - prompt_tokens
            - reserved_output

        )

        if available < 0:

            available = 0

        return {

            "prompt_tokens": prompt_tokens,

            "reserved_output_tokens": reserved_output,

            "available_context_tokens": available,

            "max_context": max_context

        }

    # -----------------------------------------
    # Check Overflow
    # -----------------------------------------

    def fits(

        self,

        prompt,

        max_context

    ):

        tokens = self.estimate_tokens(

            prompt

        )

        return tokens <= max_context

    # =====================================================
    # Compatibility Methods
    # =====================================================

    def fit(self, prompt):

        """
        Pipeline compatibility.
        Returns the original prompt if it fits.
        """

        budget = self.calculate(

            prompt,

            self.default_context,

            self.default_reserved_output

        )

        print("\nToken Budget:", budget)

        return prompt

    def optimize(self, prompt):

        return self.fit(prompt)

    def apply(self, prompt):

        return self.fit(prompt)

    def truncate(self, prompt):

        return self.fit(prompt)


if __name__ == "__main__":

    manager = TokenBudgetManager()

    prompt = """

    Adaptive Context Compression improves
    memory retrieval using semantic search
    and vector databases.

    """

    result = manager.calculate(

        prompt,

        max_context=8000,

        reserved_output=1000

    )

    print("\n========== RESULT ==========\n")

    print(result)

    print(

        "\nFits Context:",

        manager.fits(

            prompt,

            8000

        )

    )