from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Numeric

from app.database.db import Base


class Fee(Base):

    __tablename__ = "fee"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        String(20),
        nullable=False
    )

    

    transport_fee = Column(
        Numeric(10,2),
        nullable=False
    )
    
    tuition_fee = Column(
        Numeric(10,2),
        nullable=False
    )


    extra_fee = Column(
        Numeric(10,2),
        nullable=False
    )

    total_fee = Column(
        Numeric(10,2),
        nullable=False
    )

    paid_amount = Column(
        Numeric(10,2),
        nullable=False
    )

    due_amount = Column(
        Numeric(10,2),
        nullable=False
    )

    payment_status = Column(
        String(20),
        nullable=False
    )