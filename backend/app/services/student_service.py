from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student
from app.models.fee import Fee


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
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.student import Student


from app.models.fee import Fee

def create_student(db: Session, student_data):

    existing_student = (
        db.query(Student)
        .filter(Student.student_id == student_data.student_id)
        .first()
    )

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    student = Student(
        student_id=student_data.student_id,
        name=student_data.name,
        age=student_data.age,
        doj=student_data.doj,
        student_class=student_data.student_class,
        email=student_data.email,
        phone_number=student_data.phone_number
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    # -------------------------------
    # Automatically create Fee Record
    # -------------------------------

    fee = Fee(
        student_id=student.student_id,

        transport_fee=0,
        tuition_fee=0,
        extra_fee=0,

        total_fee=0,
        paid_amount=0,
        due_amount=0,

        payment_status="Pending"
    )

    db.add(fee)
    db.commit()

    return student


def get_all_students(db: Session):
    return db.query(Student).all()


def get_student_by_id(
    db: Session,
    student_id: str
):

    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


def update_student(
    db: Session,
    student_id: str,
    updated_data
):

    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated_data.name
    student.age = updated_data.age
    student.doj = updated_data.doj
    student.student_class = updated_data.student_class
    student.email = updated_data.email
    student.phone_number = updated_data.phone_number

    db.commit()
    db.refresh(student)

    return student


def delete_student(
    db: Session,
    student_id: str
):

    student = (
        db.query(Student)
        .filter(Student.student_id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }
    
