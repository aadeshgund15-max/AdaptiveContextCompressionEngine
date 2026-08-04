"""
Adaptive Context Intelligence Engine (ACIE)
Retrieval Pipeline Tests
"""

import pytest


# =====================================================
# Retrieval Pipeline Exists
# =====================================================

def test_retrieval_pipeline_exists(

    retrieval_pipeline

):

    assert retrieval_pipeline is not None


# =====================================================
# Retrieval Execution
# =====================================================

def test_retrieve_memories(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    assert result is not None

    assert isinstance(

        result,

        dict

    )


# =====================================================
# Retrieved Memories
# =====================================================

def test_retrieved_memories(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    assert "retrieved_memories" in result

    memories = result["retrieved_memories"]

    assert isinstance(

        memories,

        list

    )

    if len(memories) > 0:

        memory = memories[0]

        assert "text" in memory

        assert "importance" in memory

        assert "confidence" in memory


# =====================================================
# Expanded Queries
# =====================================================

def test_expanded_queries(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    assert "expanded_queries" in result

    assert isinstance(

        result["expanded_queries"],

        list

    )


# =====================================================
# Ranked Memories
# =====================================================

def test_ranked_memories(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    assert "ranked_memories" in result

    assert isinstance(

        result["ranked_memories"],

        list

    )


# =====================================================
# Context Window
# =====================================================

def test_context_window(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    assert "context_window" in result


# =====================================================
# Token Budget
# =====================================================

def test_token_budget(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    context = result["context_window"]

    assert context["token_budget"] == 100


# =====================================================
# Query Returned
# =====================================================

def test_query(

    retrieval_pipeline,

    sample_query

):

    result = retrieval_pipeline.retrieve(

        query=sample_query,

        memories=[],

        token_budget=100

    )

    assert result["query"] == sample_query