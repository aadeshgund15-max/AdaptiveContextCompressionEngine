"""
Adaptive Context Intelligence Engine (ACIE)
Token Estimator
"""


class TokenEstimator:

    def estimate_tokens(self, text):

        words = text.split()

        estimated_tokens = int(len(words) * 1.3)

        return estimated_tokens


if __name__ == "__main__":

    estimator = TokenEstimator()

    sentence = "Adaptive context compression reduces prompt size."

    print("Sentence:")
    print(sentence)

    print()

    print("Estimated Tokens:")
    print(estimator.estimate_tokens(sentence))