"""
Adaptive Context Intelligence Engine (ACIE)
API Schemas
"""

from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Field


# =====================================================
# Base Response
# =====================================================

class APIResponse(BaseModel):

    success: bool = True

    message: str

    data: Optional[Dict[str, Any]] = None


# =====================================================
# Chat
# =====================================================

class ChatRequest(BaseModel):

    query: str = Field(

        ...,

        description="User query"

    )


class ChatResponse(BaseModel):

    response: str

    status: str


# =====================================================
# Complete Engine
# =====================================================

class EngineRequest(BaseModel):

    query: str

    conversation: List[str] = []

    documents: List[str] = []

    requires_retrieval: bool = True

    task_type: str = "general"


class EngineResponse(BaseModel):

    memory: Dict[str, Any]

    retrieval: Optional[Dict[str, Any]]

    reasoning: Dict[str, Any]

    prompt: str

    model: Dict[str, Any]

    response: Dict[str, Any]


# =====================================================
# Memory
# =====================================================

class MemoryRequest(BaseModel):

    query: str

    conversation: List[str] = []

    documents: List[str] = []


class MemoryResponse(BaseModel):

    stored: bool

    memory_id: Optional[int] = None

    importance: float

    confidence: float

    decision: str


# =====================================================
# Retrieval
# =====================================================

class RetrievalRequest(BaseModel):

    query: str

    top_k: int = 5


class RetrievalResponse(BaseModel):

    query: str

    results: List[Any]


# =====================================================
# Compression
# =====================================================

class CompressionRequest(BaseModel):

    memories: List[Any]


class CompressionResponse(BaseModel):

    compressed_memories: List[Any]

    compression_ratio: float

    tokens_saved: int


# =====================================================
# Context Builder
# =====================================================

class ContextRequest(BaseModel):

    query: str

    top_k: int = 5

    token_budget: int = 1000


class ContextResponse(BaseModel):

    query: str

    result: Dict[str, Any]


# =====================================================
# Health
# =====================================================

class HealthResponse(BaseModel):

    status: str

    message: str


# =====================================================
# Agent Status
# =====================================================

class AgentStatusResponse(BaseModel):

    agent: str

    memory: str

    retrieval: str

    reasoning: str

    llm: str

    api: str