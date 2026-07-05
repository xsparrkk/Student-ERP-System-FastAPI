from sqlalchemy import Column, BigInteger, String, Text
from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    username = Column(
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        Text,
        nullable=False
    )

    role = Column(
        String(20),
        default="student"
    )
    
    student_id = Column(
        String(20),
        unique=True,
        nullable=True
    )