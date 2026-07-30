"""
Adaptive Context Intelligence Engine (ACIE)
FastAPI Application
"""

from fastapi import FastAPI
from Backend.api.routes import router

app = FastAPI(
    title="Adaptive Context Intelligence Engine",
    version="1.0.0",
    description="AI-powered Context Compression Engine"
)

app.include_router(router)

@app.get("/")
def home():

    return {

        "project": "Adaptive Context Intelligence Engine",

        "version": "1.0.0",

        "status": "Running"

    }