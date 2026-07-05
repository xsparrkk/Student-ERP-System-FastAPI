from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.marks_schema import (
    MarksCreate,
    MarksResponse
)

from app.services.marks_service import (
    add_marks,
    get_marks_by_student
)

from app.services.marks_service import (
    add_marks,
    get_marks_by_student,
    update_marks,
    delete_marks
)


from app.auth.roles import admin_required
from app.auth.dependencies import get_current_user

router = APIRouter()

@router.post(
    "/",
    response_model=MarksResponse
)
def create_marks(
    marks: MarksCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    return add_marks(
        db,
        marks
    )
    
@router.get(
    "/student/{student_id}",
    response_model=list[MarksResponse]
)
def fetch_marks(
    student_id: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    return get_marks_by_student(
        db,
        student_id
    )
    
# PUT API
@router.put(
    "/{marks_id}",
    response_model=MarksResponse
)
def update_marks_record(
    marks_id: int,
    marks: MarksCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    return update_marks(
        db,
        marks_id,
        marks
    )
    
# delete API
@router.delete(
    "/{marks_id}"
)
def delete_marks_record(
    marks_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):

    return delete_marks(
        db,
        marks_id
    )