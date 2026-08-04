"""
ACIE Baseline Comparison

Compare normal context processing
against ACIE compression.
"""


class CompressionComparison:


    @staticmethod
    def compare(
        baseline_tokens: int,
        compressed_tokens: int
    ) -> dict:


        tokens_saved = (
            baseline_tokens
            -
            compressed_tokens
        )


        saving_percentage = (

            tokens_saved
            /
            baseline_tokens

        ) * 100


        return {


            "baseline_tokens":
                baseline_tokens,


            "compressed_tokens":
                compressed_tokens,


            "tokens_saved":
                tokens_saved,


            "saving_percentage":
                saving_percentage

        }