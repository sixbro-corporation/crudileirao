from datetime import date
from pydantic import BaseModel


class CreatePlayerDTO(BaseModel):
    player_name: str
    birth_date: date
    posicao: str
    shirt_number: int
    team_id: int


class UpdatePlayerDTO(BaseModel):
    player_name: str | None = None
    birth_date: date | None = None
    posicao: str | None = None
    shirt_number: int | None = None
    team_id: int | None = None