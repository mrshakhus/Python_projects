from fastapi import Depends, FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead
from auth.database import User

app = FastAPI(
    title = 'Trading App'
)
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"

@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonym"

#printing in response errors which may occur in server 
@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


# #implementing GET method and validation of data stored in server
# fake_users = [
#     {"id": 1, "role": "admin", "name": "Mike"},
#     {"id": 2, "role": "trader", "name": "John"},
#     {"id": 3, "role": "investor", "name": "Steve"},
#     {"id": 4, "role": "trader", "name": "Tom", "degree": [
#      {"id": 1, "created_at": "2032-04-23T10:20:30", "degree_type": "expert"}
#         ]},
# ]

# class Degree_type(Enum):
#     newbie = "newbie"
#     expert = "expert"

# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     degree_type: Degree_type

# class User(BaseModel):
#     id: int
#     role: str
#     name: str
#     degree: Optional[List[Degree]] = []

# @app.get("/users/{user_id}", response_model=List[User])
# def get_user_by_id(user_id: int):
#     return [user for user in fake_users if user.get("id") == user_id]


# #Getting information about trades
# fake_trades = [
#     {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 57, "amount": 2.12},
#     {"id": 2, "user_id": 1, "currency": "ETH", "side": "buy", "price": 50, "amount": 1.32},
#     {"id": 3, "user_id": 2, "currency": "TON", "side": "sell", "price": 10, "amount": 10.76}
# ]

# @app.get("/trades")
# def get_trades(length: int = 1, offset: int = 0):
#     return fake_trades[offset:][:length]


# #implementing POST method and changing name
# fake_users2 = [
#     {"id": 1, "role": "admin", "name": "Mike"},
#     {"id": 2, "role": "trader", "name": "John"},
#     {"id": 3, "role": "investor", "name": "Steve", }
# ]

# @app.post("/users/{user_id}")
# def change_user_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user["id"] == user_id, fake_users2))[0]
#     current_user["name"] = new_name
#     return {"status": 200, "user_info": current_user}


# #validating user input with pydentic and typing
# class Trade(BaseModel):
#     id: int
#     user_id: int
#     currency: str = Field(max_length=4)
#     side: str
#     price: float = Field(ge=0)
#     amount: float = Field(gt=0)

# @app.post("/trades")
# def add_trade(trade: List[Trade]):
#     fake_trades.extend(trade)
#     return {"status": 200, "data": fake_trades}

#again