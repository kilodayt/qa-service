from datetime import datetime

from pydantic import BaseModel, Field, constr

from .answer import AnswerOut

TextField = constr(strip_whitespace=True, min_length=1, max_length=10_000)


class QuestionCreate(BaseModel):
    text: TextField = Field(..., description="Текст вопроса")


class QuestionOut(BaseModel):
    id: int
    text: str
    created_at: datetime

    class Config:
        from_attributes = True


class QuestionWithAnswers(QuestionOut):
    answers: list[AnswerOut] = []
