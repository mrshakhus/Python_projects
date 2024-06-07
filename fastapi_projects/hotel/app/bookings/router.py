from fastapi import APIRouter, Depends

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)

@router.get("", response_model=list[SBooking])
async def get_bookings(user: Users = Depends(get_current_user)):
    print(user.email, user.id)
    return await BookingsDAO.find_all()
