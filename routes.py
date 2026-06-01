from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import Insertt, Supdate
from crud import (
    create_student,
    get_all_students,
    get_student,
    update_student,
    delete_student
)

router = APIRouter()

@router.post("/student-create")
def create(data: Insertt, db: Session = Depends(get_db)):
    return create_student(data, db)

@router.get("/student-retrival")
def get_all(db: Session = Depends(get_db)):
    return get_all_students(db)

@router.get("/student/{student_id}")
def get_one(student_id: int, db: Session = Depends(get_db)):
    return get_student(student_id, db)

@router.put("/student/{student_id}")
def update(student_id: int, updated_data: Supdate, db: Session = Depends(get_db)):
    return update_student(student_id, updated_data, db)

@router.delete("/student-remove/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    return delete_student(student_id, db)