"""
Adaptive Context Intelligence Engine (ACIE)
Core Engine
"""

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline

from Backend.reasoning.reasoning_engine import ReasoningEngine

import inspect

from Backend.llm.prompt_builder import PromptBuilder
from Backend.llm.context_optimizer import ContextOptimizer
from Backend.llm.token_budget_manager import TokenBudgetManager
from Backend.llm.llm_router import LLMRouter
from Backend.llm.llm_client import LLMClient
from Backend.llm.response_parser import ResponseParser
from Backend.llm.streaming_generator import StreamingGenerator


class ACIEEngine:

    def __init__(self):

        self.memory_pipeline = MemoryPipeline()

        self.retrieval_pipeline = RetrievalPipeline()

        self.reasoning_engine = ReasoningEngine()

        self.prompt_builder = PromptBuilder()

        self.context_optimizer = ContextOptimizer()

        self.token_budget_manager = TokenBudgetManager()

        self.llm_router = LLMRouter()

        self.llm_client = LLMClient()

        self.response_parser = ResponseParser()

        self.streaming_generator = StreamingGenerator()

    # ----------------------------------------------------
    # Execute Complete AI Pipeline
    # ----------------------------------------------------

    def execute(

        self,

        query,

        conversation=None,

        documents=None

    ):

        if conversation is None:
            conversation = []

        if documents is None:
            documents = []

        print("\n========== ACIE ENGINE ==========\n")

        # ------------------------------------
        # Memory
        # ------------------------------------

        memory_result = self.memory_pipeline.process(

            query=query,

            conversation=conversation,

            documents=documents

        )

        # ------------------------------------
        # Retrieval
        # ------------------------------------

        retrieval_result = self.retrieval_pipeline.retrieve(

            query=query,

            memories=memory_result["consolidated_memories"],

            token_budget=100

        )

        # ------------------------------------
        # Reasoning
        # ------------------------------------

        # Call the reasoning engine using available method names for compatibility
        if hasattr(self.reasoning_engine, "reason"):
            reasoning_callable = getattr(self.reasoning_engine, "reason")
        elif hasattr(self.reasoning_engine, "run"):
            reasoning_callable = getattr(self.reasoning_engine, "run")
        elif hasattr(self.reasoning_engine, "execute"):
            reasoning_callable = getattr(self.reasoning_engine, "execute")
        else:
            raise AttributeError("ReasoningEngine has no callable 'reason', 'run', or 'execute'")

        reasoning_result = reasoning_callable(
            query=query,
            retrieved_context=retrieval_result
        )

        # ------------------------------------
        # Context Optimization
        # ------------------------------------

        optimized_context = self.context_optimizer.optimize(

            retrieval_result

        )

        # ------------------------------------
        # Prompt
        # ------------------------------------

        prompt = self.prompt_builder.build(

            query=query,

            context_window=optimized_context,

            reasoning_plan=reasoning_result

        )

        # ------------------------------------
        # Token Budget
        # ------------------------------------

        # Token budget manager may expose different method names across implementations.
        if hasattr(self.token_budget_manager, "fit"):
            tbm_callable = getattr(self.token_budget_manager, "fit")
        elif hasattr(self.token_budget_manager, "apply"):
            tbm_callable = getattr(self.token_budget_manager, "apply")
        elif hasattr(self.token_budget_manager, "adjust"):
            tbm_callable = getattr(self.token_budget_manager, "adjust")
        elif hasattr(self.token_budget_manager, "manage"):
            tbm_callable = getattr(self.token_budget_manager, "manage")
        else:
            # Fallback: no-op
            tbm_callable = lambda p: p

        prompt = tbm_callable(
            prompt
        )

        # ------------------------------------
        # Model Selection
        # ------------------------------------

        model = self.llm_router.route(

            request=prompt

        )

        # ------------------------------------
        # LLM Generation
        # ------------------------------------

        raw_response = self.llm_client.generate(

            prompt

        )

        # ------------------------------------
        # Parse
        # ------------------------------------

        final_response = self.response_parser.parse(

            raw_response

        )

        return {

            "query": query,

            "model": model,

            "memory": memory_result,

            "retrieval": retrieval_result,

            "reasoning": reasoning_result,

            "response": final_response

        }


if __name__ == "__main__":

    engine = ACIEEngine()

    result = engine.execute(

        query="Explain Adaptive Context Compression."

    )

    print("\n========== RESULT ==========\n")

    print(result)