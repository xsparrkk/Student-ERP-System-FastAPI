from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import BigInteger

from app.database.db import Base


class Marks(Base):

    __tablename__ = "marks"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )

    student_id = Column(
        String(20),
        nullable=False
    )

    student_class = Column(
        "class",
        Integer,
        nullable=False
    )

    subject = Column(
        String(100),
        nullable=False
    )

    marks = Column(
        Integer,
        nullable=False
    )

    year = Column(
        Integer,
        nullable=False
    )