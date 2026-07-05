from sqlalchemy import (Column,BigInteger,String,Numeric,
    Date,Text,ForeignKey,func)

from app.database.db import Base


class FeePayment(Base):

    __tablename__ = "fee_payments"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    fee_id = Column(
        BigInteger,
        ForeignKey("fee.id"),
        nullable=False
    )

    student_id = Column(
        String(20),
        ForeignKey("student.student_id"),
        nullable=False
    )

    payment_amount = Column(
        Numeric(10,2),
        nullable=False
    )

    payment_mode = Column(
        String(30),
        nullable=False
    )

    payment_date = Column(
        Date,
        server_default=func.current_date()
    )

    remarks = Column(Text)