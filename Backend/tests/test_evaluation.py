"""
Evaluation Module Tests
"""


from Backend.evaluation.metrics import EvaluationMetrics
from Backend.evaluation.comparison import CompressionComparison



def test_compression_ratio():

    ratio = EvaluationMetrics.compression_ratio(
        1000,
        500
    )


    assert ratio == 0.5



def test_token_reduction():

    reduction = EvaluationMetrics.token_reduction(
        1000,
        500
    )


    assert reduction == 50



def test_comparison():

    result = CompressionComparison.compare(
        1000,
        400
    )


    assert result["tokens_saved"] == 600


    assert result["saving_percentage"] == 60