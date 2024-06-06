from fastapi import APIRouter, HTTPException, Response, status

from app.users.auth import authenticate_user, create_access_token, get_password_hash
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
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("bookings_access_cookie", access_token, httponly=True)
    return {"access_token": access_token}

    
    