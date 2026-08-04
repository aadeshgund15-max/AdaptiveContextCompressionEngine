"""
Adaptive Context Intelligence Engine (ACIE)
Pytest Fixtures
"""

import pytest

from fastapi.testclient import TestClient

from Backend.api.app import app

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline
from Backend.reasoning.reasoning_engine import ReasoningEngine
from Backend.core.pipeline_manager import PipelineManager
from Backend.llm.llm_client import LLMClient


# ==========================================
# FastAPI Client
# ==========================================

@pytest.fixture(scope="session")
def client():

    return TestClient(app)


# ==========================================
# Memory Pipeline
# ==========================================

@pytest.fixture(scope="session")
def memory_pipeline():

    return MemoryPipeline()


# ==========================================
# Retrieval Pipeline
# ==========================================

@pytest.fixture(scope="session")
def retrieval_pipeline():

    return RetrievalPipeline()


# ==========================================
# Reasoning Engine
# ==========================================

@pytest.fixture(scope="session")
def reasoning_engine():

    return ReasoningEngine()


# ==========================================
# Complete Pipeline
# ==========================================

@pytest.fixture(scope="session")
def pipeline_manager():

    return PipelineManager()


# ==========================================
# LLM Clients
# ==========================================

@pytest.fixture(params=["groq", "gemini", "ollama"])
def llm_client(request):

    return LLMClient(

        model=request.param

    )


# ==========================================
# Sample Query
# ==========================================

@pytest.fixture
def sample_query():

    return "Explain Adaptive Context Compression."


# ==========================================
# Sample Conversation
# ==========================================

@pytest.fixture
def sample_conversation():

    return [

        "What is Retrieval-Augmented Generation?",

        "Explain Vector Databases."

    ]


# ==========================================
# Sample Documents
# ==========================================

@pytest.fixture
def sample_documents():

    return [

        "Research Paper A",

        "Research Paper B"

    ]