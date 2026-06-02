from pydantic import BaseModel


class AchievementSchema(BaseModel):
    team_id: int
    edition_id: int

    model_config = {"from_attributes": True}
