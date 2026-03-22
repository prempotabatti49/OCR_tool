from fastapi import APIRouter
from app.api.ingestion_api import router as ingestion_router
from app.api.retrieval_api import router as retrieval_router

api_router = APIRouter()

api_router.include_router(ingestion_router)
api_router.include_router(retrieval_router)

