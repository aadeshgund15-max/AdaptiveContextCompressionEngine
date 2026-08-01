"""
Adaptive Context Intelligence Engine (ACIE)
Request Models
"""

from pydantic import BaseModel


class StoreRequest(BaseModel):

    query: str

    conversation: list[str]

    documents: list[str]


class RetrieveRequest(BaseModel):

    query: str

    top_k: int = 5


class CompressRequest(BaseModel):

    memories: list[str]


class ContextRequest(BaseModel):

    query: str

    token_budget: int = 100

    top_k: int = 10


class SummarizeRequest(BaseModel):

    memories: list[str]