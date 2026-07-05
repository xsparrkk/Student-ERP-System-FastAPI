from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.marks import Marks

# Add Marks
def add_marks(
    db: Session,
    marks_data
):

    marks = Marks(
        student_id=marks_data.student_id,
        student_class=marks_data.student_class,
        subject=marks_data.subject,
        marks=marks_data.marks,
        year=marks_data.year
    )

    db.add(marks)

    db.commit()

    db.refresh(marks)

    return marks

# Fetch Marks
def get_marks_by_student(
    db: Session,
    student_id: str
):

    return (
        db.query(Marks)
        .filter(
            Marks.student_id == student_id
        )
        .all()
    )
    
# Update Marks

def update_marks(
    db: Session,
    marks_id: int,
    marks_data
):

    marks_record = (
        db.query(Marks)
        .filter(Marks.id == marks_id)
        .first()
    )

    if not marks_record:
        raise HTTPException(
            status_code=404,
            detail="Marks record not found"
        )

    marks_record.student_id = marks_data.student_id
    marks_record.student_class = marks_data.student_class
    marks_record.subject = marks_data.subject
    marks_record.marks = marks_data.marks
    marks_record.year = marks_data.year

    db.commit()

    db.refresh(marks_record)

    return marks_record

# Delete Marks

def delete_marks(
    db: Session,
    marks_id: int
):

    marks_record = (
        db.query(Marks)
        .filter(Marks.id == marks_id)
        .first()
    )

    if not marks_record:
        raise HTTPException(
            status_code=404,
            detail="Marks record not found"
        )

    db.delete(marks_record)

    db.commit()

    return {
        "message": "Marks deleted successfully"
    }