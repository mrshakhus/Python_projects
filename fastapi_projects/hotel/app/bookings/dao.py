from datetime import date
from app.bookings.models import Bookings
from app.dao.base import BaseDAO


class BookingsDAO(BaseDAO):
    model = Bookings
    
    @classmethod
    async def add(
        cls,
        room_id: int,
        date_from: date,
        date_to: date,
        ):
        """
        WITH booked_rooms AS(
        SELECT * FROM bookings
        WHERE room_id = 1 AND
        (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
        (date_from <= '2023-05-15' AND date_to > '2023-05-15')
        )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms 
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id
        """

