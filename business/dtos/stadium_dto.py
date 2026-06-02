from pydantic import BaseModel


class CreateStadiumDTO(BaseModel):
    stadium_name: str
    city: str
    capacity: int


class UpdateStadiumDTO(BaseModel):
    stadium_name: str | None = None
    city: str | None = None
    capacity: int | None = None