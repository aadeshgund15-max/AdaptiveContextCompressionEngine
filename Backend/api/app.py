"""
Adaptive Context Intelligence Engine (ACIE)
FastAPI Application
"""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Backend.api.routes import router

app = FastAPI(
    title="Adaptive Context Intelligence Engine",
    version="1.0.0",
    description="AI-powered Context Compression Engine"
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(router)

@app.get("/")
def home():

    return {

        "project": "Adaptive Context Intelligence Engine",

        "version": "1.0.0",

        "status": "Running"

    }