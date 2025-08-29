from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.db import models
from app.schemas.answer import AnswerCreate, AnswerOut

router = APIRouter(tags=["answers"])


@router.post(
    "/questions/{qid}/answers/",
    response_model=AnswerOut,
    status_code=status.HTTP_201_CREATED,
)
def create_answer(qid: int, payload: AnswerCreate, db: Session = Depends(get_db)):
    q_exists = db.query(models.Question.id).filter(models.Question.id == qid).first()
    if not q_exists:
        raise HTTPException(status_code=400, detail="Cannot add answer to non-existent question")

    ans = models.Answer(question_id=qid, user_id=payload.user_id, text=payload.text)
    db.add(ans)
    db.commit()
    db.refresh(ans)
    return ans


@router.get("/answers/{aid}", response_model=AnswerOut)
def get_answer(aid: int, db: Session = Depends(get_db)):
    ans = db.query(models.Answer).filter(models.Answer.id == aid).first()
    if not ans:
        raise HTTPException(status_code=404, detail="Answer not found")
    return ans


@router.delete("/answers/{aid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(aid: int, db: Session = Depends(get_db)):
    ans = db.query(models.Answer).filter(models.Answer.id == aid).first()
    if not ans:
        raise HTTPException(status_code=404, detail="Answer not found")
    db.delete(ans)
    db.commit()
    return None
