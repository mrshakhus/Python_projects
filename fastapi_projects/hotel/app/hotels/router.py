from datetime import date
from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCanNotBeBooked
from app.hotels.dao import HotelDAO
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bhotels',
    tags=['Отели']
)

@router.get("/{location}", status_code=200)
async def get_hotels(location: str, date_from: date, date_to: date):
    hotels = await HotelDAO.get_all(location, date_from, date_to)

    return hotels