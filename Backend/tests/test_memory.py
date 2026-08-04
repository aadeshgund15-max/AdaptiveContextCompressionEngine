"""
Adaptive Context Intelligence Engine (ACIE)
Memory Tests
"""

import pytest


# =====================================================
# Memory Pipeline
# =====================================================

def test_memory_pipeline_exists(

    memory_pipeline

):

    assert memory_pipeline is not None


# =====================================================
# Memory Processing
# =====================================================

def test_memory_process(

    memory_pipeline,

    sample_query,

    sample_conversation,

    sample_documents

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=sample_conversation,

        documents=sample_documents

    )

    assert result is not None

    assert isinstance(

        result,

        dict

    )


# =====================================================
# Memory Decision
# =====================================================

def test_memory_decision(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "decision" in result

    assert result["decision"] in [

        "STORE",

        "FORGET"

    ]


# =====================================================
# Importance Score
# =====================================================

def test_importance_score(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "importance" in result

    assert isinstance(

        result["importance"],

        int

    )


# =====================================================
# Confidence Score
# =====================================================

def test_confidence_score(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "confidence" in result

    assert isinstance(

        result["confidence"],

        float

    )


# =====================================================
# Compression
# =====================================================

def test_compression(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "compression" in result


# =====================================================
# Reflection
# =====================================================

def test_reflection(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "reflection" in result


# =====================================================
# Knowledge Graph
# =====================================================

def test_knowledge_graph(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "knowledge_graph" in result


# =====================================================
# Consolidated Memories
# =====================================================

def test_consolidated_memories(

    memory_pipeline,

    sample_query

):

    result = memory_pipeline.process(

        query=sample_query,

        conversation=[],

        documents=[]

    )

    assert "consolidated_memories" in result