"""
Adaptive Context Intelligence Engine (ACIE)
API Tests
"""

import pytest


# ==========================================
# Root Endpoint
# ==========================================

def test_root(client):

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["project"] == "Adaptive Context Intelligence Engine"

    assert data["status"] == "Running"


# ==========================================
# Health Endpoint
# ==========================================

def test_health(client):

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "Healthy"


# ==========================================
# Version Endpoint
# ==========================================

def test_version(client):

    response = client.get("/version")

    assert response.status_code == 200

    data = response.json()

    assert "version" in data


# ==========================================
# Ping Endpoint
# ==========================================

def test_ping(client):

    response = client.get("/ping")

    assert response.status_code == 200

    assert response.json()["message"] == "Pong"


# ==========================================
# Agent Status
# ==========================================

def test_agent_status(client):

    response = client.get("/agent-status")

    assert response.status_code == 200

    data = response.json()

    assert data["agent"] == "ACIE"

    assert data["api"] == "ONLINE"


# ==========================================
# Store Memory
# ==========================================

def test_store_memory(client):

    payload = {

        "query": "What is Artificial Intelligence?",

        "conversation": [],

        "documents": []

    }

    response = client.post(

        "/store",

        json=payload

    )

    assert response.status_code == 200

    data = response.json()

    assert "decision" in data


# ==========================================
# Retrieve Memory
# ==========================================

def test_retrieve_memory(client):

    payload = {

        "query": "Artificial Intelligence",

        "top_k": 3

    }

    response = client.post(

        "/retrieve",

        json=payload

    )

    assert response.status_code == 200

    data = response.json()

    assert "results" in data


# ==========================================
# Pipeline
# ==========================================

def test_pipeline(client):

    payload = {

        "query": "Explain Adaptive Context Compression.",

        "conversation": [],

        "documents": []

    }

    response = client.post(

        "/pipeline",

        json=payload

    )

    assert response.status_code == 200


# ==========================================
# Chat
# ==========================================

def test_chat(client):

    payload = {

        "query": "What is AI?"

    }

    response = client.post(

        "/chat",

        json=payload

    )

    assert response.status_code == 200

    data = response.json()

    assert "response" in data

    assert data["status"] == "SUCCESS"