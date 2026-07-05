


'''from fastapi import FastAPI

from app.database.db import Base, engine

from app.models.student import Student

from app.routes.student_routes import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)'''

from fastapi import FastAPI
from app.models.marks import Marks

from app.routes.marks_routes import (router as marks_router)
from app.database.db import Base, engine
from app.models.student import Student
from app.routes.student_routes import router as student_router
from app.models.user import User
from app.routes.auth_routes import (
    router as auth_router
)

from app.models.fee import Fee
from app.routes.fee_routes import(router as fee_router)

from app.models.fee_payment import FeePayment
from app.routes.fee_payment_routes import (router as fee_payment_router)


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System")


@app.get("/")
def home():
    return {
        "message": "Student Management System API Running"
    }


# Student Routes
app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    marks_router,
    prefix="/marks",
    tags=["Marks"]
)

app.include_router(
    fee_router, prefix = "/fees", tags = ["Fees"]
)

app.include_router(
    fee_payment_router, prefix = "/payments", tags = ["Fee Payments"]
)