from datetime import datetime

from pydantic import BaseModel, Field, constr

TextField = constr(strip_whitespace=True, min_length=1, max_length=10_000)
UserIdField = constr(strip_whitespace=True, min_length=1, max_length=64)


class AnswerCreate(BaseModel):
    user_id: UserIdField = Field(..., description="Идентификатор пользователя")
    text: TextField = Field(..., description="Текст ответа")


class AnswerOut(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

    class Config:
        from_attributes = True
