"""
Adaptive Context Intelligence Engine (ACIE)
Runtime Configuration
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class RuntimeConfig:

    # --------------------------------------------------
    # LLM Configuration
    # --------------------------------------------------

    default_model: str = "gemini"

    temperature: float = 0.3

    max_tokens: int = 4096

    stream_response: bool = True

    # --------------------------------------------------
    # Memory
    # --------------------------------------------------

    enable_memory: bool = True

    memory_limit: int = 1000

    importance_threshold: int = 60

    # --------------------------------------------------
    # Retrieval
    # --------------------------------------------------

    enable_retrieval: bool = True

    retrieval_top_k: int = 5

    token_budget: int = 100

    # --------------------------------------------------
    # Reasoning
    # --------------------------------------------------

    enable_reasoning: bool = True

    enable_reflection: bool = True

    # --------------------------------------------------
    # Knowledge Graph
    # --------------------------------------------------

    enable_knowledge_graph: bool = True

    graph_depth: int = 2

    # --------------------------------------------------
    # Compression
    # --------------------------------------------------

    enable_compression: bool = True

    compression_ratio: float = 0.70

    # --------------------------------------------------
    # Agent
    # --------------------------------------------------

    enable_tools: bool = True

    enable_planner: bool = True

    enable_multi_agent: bool = False

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    enable_logging: bool = True

    log_level: str = "INFO"

    # --------------------------------------------------
    # Providers
    # --------------------------------------------------

    available_models: List[str] = field(default_factory=lambda: [

        "gemini",

        "gpt",

        "claude",

        "groq",

        "ollama"

    ])

    # --------------------------------------------------
    # Utility
    # --------------------------------------------------

    def to_dict(self):

        return self.__dict__


if __name__ == "__main__":

    config = RuntimeConfig()

    print(config)

    print()

    print(config.to_dict())