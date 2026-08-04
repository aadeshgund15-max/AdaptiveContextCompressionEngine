"""
Adaptive Context Intelligence Engine (ACIE)
Reasoning Engine Tests
"""

import pytest


# =====================================================
# Reasoning Engine Exists
# =====================================================

def test_reasoning_engine_exists(

    reasoning_engine

):

    assert reasoning_engine is not None


# =====================================================
# Reasoning Process
# =====================================================

def test_reasoning_process(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert result is not None

    assert isinstance(

        result,

        dict

    )


# =====================================================
# Strategy
# =====================================================

def test_strategy(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert "strategy" in result


# =====================================================
# Plan
# =====================================================

def test_plan(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert "plan" in result

    assert isinstance(

        result["plan"],

        list

    )


# =====================================================
# Chain of Thought
# =====================================================

def test_reasoning(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert "reasoning" in result


# =====================================================
# Reflection
# =====================================================

def test_reflection(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert "reflection" in result


# =====================================================
# Verification
# =====================================================

def test_verification(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert "verification" in result


# =====================================================
# Self Critique
# =====================================================

def test_critique(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    assert "critique" in result


# =====================================================
# Complete Output Structure
# =====================================================

def test_output_structure(

    reasoning_engine,

    sample_query

):

    result = reasoning_engine.process(

        query=sample_query,

        retrieved_memories=[],

        draft_response=""

    )

    expected_keys = {

        "strategy",

        "plan",

        "reasoning",

        "reflection",

        "verification",

        "critique"

    }

    assert expected_keys.issubset(

        result.keys()

    )