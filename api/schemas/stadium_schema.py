from pydantic import BaseModel


class StadiumSchema(BaseModel):
    stadium_name: str
    city: str
    capacity: int

    model_config = {"from_attributes": True}