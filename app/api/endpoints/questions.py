from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.db import models
from app.schemas.question import QuestionCreate, QuestionOut, QuestionWithAnswers

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=list[QuestionOut])
def list_questions(db: Session = Depends(get_db)):
    return db.query(models.Question).order_by(models.Question.id).all()


@router.post("/", response_model=QuestionOut, status_code=status.HTTP_201_CREATED)
def create_question(payload: QuestionCreate, db: Session = Depends(get_db)):
    q = models.Question(text=payload.text)
    db.add(q)
    db.commit()
    db.refresh(q)
    return q


@router.get("/{qid}", response_model=QuestionWithAnswers)
def get_question(qid: int, db: Session = Depends(get_db)):
    q = db.query(models.Question).filter(models.Question.id == qid).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q


@router.delete("/{qid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(qid: int, db: Session = Depends(get_db)):
    q = db.query(models.Question).filter(models.Question.id == qid).first()
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(q)  # каскадно удалит answers
    db.commit()
    return None
