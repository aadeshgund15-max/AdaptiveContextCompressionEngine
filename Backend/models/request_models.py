"""
Adaptive Context Intelligence Engine (ACIE)
Request Models
"""

from typing import List

from pydantic import BaseModel


class StoreRequest(BaseModel):

    query: str

    conversation: List[str]

    documents: List[str]


class RetrieveRequest(BaseModel):

    query: str

    top_k: int = 5