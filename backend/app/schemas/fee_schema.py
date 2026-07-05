from decimal import Decimal

from pydantic import BaseModel


class FeeCreate(BaseModel):

    student_id: str
    transport_fee: Decimal
    tuition_fee: Decimal
    extra_fee: Decimal
    total_fee: Decimal
    paid_amount: Decimal
    due_amount: Decimal
    payment_status: str


class FeeResponse(FeeCreate):

    id: int

    class Config:
        from_attributes = True