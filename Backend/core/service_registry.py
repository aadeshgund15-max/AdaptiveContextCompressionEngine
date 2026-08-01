"""
Adaptive Context Intelligence Engine (ACIE)
Service Registry
"""

from Backend.services.embedding_service import EmbeddingService


class ServiceRegistry:

    _embedding_service = None

    @classmethod
    def get_embedding_service(cls):

        if cls._embedding_service is None:

            cls._embedding_service = EmbeddingService()

        return cls._embedding_service