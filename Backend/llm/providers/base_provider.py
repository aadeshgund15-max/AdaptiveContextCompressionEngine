"""
Adaptive Context Intelligence Engine (ACIE)
Base Provider
"""

from abc import ABC, abstractmethod
from typing import Any, Generator


class BaseProvider(ABC):

    def __init__(self, model_name: str):
        self.model_name = model_name

    # -------------------------------------------------
    # Generate Response
    # -------------------------------------------------

    @abstractmethod
    def generate(
        self,
        prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 2048
    ) -> dict[str, Any]:
        """
        Generate a response from the provider.
        """
        pass

    # -------------------------------------------------
    # Streaming Response
    # -------------------------------------------------

    @abstractmethod
    def stream(
        self,
        prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 2048
    ) -> Generator[str, None, None]:
        """
        Stream response from provider.
        """
        pass

    # -------------------------------------------------
    # Health Check
    # -------------------------------------------------

    def health_check(self) -> dict[str, Any]:
        """
        Default health check.
        Providers can override this.
        """
        return {
            "status": "healthy",
            "provider": self.__class__.__name__,
            "model": self.model_name,
            "available": True
        }

    # -------------------------------------------------
    # Provider Information
    # -------------------------------------------------

    def info(self) -> dict[str, Any]:
        return {
            "provider": self.__class__.__name__,
            "model": self.model_name,
            "available": True
        }