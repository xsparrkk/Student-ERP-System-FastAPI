

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.fee_payment_schema import (
    FeePaymentCreate,
    FeePaymentResponse
)

from app.services.fee_payment_service import (
    record_payment,
    get_student_payments,
    get_payment_by_id
)
from app.auth.dependencies import get_current_user
from app.auth.roles import admin_required

router = APIRouter()

# Record payment
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.auth.dependencies import get_current_user

from app.schemas.fee_payment_schema import (
    FeePaymentCreate,
    FeePaymentResponse
)

from app.services.fee_payment_service import (
    record_payment,
    get_student_payments,
    get_payment_by_id
)

router = APIRouter()


# Record payment
@router.post(
    "/",
    response_model=FeePaymentResponse
)
def add_payment(
    payment: FeePaymentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    # ✅ Role Check
    if current_user["role"] != "student":
        raise HTTPException(
            status_code=403,
            detail="Only students can make fee payments."
        )

    return record_payment(
        db,
        payment,
        current_user
    )
    
# Student History 
@router.get("/student/{student_id}", response_model=list[FeePaymentResponse])
def payment_history(student_id: str,db: Session = Depends(get_db)):
    return get_student_payments(
        db,
        student_id
    )
    
# Payment Details 
@router.get("/{payment_id}",response_model=FeePaymentResponse)
def payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    return get_payment_by_id(db,payment_id)