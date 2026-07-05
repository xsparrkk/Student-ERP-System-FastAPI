from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.fee import Fee


def create_fee(db: Session, fee_data):

    existing = (
        db.query(Fee)
        .filter(Fee.student_id == fee_data.student_id)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Fee record already exists"
        )

    fee = Fee(
        student_id=fee_data.student_id,
        
        transport_fee=fee_data.transport_fee,
        tuition_fee=fee_data.tuition_fee,
        extra_fee=fee_data.extra_fee,
        total_fee=fee_data.total_fee,
        paid_amount=fee_data.paid_amount,
        due_amount=fee_data.due_amount,
        payment_status=fee_data.payment_status
    )

    db.add(fee)
    db.commit()
    db.refresh(fee)

    return fee


def get_all_fees(db: Session):

    return db.query(Fee).all()


def get_fee_by_student(db: Session, student_id: str):

    fee = (
        db.query(Fee)
        .filter(Fee.student_id == student_id)
        .first()
    )

    if not fee:
        raise HTTPException(
            status_code=404,
            detail="Fee record not found"
        )

    return fee


def update_fee(
    db: Session,
    fee_id: int,
    fee_data
):

    fee = (
        db.query(Fee)
        .filter(Fee.id == fee_id)
        .first()
    )

    if not fee:
        raise HTTPException(
            status_code=404,
            detail="Fee record not found"
        )

    fee.student_id = fee_data.student_id
    fee.transport_fee = fee_data.transport_fee
    fee.tuition_fee = fee_data.tuition_fee
    fee.extra_fee = fee_data.extra_fee
    fee.total_fee = fee_data.total_fee
    fee.paid_amount = fee_data.paid_amount
    fee.due_amount = fee_data.due_amount
    fee.payment_status = fee_data.payment_status

    db.commit()
    db.refresh(fee)

    return fee


def delete_fee(
    db: Session,
    fee_id: int
):

    fee = (
        db.query(Fee)
        .filter(Fee.id == fee_id)
        .first()
    )

    if not fee:
        raise HTTPException(
            status_code=404,
            detail="Fee record not found"
        )

    db.delete(fee)
    db.commit()

    return {
        "message": "Fee deleted successfully"
    }
    
def calculate_fee(
    tuition_fee,
    transport_fee,
    extra_fee,
    total_paid
):
    total_fee = (
        tuition_fee
        + transport_fee
        + extra_fee
    )

    due_amount = total_fee - total_paid

    if total_paid == 0:
        payment_status = "Pending"

    elif due_amount <= 0:

        due_amount = 0

        payment_status = "Paid"

    else:

        payment_status = "Partial"

    return (
        total_fee,
        due_amount,
        payment_status
    )