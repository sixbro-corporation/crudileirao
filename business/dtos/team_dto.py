from datetime import date

from pydantic import BaseModel


class CreateTeamDTO(BaseModel):
    team_name: str
    state: str
    creation: int
    manager_id: int
    estadio_id: int


class UpdateTeamDTO(BaseModel):
    team_name: str | None = None
    state: str | None = None
    creation: int | None = None
    manager_id: int | None = None
    estadio_id: int | None = None
