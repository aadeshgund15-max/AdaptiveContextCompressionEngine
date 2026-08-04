"""
Adaptive Context Intelligence Engine (ACIE)
Pipeline Manager
"""

import inspect
from typing import Any

from Backend.pipeline.memory_pipeline import MemoryPipeline
from Backend.pipeline.retrieval_pipeline import RetrievalPipeline

from Backend.reasoning.reasoning_engine import ReasoningEngine

from Backend.llm.prompt_builder import PromptBuilder
from Backend.llm.context_optimizer import ContextOptimizer
from Backend.llm.token_budget_manager import TokenBudgetManager
from Backend.llm.llm_router import LLMRouter
from Backend.llm.llm_client import LLMClient
from Backend.llm.failover_manager import FailoverManager
from Backend.llm.response_parser import ResponseParser


class PipelineManager:

    def __init__(self):

        self.memory_pipeline = MemoryPipeline()

        self.retrieval_pipeline = RetrievalPipeline()

        self.reasoning_engine = ReasoningEngine()

        self.context_optimizer = ContextOptimizer()

        self.prompt_builder = PromptBuilder()

        self.token_budget_manager = TokenBudgetManager()

        self.llm_router = LLMRouter()

        # Keep this if you still use it elsewhere
        self.llm_client = LLMClient()

        # NEW
        self.failover_manager = FailoverManager()

        self.response_parser = ResponseParser()

    # -------------------------------------------------
    # Execute Complete Pipeline
    # -------------------------------------------------

    def execute(

        self,

        request,

        conversation=None,

        documents=None

    ):

        if conversation is None:
            conversation = []

        if documents is None:
            documents = []

        result: dict[str, Any] = {

            "memory": None,

            "retrieval": None,

            "reasoning": None,

            "prompt": None,

            "model": None,

            "response": None

        }

        # -----------------------------------------
        # Memory Pipeline
        # -----------------------------------------

        memory_result = self.memory_pipeline.process(

            query=request["query"],

            conversation=conversation,

            documents=documents

        )

        result["memory"] = memory_result

        # -----------------------------------------
        # Retrieval
        # -----------------------------------------

        retrieval_result = None

        if request["requires_retrieval"]:

            retrieval_result = self.retrieval_pipeline.retrieve(

                query=request["query"],

                memories=memory_result["consolidated_memories"],

                token_budget=100

            )

            result["retrieval"] = retrieval_result

        # -----------------------------------------
        # Reasoning
        # -----------------------------------------

        reasoning_method = (
            getattr(self.reasoning_engine, "reason", None)
            or getattr(self.reasoning_engine, "process", None)
            or getattr(self.reasoning_engine, "execute", None)
            or getattr(self.reasoning_engine, "run", None)
            or getattr(self.reasoning_engine, "analyze", None)
        )

        if reasoning_method is None:
            raise AttributeError(
                "ReasoningEngine does not implement a compatible reasoning method."
            )

        # -----------------------------------------
        # Prepare reasoning inputs
        # -----------------------------------------

        retrieved_memories = []

        if retrieval_result is not None and isinstance(retrieval_result, dict):
            retrieved_memories = (
                retrieval_result.get("selected_memories")
                or retrieval_result.get("retrieved_memories")
                or retrieval_result.get("memories")
                or []
            )

        draft_response = ""

        reasoning_result = reasoning_method(
            query=request["query"],
            retrieved_memories=retrieved_memories,
            draft_response=draft_response
        )

        result["reasoning"] = reasoning_result

        # -----------------------------------------
        # Optimize Context
        # -----------------------------------------

        optimized_context = self.context_optimizer.optimize(
            retrieval_result
        )

        # -------------------------------------------------
        # Normalize optimizer output
        # -------------------------------------------------

        if isinstance(optimized_context, list):
            optimized_context = {
                "selected_memories": optimized_context
            }
        elif optimized_context is None:
            optimized_context = {
                "selected_memories": []
            }

        # -----------------------------------------
        # Build Prompt
        # -----------------------------------------

        prompt = self.prompt_builder.build(
            query=request["query"],
            context_window=optimized_context,
            reasoning_plan=reasoning_result
        )

        result["prompt"] = prompt

        # -----------------------------------------
        # Token Budget
        # -----------------------------------------

        token_budget_method = (
            getattr(self.token_budget_manager, "fit", None)
            or getattr(self.token_budget_manager, "optimize", None)
            or getattr(self.token_budget_manager, "apply", None)
            or getattr(self.token_budget_manager, "truncate", None)
        )

        if token_budget_method is None:
            raise AttributeError(
                "TokenBudgetManager does not implement a compatible token budget method."
            )

        prompt = token_budget_method(
            prompt
        )

        # -----------------------------------------
        # Model Selection
        # -----------------------------------------

        llm_route_method = getattr(self.llm_router, "route", None)

        if llm_route_method is None:
            raise AttributeError(
                "LLMRouter does not implement a route method."
            )

        route_params = list(inspect.signature(llm_route_method).parameters.keys())

        if len(route_params) == 1:
            if route_params[0] == "request":
                model = llm_route_method(request)
            else:
                model = llm_route_method(request["query"])
        else:
            model = llm_route_method(
                query=request["query"],
                task_type=request.get("task_type")
            )

        result["model"] = model

        print("\n========== MODEL DEBUG ==========")
        print(model)
        print("=" * 60)

        # -----------------------------------------
        # Generate (with Automatic Failover)
        # -----------------------------------------

        raw_response = self.failover_manager.generate(

            prompt=prompt,

            preferred_provider=model["selected_model"]

        )

        # -----------------------------------------
        # Parse
        # -----------------------------------------

        final_response = self.response_parser.parse(

            raw_response

        )

        result["response"] = final_response

        return result


if __name__ == "__main__":

    from Backend.core.request_processor import RequestProcessor

    processor = RequestProcessor()

    request = processor.process(

        "Explain Adaptive Context Compression."

    )

    manager = PipelineManager()

    result = manager.execute(

        request

    )

    print("\n========== RESULT ==========\n")

    print(result)