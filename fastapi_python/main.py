from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List


app = FastAPI(
    title = 'Trading App'
)

#implementing GET method
fake_users = [
    {"id": 1, "role": "admin", "name": "Mike"},
    {"id": 2, "role": "trader", "name": "John"},
    {"id": 3, "role": "investor", "name": "Steve"}
]

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 57, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "ETH", "side": "buy", "price": 50, "amount": 1.32},
    {"id": 3, "user_id": 2, "currency": "TON", "side": "sell", "price": 10, "amount": 10.76}
]

@app.get("/trades")
def get_trades(length: int = 1, offset: int = 0):
    return fake_trades[offset:][:length]

#implementing POST method
fake_users2 = [
    {"id": 1, "role": "admin", "name": "Mike"},
    {"id": 2, "role": "trader", "name": "John"},
    {"id": 3, "role": "investor", "name": "Steve", }
]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user["id"] == user_id, fake_users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "user_info": current_user}


#validating user input with pydentic and typing
class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=4)
    side: str
    price: float = Field(ge=0)
    amount: float = Field(gt=0)

@app.post("/trades")
def add_trade(trade: List[Trade]):
    fake_trades.extend(trade)
    return {"status": 200, "data": fake_trades}