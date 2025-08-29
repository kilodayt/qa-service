from fastapi import FastAPI

from app.api.router import api_router
from app.core.logging import setup_logging

setup_logging()
app = FastAPI(title="QA Service")
app.include_router(api_router)


@app.get("/health")
def health():
    return {"status": "ok"}
