from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy.orm import Session

import bcrypt

from database import (
    engine,
    SessionLocal
)

from auth import (
    Base,
    User
)

from schemas import (
    UserCreate,
    UserLogin
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


# -----------------------------------
# DATABASE SESSION
# -----------------------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# -----------------------------------
# SIGNUP
# -----------------------------------

@app.post("/signup")
def signup(user: UserCreate):

    db = SessionLocal()

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Account already exists"
        )

    hashed_password = bcrypt.hashpw(
        user.password.encode(),
        bcrypt.gensalt()
    )

    new_user = User(
        email=user.email,
        password=hashed_password.decode()
    )

    db.add(new_user)
    db.commit()

    return {
        "message":
        "Account created successfully"
    }


# -----------------------------------
# LOGIN
# -----------------------------------

@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing:

        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    if not bcrypt.checkpw(
        user.password.encode(),
        existing.password.encode()
    ):

        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    return {
        "message":
        "Login successful",
        "email":
        existing.email
    }