from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.auth_schema import (
    UserRegister,
    UserLogin
)

from app.auth.auth_service import (
    register_user,
    login_user
)

router = APIRouter()

#Register User

@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(db,user)

#Login Route
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        user
    )