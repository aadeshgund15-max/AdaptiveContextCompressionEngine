"""
ACIE Evaluation Metrics

Calculates compression performance metrics.
"""


class EvaluationMetrics:


    @staticmethod
    def compression_ratio(
        original_tokens: int,
        compressed_tokens: int
    ) -> float:

        """
        Calculate compression ratio.

        Example:
        Original = 1000
        Compressed = 500

        Ratio = 0.5
        """

        if original_tokens == 0:
            return 0.0


        return compressed_tokens / original_tokens



    @staticmethod
    def token_reduction(
        original_tokens: int,
        compressed_tokens: int
    ) -> float:

        """
        Calculate percentage of tokens removed.
        """

        if original_tokens == 0:
            return 0.0


        return (
            (
                original_tokens
                -
                compressed_tokens
            )
            /
            original_tokens
        ) * 100



    @staticmethod
    def compression_efficiency(
        compressed_tokens: int,
        quality_score: float
    ) -> float:

        """
        Measures retained quality per token.
        """

        if compressed_tokens == 0:
            return 0.0


        return quality_score / compressed_tokens