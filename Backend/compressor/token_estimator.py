"""
Adaptive Context Intelligence Engine (ACIE)
Token Estimator
"""


class TokenEstimator:
    """
    Estimates the number of tokens in a text.
    Approximation:
    1 token ≈ 0.75 words
    """

    def __init__(self):
        pass

    def estimate(self, text):

        if not text:
            return 0

        words = len(text.split())

        estimated_tokens = int(words / 0.75)

        return estimated_tokens


if __name__ == "__main__":

    estimator = TokenEstimator()

    sample = """
    Adaptive Context Compression improves LLM memory efficiency.
    """

    print("Text:")
    print(sample)

    print("\nEstimated Tokens:")
    print(estimator.estimate(sample))