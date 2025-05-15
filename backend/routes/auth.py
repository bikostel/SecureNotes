from fastapi import APIRouter, HTTPException
from backend.models.user import UserCreate, UserLogin, UserResponse
from backend.security.passwords import hash_password, verify_password
from backend.security.jwt_handler import create_access_token
from backend.database.fake_db import fake_users_db

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    hashed_password = hash_password(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "password": hashed_password
    }

    return {"username": user.username}


@router.post("/login")
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

