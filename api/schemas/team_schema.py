from pydantic import BaseModel
from datetime import date

class TeamSchema(BaseModel):
    team_name: str
    state: str
    creation: int
    manager_id: int
    stadium_id: int

    model_config = {"from_attributes": True}