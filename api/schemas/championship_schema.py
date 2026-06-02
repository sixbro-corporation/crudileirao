from pydantic import BaseModel


class ChampionshipSchema(BaseModel):
    championship_name: str
    title_type_id: int
    year: int

    model_config = {"from_attributes": True}
