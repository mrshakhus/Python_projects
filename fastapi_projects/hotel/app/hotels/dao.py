from datetime import date

from sqlalchemy import and_, func, or_, select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def get_all(
        cls,
        location: str,
        date_from: date,
        date_to: date
    ):
        async with async_session_maker() as session:
            """
            --1.
            WITH needed_hotels AS(
            SELECT id, room_quantity
            FROM hotels
            WHERE location LIKE '%Алтай%'
            ),
            """
            needed_hotels = (
                select(Hotels.id, Hotels.room_quantity)
                .where(Hotels.location.like(f'%{location}%'))
                .cte("needed_hotels")
                )

            """
            --2.
            all_booked_rooms AS(
            SELECT room_id
            FROM bookings
            WHERE (date_from >= '2023-05-15' AND date_from <= '2023-06-20') OR
                (date_from <= '2023-05-15' AND date_to > '2023-05-15')
            ),
            """
            all_booked_rooms = (
                select(Bookings.room_id).where(
                    or_(
                        and_(
                            Bookings.date_from >= date_from,
                            Bookings.date_from <= date_to
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_from
                        )
                    )
                ).cte("all_booked_rooms")
            )

            """
            --3.
            needed_booked_rooms AS(
            SELECT hotel_id
            FROM rooms
            INNER JOIN all_booked_rooms ON all_booked_rooms.room_id = rooms.id
            )
            """
            needed_booked_rooms = (
                select(Rooms.hotel_id)
                .join(
                    all_booked_rooms,
                    all_booked_rooms.c.room_id == Rooms.id
                ).cte("needed_booked_rooms")
            )

            """
            --4.
            SELECT needed_hotels.room_quantity - COUNT(needed_booked_rooms.hotel_id) FROM needed_hotels 
            LEFT JOIN needed_booked_rooms ON needed_booked_rooms.hotel_id = needed_hotels.id
            GROUP BY needed_hotels.id, needed_hotels.room_quantity
            """
            get_needed_hotels = (
                select(
                    needed_hotels.c.room_quantity - func.count(needed_booked_rooms.c.hotel_id)
                )
                .join(
                    needed_booked_rooms,
                    needed_booked_rooms.c.hotel_id == needed_hotels.c.id,
                    isouter=True
                )
                .group_by(needed_hotels.c.id, needed_hotels.c.room_quantity)
            )

            needed_hotels = await session.execute(get_needed_hotels)
            return needed_hotels.mappings().all()