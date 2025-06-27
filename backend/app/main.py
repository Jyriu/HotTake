"""HotTake FastAPI application entrypoint."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="HotTake API", version="0.1.0")

# Allow CORS for local dev and preview deployments. Can be restricted later via env.
origins = os.getenv("CORS_ALLOW_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz", tags=["Health"], summary="Health check endpoint")
async def healthcheck() -> dict[str, str]:
    """Basic liveness probe used by Kubernetes / Docker compose."""
    return {"status": "ok"}
