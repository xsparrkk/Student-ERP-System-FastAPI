from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student


# def create_student(db: Session, student_data):

#     existing_student = (
#         db.query(Student)
#         .filter(Student.student_id == student_data.student_id)
#         .first()
#     )

#     if existing_student:
#         raise HTTPException(
#             status_code=400,
#             detail="Student ID already exists"
#         )

#     student = Student(
#         student_id=student_data.student_id,
#         name=student_data.name,
#         age=student_data.age,
#         doj=student_data.doj,
#         student_class=student_data.student_class,
#         email=student_data.email,
#         phone_number=student_data.phone_number
#     )

#     db.add(student)
#     db.commit()
#     db.refresh(student)

#     return student


# def get_all_students(db: Session):
#     return db.query(Student).all()

from datetime import date
from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    student_id: str
    name: str
    age: int
    doj: date
    student_class: int
    email: EmailStr
    phone_number: str


class StudentUpdate(BaseModel):
    name: str
    age: int
    doj: date
    student_class: int
    email: EmailStr
    phone_number: str


class StudentResponse(BaseModel):
    id: int
    student_id: str
    name: str
    age: int
    doj: date
    student_class: int
    email: str
    phone_number: str

    class Config:
        from_attributes = True