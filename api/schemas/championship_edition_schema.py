from pydantic import BaseModel


class ChampionshipEditionSchema(BaseModel):
    championship_id: int
    year: int

    model_config = {"from_attributes": True}