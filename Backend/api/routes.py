"""
Adaptive Context Intelligence Engine (ACIE)
API Routes
"""

from fastapi import APIRouter

from Backend.collector.context_collector import ContextCollector
from Backend.scorer.importance_scorer import ImportanceScorer
from Backend.scorer.confidence_calculator import ConfidenceCalculator
from Backend.decision_engine.decision_engine import DecisionEngine
from Backend.memory.memory_manager import MemoryManager
from Backend.retriever.retriever import Retriever

from Backend.models.request_models import (
    StoreRequest,
    RetrieveRequest
)

router = APIRouter()

collector = ContextCollector()
importance_scorer = ImportanceScorer()
confidence_calculator = ConfidenceCalculator()
decision_engine = DecisionEngine()
memory_manager = MemoryManager()
retriever = Retriever()


@router.get("/")
def root():

    return {
        "project": "Adaptive Context Intelligence Engine",
        "version": "1.3.0",
        "status": "Running"
    }


@router.get("/health")
def health():

    return {
        "status": "Healthy",
        "message": "ACIE API is running successfully."
    }


@router.get("/version")
def version():

    return {
        "project": "Adaptive Context Intelligence Engine",
        "version": "1.3.0"
    }


@router.get("/memories")
def get_memories():

    memories = memory_manager.get_all_memories()

    return {
        "count": len(memories),
        "memories": memories
    }


@router.post("/store")
def store_memory(request: StoreRequest):

    context = collector.collect(

        query=request.query,

        conversation=request.conversation,

        documents=request.documents

    )

    importance = importance_scorer.calculate_score(
        context
    )

    confidence = confidence_calculator.calculate_confidence(
        context
    )

    decision = decision_engine.decide(
        importance,
        confidence
    )

    if decision == "STORE":

        memory_id = memory_manager.store(

            context,

            importance,

            confidence,

            decision

        )

        return {

            "stored": True,

            "message": "Memory stored successfully.",

            "memory_id": memory_id,

            "importance": importance,

            "confidence": confidence,

            "decision": decision,

            "reason": "Importance and confidence satisfy the storage threshold."

        }

    elif decision == "COMPRESS":

        return {

            "stored": False,

            "message": "Memory marked for compression.",

            "importance": importance,

            "confidence": confidence,

            "decision": decision,

            "reason": "Memory is useful but does not satisfy the storage threshold."

        }

    elif decision == "MERGE":

        return {

            "stored": False,

            "message": "Memory should be merged with an existing memory.",

            "importance": importance,

            "confidence": confidence,

            "decision": decision,

            "reason": "Memory has moderate importance."

        }

    else:

        return {

            "stored": False,

            "message": "Memory discarded.",

            "importance": importance,

            "confidence": confidence,

            "decision": decision,

            "reason": "Memory importance is too low."

        }


@router.post("/retrieve")
def retrieve_memory(request: RetrieveRequest):

    results = retriever.retrieve(

        request.query,

        request.top_k

    )

    return {

        "query": request.query,

        "top_k": request.top_k,

        "results": results

    }