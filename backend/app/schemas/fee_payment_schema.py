from datetime import date

from pydantic import BaseModel


class FeePaymentCreate(BaseModel):

    

    payment_amount: float

    payment_mode: str

    remarks: str | None = None


class FeePaymentResponse(BaseModel):

    id: int

    fee_id: int

    student_id: str

    payment_amount: float

    payment_mode: str

    payment_date: date

    remarks: str | None

    class Config:
        from_attributes = True