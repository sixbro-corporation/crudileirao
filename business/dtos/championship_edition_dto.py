from pydantic import BaseModel


class CreateChampionshipEditionDTO(BaseModel):
    year: int


class UpdateChampionshipEditionDTO(BaseModel):
    year: int | None = None