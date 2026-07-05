from sqlalchemy import Column, BigInteger, Integer, String, Date

from app.database.db import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(BigInteger, primary_key=True, index=True)

    student_id = Column(String(20), unique=True, nullable=False)

    name = Column(String(100), nullable=False)

    age = Column(Integer, nullable=False)

    doj = Column(Date, nullable=False)

    student_class = Column("class", Integer, nullable=False)

    email = Column(String(255), unique=True)

    phone_number = Column(String(15))