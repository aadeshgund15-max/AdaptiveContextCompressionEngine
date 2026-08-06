"""
Semantic Similarity Evaluation

Measures information preservation
after context compression.
"""


from sentence_transformers import util


class SemanticSimilarity:


    def __init__(self, embedding_model):

        self.embedding_model = embedding_model



    def calculate(
        self,
        original_text: str,
        compressed_text: str
    ) -> float:


        original_embedding = (
            self.embedding_model.encode(
                original_text,
                convert_to_tensor=True
            )
        )


        compressed_embedding = (
            self.embedding_model.encode(
                compressed_text,
                convert_to_tensor=True
            )
        )


        score = util.cos_sim(
            original_embedding,
            compressed_embedding
        )


        return float(score[0][0])