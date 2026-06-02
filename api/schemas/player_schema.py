from datetime import date
from pydantic import BaseModel


class PlayerSchema(BaseModel):
    player_name: str
    birth_date: date
    posicao: str
    shirt_number: int
    team_id: int

    model_config = {"from_attributes": True}