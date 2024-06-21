from pydantic import BaseModel, ConfigDict, json

class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: json
    room_quantity: int 
    image_id: int

    model_config = ConfigDict(from_attributes=True)