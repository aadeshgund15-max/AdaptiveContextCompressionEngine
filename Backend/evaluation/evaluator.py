"""
ACIE Evaluation Controller
"""


from Backend.evaluation.metrics import EvaluationMetrics
from Backend.evaluation.semantic_similarity import SemanticSimilarity



class ACIEEvaluator:


    def __init__(
        self,
        embedding_model
    ):

        self.semantic = SemanticSimilarity(
            embedding_model
        )



    def evaluate(
        self,
        original_context,
        compressed_context,
        original_tokens,
        compressed_tokens
    ):


        similarity = self.semantic.calculate(
            original_context,
            compressed_context
        )


        return {


            "compression_ratio":
                EvaluationMetrics.compression_ratio(
                    original_tokens,
                    compressed_tokens
                ),


            "token_reduction":
                EvaluationMetrics.token_reduction(
                    original_tokens,
                    compressed_tokens
                ),


            "semantic_similarity":
                similarity

        }