from fastapi import APIRouter

from app.bookings.dao import BookingsDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование']
)

@router.get("", response_model=list[SBooking])
async def get_bookings():
    return await BookingsDAO.find_all()
