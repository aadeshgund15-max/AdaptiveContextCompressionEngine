"""
Adaptive Context Intelligence Engine (ACIE)
Pipeline Manager Tests
"""

import pytest

from Backend.core.request_processor import RequestProcessor


# =====================================================
# Pipeline Exists
# =====================================================

def test_pipeline_manager_exists(

    pipeline_manager

):

    assert pipeline_manager is not None


# =====================================================
# Complete Pipeline
# =====================================================

def test_complete_pipeline(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain Adaptive Context Compression."

    )

    result = pipeline_manager.execute(

        request

    )

    assert result is not None

    assert isinstance(

        result,

        dict

    )


# =====================================================
# Memory Stage
# =====================================================

def test_memory_stage(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    assert "memory" in result

    assert result["memory"] is not None


# =====================================================
# Retrieval Stage
# =====================================================

def test_retrieval_stage(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    assert "retrieval" in result


# =====================================================
# Reasoning Stage
# =====================================================

def test_reasoning_stage(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    assert "reasoning" in result

    assert result["reasoning"] is not None


# =====================================================
# Prompt Stage
# =====================================================

def test_prompt_stage(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    assert "prompt" in result

    assert result["prompt"] is not None


# =====================================================
# Model Routing
# =====================================================

def test_model_stage(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    assert "model" in result

    assert result["model"] is not None

    assert "selected_model" in result["model"]


# =====================================================
# Response Stage
# =====================================================

def test_response_stage(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    assert "response" in result

    assert result["response"] is not None


# =====================================================
# Final Output Structure
# =====================================================

def test_output_structure(

    pipeline_manager

):

    processor = RequestProcessor()

    request = processor.process(

        "Explain AI"

    )

    result = pipeline_manager.execute(

        request

    )

    expected = {

        "memory",

        "retrieval",

        "reasoning",

        "prompt",

        "model",

        "response"

    }

    assert expected.issubset(

        result.keys()

    )