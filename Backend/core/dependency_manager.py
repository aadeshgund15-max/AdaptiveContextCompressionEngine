"""
Adaptive Context Intelligence Engine (ACIE)
Dependency Manager
"""

from Backend.core.runtime_config import RuntimeConfig

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline

from Backend.reasoning.reasoning_engine import ReasoningEngine

from Backend.llm.prompt_builder import PromptBuilder
from Backend.llm.context_optimizer import ContextOptimizer
from Backend.llm.token_budget_manager import TokenBudgetManager
from Backend.llm.llm_router import LLMRouter
from Backend.llm.llm_client import LLMClient
from Backend.llm.response_parser import ResponseParser
from Backend.llm.streaming_generator import StreamingGenerator


class DependencyManager:

    def __init__(self):

        self.config = RuntimeConfig()

        self._instances = {}

    # -------------------------------------------------
    # Runtime Config
    # -------------------------------------------------

    def config_manager(self):

        return self.config

    # -------------------------------------------------
    # Memory Pipeline
    # -------------------------------------------------

    def memory_pipeline(self):

        if "memory_pipeline" not in self._instances:

            self._instances["memory_pipeline"] = MemoryPipeline()

        return self._instances["memory_pipeline"]

    # -------------------------------------------------
    # Retrieval Pipeline
    # -------------------------------------------------

    def retrieval_pipeline(self):

        if "retrieval_pipeline" not in self._instances:

            self._instances["retrieval_pipeline"] = RetrievalPipeline()

        return self._instances["retrieval_pipeline"]

    # -------------------------------------------------
    # Reasoning
    # -------------------------------------------------

    def reasoning_engine(self):

        if "reasoning_engine" not in self._instances:

            self._instances["reasoning_engine"] = ReasoningEngine()

        return self._instances["reasoning_engine"]

    # -------------------------------------------------
    # Prompt Builder
    # -------------------------------------------------

    def prompt_builder(self):

        if "prompt_builder" not in self._instances:

            self._instances["prompt_builder"] = PromptBuilder()

        return self._instances["prompt_builder"]

    # -------------------------------------------------
    # Context Optimizer
    # -------------------------------------------------

    def context_optimizer(self):

        if "context_optimizer" not in self._instances:

            self._instances["context_optimizer"] = ContextOptimizer()

        return self._instances["context_optimizer"]

    # -------------------------------------------------
    # Token Budget
    # -------------------------------------------------

    def token_budget_manager(self):

        if "token_budget_manager" not in self._instances:

            self._instances["token_budget_manager"] = TokenBudgetManager()

        return self._instances["token_budget_manager"]

    # -------------------------------------------------
    # Router
    # -------------------------------------------------

    def llm_router(self):

        if "llm_router" not in self._instances:

            self._instances["llm_router"] = LLMRouter()

        return self._instances["llm_router"]

    # -------------------------------------------------
    # Client
    # -------------------------------------------------

    def llm_client(self):

        if "llm_client" not in self._instances:

            self._instances["llm_client"] = LLMClient()

        return self._instances["llm_client"]

    # -------------------------------------------------
    # Parser
    # -------------------------------------------------

    def response_parser(self):

        if "response_parser" not in self._instances:

            self._instances["response_parser"] = ResponseParser()

        return self._instances["response_parser"]

    # -------------------------------------------------
    # Streaming
    # -------------------------------------------------

    def streaming_generator(self):

        if "streaming_generator" not in self._instances:

            self._instances["streaming_generator"] = StreamingGenerator()

        return self._instances["streaming_generator"]

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    def summary(self):

        return {

            "loaded_dependencies": list(

                self._instances.keys()

            ),

            "count": len(

                self._instances

            )

        }


if __name__ == "__main__":

    manager = DependencyManager()

    manager.memory_pipeline()

    manager.retrieval_pipeline()

    manager.reasoning_engine()

    manager.prompt_builder()

    manager.llm_client()

    print(

        manager.summary()

    )