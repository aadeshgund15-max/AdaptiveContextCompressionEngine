"""
Adaptive Context Intelligence Engine (ACIE)
Model Registry

Loads AI models only once and shares them
across the entire application.
"""

from sentence_transformers import SentenceTransformer

from Backend.core.config import Config


class ModelRegistry:

    _embedding_model = None

    @classmethod
    def get_embedding_model(cls):

        if cls._embedding_model is None:

            print("\nLoading embedding model...")

            cls._embedding_model = SentenceTransformer(

                Config.EMBEDDING_MODEL

            )

            print("Embedding model loaded successfully.\n")

        return cls._embedding_model