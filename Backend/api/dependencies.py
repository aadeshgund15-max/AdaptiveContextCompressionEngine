"""
Adaptive Context Intelligence Engine (ACIE)
API Dependencies
"""

from Backend.core.pipeline_manager import PipelineManager

from Backend.pipeline.memory_pipeline import MemoryPipeline

from Backend.collector.context_collector import ContextCollector

from Backend.scorer.importance_scorer import ImportanceScorer

from Backend.scorer.confidence_calculator import ConfidenceCalculator

from Backend.decision_engine.decision_engine import DecisionEngine

from Backend.memory.memory_manager import MemoryManager

from Backend.retriever.retriever import Retriever

from Backend.hybrid.hybrid_retriever import HybridRetriever

from Backend.compressor.context_compressor import ContextCompressor

from Backend.context_builder.context_window_builder import ContextWindowBuilder

from Backend.reflection.reflection_engine import ReflectionEngine

from Backend.agent.agent_runtime import AgentRuntime


# =====================================================
# Singleton Instances
# =====================================================

pipeline_manager = PipelineManager()

memory_pipeline = MemoryPipeline()

collector = ContextCollector()

importance_scorer = ImportanceScorer()

confidence_calculator = ConfidenceCalculator()

decision_engine = DecisionEngine()

memory_manager = MemoryManager()

retriever = Retriever()

hybrid_retriever = HybridRetriever()

compressor = ContextCompressor()

context_builder = ContextWindowBuilder()

reflection_engine = ReflectionEngine()

agent_runtime = AgentRuntime()


# =====================================================
# Dependency Providers
# =====================================================

def get_pipeline_manager():

    return pipeline_manager


def get_memory_pipeline():

    return memory_pipeline


def get_context_collector():

    return collector


def get_importance_scorer():

    return importance_scorer


def get_confidence_calculator():

    return confidence_calculator


def get_decision_engine():

    return decision_engine


def get_memory_manager():

    return memory_manager


def get_retriever():

    return retriever


def get_hybrid_retriever():

    return hybrid_retriever


def get_context_compressor():

    return compressor


def get_context_builder():

    return context_builder


def get_reflection_engine():

    return reflection_engine


def get_agent_runtime():

    return agent_runtime