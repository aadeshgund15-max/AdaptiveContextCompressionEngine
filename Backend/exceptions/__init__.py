"""
Adaptive Context Intelligence Engine (ACIE)
Exception Package
"""

from .base_exception import ACIEException

from .memory_exception import (
    MemoryException,
    MemoryStorageException,
    MemoryRetrievalException,
    MemoryCompressionException,
    MemoryReflectionException,
    KnowledgeGraphException,
    WorkingMemoryException,
    LongTermMemoryException,
)

from .retrieval_exception import (
    RetrievalException,
    VectorRetrievalException,
    HybridRetrievalException,
    GraphRetrievalException,
    EmbeddingException,
    FAISSException,
    RankingException,
    ContextWindowException,
)

from .reasoning_exception import (
    ReasoningException,
    PlanningException,
    ChainOfThoughtException,
    ReflectionException,
    VerificationException,
    SelfCritiqueException,
    DecisionTreeException,
    StrategyException,
)

from .llm_exception import (
    LLMException,
    ProviderException,
    APIKeyException,
    PromptBuilderException,
    GenerationException,
    ResponseParserException,
    RouterException,
    TokenBudgetException,
)

from .api_exception import (
    APIException,
    ValidationException,
    AuthenticationException,
    AuthorizationException,
    RequestException,
    PipelineException,
    EndpointException,
)

__all__ = [

    "ACIEException",

    "MemoryException",
    "MemoryStorageException",
    "MemoryRetrievalException",
    "MemoryCompressionException",
    "MemoryReflectionException",
    "KnowledgeGraphException",
    "WorkingMemoryException",
    "LongTermMemoryException",

    "RetrievalException",
    "VectorRetrievalException",
    "HybridRetrievalException",
    "GraphRetrievalException",
    "EmbeddingException",
    "FAISSException",
    "RankingException",
    "ContextWindowException",

    "ReasoningException",
    "PlanningException",
    "ChainOfThoughtException",
    "ReflectionException",
    "VerificationException",
    "SelfCritiqueException",
    "DecisionTreeException",
    "StrategyException",

    "LLMException",
    "ProviderException",
    "APIKeyException",
    "PromptBuilderException",
    "GenerationException",
    "ResponseParserException",
    "RouterException",
    "TokenBudgetException",

    "APIException",
    "ValidationException",
    "AuthenticationException",
    "AuthorizationException",
    "RequestException",
    "PipelineException",
    "EndpointException",

]