from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.fee_schema import (
    FeeCreate,
    FeeResponse
)

from app.services.fee_service import *

from app.auth.roles import admin_required
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post(
    "/add",
    response_model=FeeResponse
)
def add_fee(
    fee: FeeCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return create_fee(db, fee)


@router.get(
    "/",
    response_model=list[FeeResponse]
)
def fetch_all_fees(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_all_fees(db)

@router.get("/{student_id}")
def fetch_fee(
    student_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    # Admin can view everyone's fee
    if current_user["role"] == "admin":
        return get_fee_by_student(db, student_id)

    # Student can only view their own fee
    if current_user["student_id"] != student_id:
        raise HTTPException(
            status_code=403,
            detail="You can only view your own fee record."
        )

    return get_fee_by_student(db, student_id)


@router.put(
    "/{fee_id}",
    response_model=FeeResponse
)
def update_fee_record(
    fee_id: int,
    fee: FeeCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return update_fee(
        db,
        fee_id,
        fee
    )


@router.delete("/{fee_id}")
def delete_fee_record(
    fee_id: int,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    return delete_fee(
        db,
        fee_id
    )