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
        #first I need to get available rooms in a hotel
        #then check whether there are >= 1 room

        #1 Don't know how to do yet

        #2 
        async with async_session_maker() as session:
            all_booked_rooms = select(Bookings).where(
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    )                    )
            ).cte("all_booked_rooms")

            hotel_id_of_booked_rooms = (
                select(
                    (Rooms.quantity - func.count(all_booked_rooms.c.room_id)
                    .filter(all_booked_rooms.c.room_id.is_not(None))
                    .label("rooms_left"))
                )
                .select_from(Rooms)
                .join(
                    all_booked_rooms,
                    all_booked_rooms.c.room_id == Rooms.id,
                )
                .group_by(Rooms.hotel_id)
            )

            rooms_left = await session.execute(hotel_id_of_booked_rooms)
            rooms_left: int = rooms_left.scalar()

        # async with async_session_maker() as session:
        #     booked_rooms = select(Bookings).where(
        #         and_(
        #             Bookings.room_id == room_id,
        #             or_(
        #                 and_(
        #                     Bookings.date_from >= date_from,
        #                     Bookings.date_from <= date_to
        #                 ),
        #                 and_(
        #                     Bookings.date_from <= date_from,
        #                     Bookings.date_to > date_from
        #                 )
        #             )
        #         )
        #     ).cte("booked_rooms")

        #     get_rooms_left = (
        #         select(
        #             (Rooms.quantity - func.count(booked_rooms.c.room_id)
        #             .filter(booked_rooms.c.room_id.is_not(None))
        #             .label("rooms_left"))
        #         )
        #         .select_from(Rooms)
        #         .join(
        #             booked_rooms,
        #             booked_rooms.c.room_id == Rooms.id,
        #             isouter=True
        #         )
        #         .where(Rooms.id == room_id)
        #         .group_by(Rooms.quantity, booked_rooms.c.room_id)
        #     )

        #     rooms_left = await session.execute(get_rooms_left)
        #     rooms_left: int = rooms_left.scalar()