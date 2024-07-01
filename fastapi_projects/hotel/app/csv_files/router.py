import json
import shutil
import pandas as pd
from fastapi import APIRouter, UploadFile
from sqlalchemy import insert
from app.database import engine
from app.hotels.models import Hotels
from app.database import async_session_maker


router = APIRouter(
    prefix = "/csv_files",
    tags = ["Загрузка csv файлов"]
)

@router.post("/hotels")
async def upload_hotels_csv_file(file: UploadFile):
    file_path = "app/static/csv_files/hotel.csv"
    with open(file_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

        # df = pd.read_csv(file_path)
        # df.to_sql('hotels', con=engine, if_exists='append', index=False)

    df = pd.read_csv(file_path, delimiter=';')

    async with async_session_maker() as session:
        for index, row in df.iterrows():
            print(json.loads(row['services']))
            hotel = {
                "name": row['name'],
                "location": row['location'],
                "services": row['services'],
                "room_quantity": row['room_quantity'],
                "image_id": row['image_id']
            }


            # add_hotel = (
            #     insert(Hotels)
            #     .values(hotel)
            # )
            # await session.execute(add_hotel)

        # await session.commit()
