
    
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.student import Student
from app.models.user import User

from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token
)

# Register User

def register_user(
    db: Session,
    user_data
):
    
    existing_user = (
        db.query(User)
        .filter(
            User.username
            == user_data.username
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(
            user_data.password
        ),
        student_id=user_data.student_id,
        role="student")
   
    

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "User registered successfully"
    }
    
# Login User 
def login_user(
    db: Session,
    login_data
):

    user = (
        db.query(User)
        .filter(
            User.username
            == login_data.username
        )
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        login_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.username,
            "role": user.role,
            "student_id": user.student_id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "student_id": user.student_id,
        "username": user.username,
        "email": user.email,
        "role": user.role
        
    }
    
    