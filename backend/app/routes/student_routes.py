from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.student_service import (
    create_student,
    get_all_students
)
from app.database.dependencies import get_db
from app.auth.roles import admin_required
from app.schemas.student_schema import (
    StudentCreate,
    StudentResponse
)
from app.models.student import Student
from app.services.student_service import create_student
from app.auth.dependencies import get_current_user



router = APIRouter()


@router.post(
    "/register",
    response_model=StudentResponse
)
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    user= Depends(get_current_user)
):
    return create_student(db, student)

@router.get("/", response_model=list[StudentResponse])
def fetch_students(
    db: Session = Depends(get_db),user=Depends(get_current_user)):
    return get_all_students(db)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.student_schema import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)

from app.services.student_service import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)

router = APIRouter()


# CREATE
@router.post(
    "/register",
    response_model=StudentResponse
)
def register_student(
    student: StudentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_student(db, student)

#student.me
@router.get("/me")
def my_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    student = (
        db.query(Student)
        .filter(
            Student.student_id == current_user["student_id"]
        )
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student



# READ ALL
@router.get(
    "/",
    response_model=list[StudentResponse]
)
def fetch_students(
    db: Session = Depends(get_db),
    user= Depends(get_current_user)
):
    return get_all_students(db)


# READ ONE

# @router.get(
#     "/{student_id}",
#     response_model=StudentResponse
# )
# def fetch_student(
#     student_id: str,
#     db: Session = Depends(get_db),
#     user= Depends(get_current_user)
# ):
#     return get_student_by_id(
#         db,
#         student_id
#     )


@router.get("/{student_id}")
def fetch_student(
    student_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    # Admin can access everyone
    if current_user["role"] == "admin":
        return get_student_by_id(db, student_id)

    # Student can access only themselves
    if current_user["student_id"] != student_id:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own profile."
        )

    return get_student_by_id(db, student_id)


# UPDATE
@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def modify_student(
    student_id: str,
    student: StudentUpdate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return update_student(
        db,
        student_id,
        student
    )


# DELETE
@router.delete(
    "/{student_id}"
)
def remove_student(
    student_id: str,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return delete_student(
        db,
        student_id
    )
    
