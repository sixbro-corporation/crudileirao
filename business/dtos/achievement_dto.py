from pydantic import BaseModel


class CreateAchievementDTO(BaseModel):
    team_id: int
    championship_id: int


class UpdateAchievementDTO(BaseModel):
    team_id: int | None = None
    championship_id: int | None = None
