from pydantic import BaseModel


class ChampionshipCreateDTO(BaseModel):
    championship_name: str
    title_type_id: int
    year: int


class ChampionshipUpdateDTO(BaseModel):
    championship_name: str | None = None
    title_type_id: int | None = None
    year: int | None = None
