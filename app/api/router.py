from fastapi import APIRouter

from .endpoints import answers, questions

api_router = APIRouter()
api_router.include_router(questions.router)
api_router.include_router(answers.router)
