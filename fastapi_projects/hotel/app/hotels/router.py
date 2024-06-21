from datetime import date
from fastapi import APIRouter

from app.hotels.dao import HotelDAO


router = APIRouter(
    prefix='/hotels',
    tags=['Отели']
)

@router.get("/{location}", status_code=200) # Ideally should validate data
async def get_hotels(location: str, date_from: date, date_to: date):
    hotels = await HotelDAO.get_all_hotels(location, date_from, date_to)

    return hotels


@router.get("/{hotel_id}/rooms", status_code=200) # Ideally should validate data
async def get_rooms(hotel_id: int, date_from: date, date_to: date):
    rooms = await HotelDAO.get_all_rooms(hotel_id, date_from, date_to)

    return rooms


@router.get("/id/{hotel_id}", status_code=200)
async def get_hotel(hotel_id: int):
    hotel = await HotelDAO.get_hotel(hotel_id)
    return hotel