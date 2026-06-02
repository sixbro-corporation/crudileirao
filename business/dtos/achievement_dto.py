from pydantic import BaseModel


class CreateAchievementDTO(BaseModel):
    team_id: int
    edition_id: int


class UpdateAchievementDTO(BaseModel):
    team_id: int | None = None
    edition_id: int | None = None
