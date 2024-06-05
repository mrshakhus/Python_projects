from fastapi import APIRouter, HTTPException

from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.schemas import SUserAuth


router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и регистрация"]
)

@router.post("/register")
async def register_user(user_data: SUserAuth):
    user_exists_already = await UsersDAO.find_one_or_none(email=user_data.email)
    if user_exists_already:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)

@router.post("/login")
async def login_user(user_data: SUserAuth):
    user_exists_already = await UsersDAO.find_one_or_none(email=user_data.email)
    if not user_exists_already:
        raise HTTPException(status_code=500)
    
    hashed_password = get_password_hash(user_data.password)
    user_exists = await UsersDAO.find_one_or_none(email=user_data.email, hashed_password=hashed_password)
    if not user_exists:
        raise HTTPException(status_code=500)
    