"""
Adaptive Context Intelligence Engine (ACIE)
Application Settings
"""

from __future__ import annotations

from Backend.config.environment import environment
from Backend.config import constants


class Settings:

    # -------------------------------------------------
    # Project
    # -------------------------------------------------

    PROJECT_NAME = constants.PROJECT_NAME

    VERSION = constants.API_VERSION

    # -------------------------------------------------
    # Providers
    # -------------------------------------------------

    GEMINI_API_KEY = environment.get(

        "GEMINI_API_KEY"

    )

    GROQ_API_KEY = environment.get(

        "GROQ_API_KEY"

    )

    OLLAMA_HOST = environment.get(

        "OLLAMA_HOST",

        "http://localhost:11434"

    )

    # -------------------------------------------------
    # Model
    # -------------------------------------------------

    DEFAULT_PROVIDER = constants.DEFAULT_PROVIDER

    DEFAULT_MODEL = constants.DEFAULT_MODEL

    # -------------------------------------------------
    # Token Budget
    # -------------------------------------------------

    MAX_CONTEXT_TOKENS = constants.MAX_CONTEXT_TOKENS

    RESERVED_OUTPUT_TOKENS = constants.RESERVED_OUTPUT_TOKENS

    # -------------------------------------------------
    # Cache
    # -------------------------------------------------

    CACHE_TTL = constants.CACHE_TTL

    EMBEDDING_CACHE_TTL = constants.EMBEDDING_CACHE_TTL

    CACHE_MAX_ENTRIES = constants.CACHE_MAX_ENTRIES

    # -------------------------------------------------
    # Retrieval
    # -------------------------------------------------

    TOP_K = constants.TOP_K

    SIMILARITY_THRESHOLD = constants.SIMILARITY_THRESHOLD


settings = Settings()