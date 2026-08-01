"""
Adaptive Context Intelligence Engine (ACIE)
Configuration
"""


class Config:

    EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

    DEFAULT_TOP_K = 5

    DEFAULT_TOKEN_BUDGET = 100

    DATABASE_NAME = "acie.db"

    COLLECTION_NAME = "acie_memory"

    DEBUG = True