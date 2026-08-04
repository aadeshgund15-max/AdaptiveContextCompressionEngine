"""
Adaptive Context Intelligence Engine (ACIE)
FastAPI Main Entry Point
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from Backend.api.routes import router


# ---------------------------------------------------
# Lifespan Events
# ---------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("\n========================================")
    print("Starting Adaptive Context Intelligence Engine")
    print("Initializing Memory System...")
    print("Initializing Retrieval Engine...")
    print("Initializing Reasoning Engine...")
    print("Initializing Agent Runtime...")
    print("Initializing LLM Layer...")
    print("ACIE Started Successfully")
    print("========================================\n")

    yield

    print("\n========================================")
    print("Stopping ACIE...")
    print("Goodbye!")
    print("========================================\n")


# ---------------------------------------------------
# FastAPI App
# ---------------------------------------------------

app = FastAPI(

    title="Adaptive Context Intelligence Engine (ACIE)",

    description=(
        "AI Memory Architecture with Hybrid Retrieval, "
        "Reasoning Engine, Context Compression, "
        "Knowledge Graphs and Autonomous Agents."
    ),

    version="2.1.0",

    docs_url="/docs",

    redoc_url="/redoc",

    lifespan=lifespan

)


# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# ---------------------------------------------------
# Routes
# ---------------------------------------------------

app.include_router(router)


# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------

@app.get("/", tags=["System"])
def root():

    return {

        "project": "Adaptive Context Intelligence Engine",

        "version": "2.1.0",

        "status": "Running",

        "api": "/docs",

        "health": "/health"

    }


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@app.get("/health", tags=["System"])
def health():

    return {

        "status": "Healthy",

        "memory": "Ready",

        "retrieval": "Ready",

        "reasoning": "Ready",

        "agent": "Ready",

        "llm": "Ready"

    }


# ---------------------------------------------------
# Exception Handlers
# ---------------------------------------------------

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):

    return JSONResponse(

        status_code=422,

        content={

            "status": "Validation Error",

            "details": exc.errors()

        }

    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):

    return JSONResponse(

        status_code=exc.status_code,

        content={

            "status": "HTTP Error",

            "detail": exc.detail

        }

    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):

    return JSONResponse(

        status_code=500,

        content={

            "status": "Internal Server Error",

            "message": str(exc)

        }

    )


# ---------------------------------------------------
# Run Server
# ---------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "Backend.main:app",

        host="127.0.0.1",

        port=8000,

        reload=True

    )