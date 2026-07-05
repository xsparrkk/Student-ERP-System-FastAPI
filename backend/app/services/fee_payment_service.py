from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException

from app.models.fee import Fee
from app.models.fee_payment import FeePayment

from app.services.fee_service import calculate_fee

#Record Payment 
def record_payment(
    db: Session,
    payment_data,
    current_user
):

    fee = (
        db.query(Fee)
        .filter(
            Fee.student_id == current_user["student_id"]
        )
        .first()
    )

    if not fee:
        raise HTTPException(
            status_code=404,
            detail="Fee record not found"
        )

    payment = FeePayment(

        fee_id=fee.id,

        student_id=current_user["student_id"],

        payment_amount=payment_data.payment_amount,

        payment_mode=payment_data.payment_mode,

        remarks=payment_data.remarks
    )

    db.add(payment)

    db.commit()

    db.refresh(payment)

    total_paid = (

        db.query(
            func.sum(
                FeePayment.payment_amount
            )
        )

        .filter(
            FeePayment.fee_id == fee.id
        )

        .scalar()

        or 0
    )

    total_fee, due, status = calculate_fee(

        fee.tuition_fee,

        fee.transport_fee,

        fee.extra_fee,

        total_paid
    )

    fee.total_fee = total_fee

    fee.paid_amount = total_paid

    fee.due_amount = due

    fee.payment_status = status

    db.commit()

    return payment

# Payment History 
def get_student_payments(
    db: Session,
    student_id: str
):

    return (

        db.query(FeePayment)

        .filter(
            FeePayment.student_id == student_id
        )

        .all()
    )
    
# Payment Details

def get_payment_by_id(
    db: Session,
    payment_id: int
):

    payment = (

        db.query(FeePayment)

        .filter(
            FeePayment.id == payment_id
        )

        .first()
    )

    if not payment:

        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment