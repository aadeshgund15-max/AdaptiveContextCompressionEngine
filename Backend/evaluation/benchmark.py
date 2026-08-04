"""
ACIE Compression Benchmark

Runs compression experiments.
"""


from Backend.evaluation.metrics import EvaluationMetrics



class CompressionBenchmark:


    def __init__(self, compressor):

        self.compressor = compressor



    def run(
        self,
        context: str
    ) -> dict:


        result = self.compressor.compress(
            context
        )


        original_tokens = (
            result["original_tokens"]
        )


        compressed_tokens = (
            result["compressed_tokens"]
        )


        return {


            "original_tokens":
                original_tokens,


            "compressed_tokens":
                compressed_tokens,


            "compression_ratio":
                EvaluationMetrics.compression_ratio(
                    original_tokens,
                    compressed_tokens
                ),


            "token_reduction":
                EvaluationMetrics.token_reduction(
                    original_tokens,
                    compressed_tokens
                )

        }