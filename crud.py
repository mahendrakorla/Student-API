from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Students

def create_student(data, db: Session):
    new_student = Students(
        s_id=data.s_id,
        s_name=data.s_name,
        s_marks=data.s_marks,
        s_result=data.s_result
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

def get_all_students(db: Session):
    return db.query(Students).all()

def get_student(student_id: int, db: Session):
    stu = db.query(Students).filter(Students.s_id == student_id).first()

    if not stu:
        raise HTTPException(status_code=404, detail="Student not found")

    return stu

def update_student(student_id: int, updated_data, db: Session):

    stu = db.query(Students).filter(Students.s_id == student_id).first()

    if not stu:
        raise HTTPException(status_code=404, detail="Student not found")

    stu.s_name = updated_data.s_name
    stu.s_marks = updated_data.s_marks
    stu.s_result = updated_data.s_result

    db.commit()
    db.refresh(stu)

    return stu

def delete_student(student_id: int, db: Session):

    stu = db.query(Students).filter(Students.s_id == student_id).first()

    if not stu:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(stu)
    db.commit()

    return {"message": "Student deleted successfully"}