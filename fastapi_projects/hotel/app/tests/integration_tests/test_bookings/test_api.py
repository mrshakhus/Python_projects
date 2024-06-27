import json
from httpx import AsyncClient
import pytest


# @pytest.mark.parametrize("room_id, date_from, date_to, rooms_booked, status_code", [
#     (4, "2030-05-01", "2030-05-09", 3, 200),
#     (4, "2030-05-01", "2030-05-09", 4, 200),
#     (4, "2030-05-01", "2030-05-09", 5, 200),
#     (4, "2030-05-01", "2030-05-09", 6, 200),
#     (4, "2030-05-01", "2030-05-09", 7, 200),
#     (4, "2030-05-01", "2030-05-09", 8, 200),
#     (4, "2030-05-01", "2030-05-09", 9, 200),
#     (4, "2030-05-01", "2030-05-09", 10, 200),
#     (4, "2030-05-01", "2030-05-09", 10, 409),
#     (4, "2030-05-01", "2030-05-09", 10, 409),
# ])
# async def test_add_and_get_booking(
#     room_id, date_from, date_to, rooms_booked, status_code, authenticated_ac: AsyncClient
# ):
#     response = await authenticated_ac.post("/bookings", params={
#         "room_id": room_id,
#         "date_from": date_from,
#         "date_to": date_to
#     })

#     assert response.status_code == status_code

#     bookings = await authenticated_ac.get("/bookings")

#     assert len(bookings.json()) == rooms_booked


"""
Получение и удаление бронирований (API-интеграционный-тест)

Давайте попробуем протестировать работу наших эндпоинтов в связке. Сперва получим все бронирования текущего аутентифицированного пользователя через GET /bookings, а затем удалим их всех в цикле через DELETE /bookings/{id}, после чего проверим через GET /bookings, что у пользователя не осталось бронирований.
*По желанию данный тест можно параметризировать для нескольких пользователей.
"""

# @pytest.mark.parametrize()
async def test_get_and_delete_bookings(authenticated_ac: AsyncClient):
    bookings = await authenticated_ac.get("/bookings")

    print(bookings.json()[0]["user_id"])
    # for _ in range(len(json(bookings))):



