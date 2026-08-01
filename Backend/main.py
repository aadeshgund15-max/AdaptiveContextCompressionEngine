"""
Adaptive Context Intelligence Engine (ACIE)
FastAPI Main Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend.api.routes import router

app = FastAPI(
    title="Adaptive Context Intelligence Engine (ACIE)",
    description="AI Memory System with Hybrid Retrieval and Context Compression",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "project": "Adaptive Context Intelligence Engine",
        "version": "2.0.0",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "message": "ACIE API is running successfully."
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "Backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )