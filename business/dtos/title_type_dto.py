from pydantic import BaseModel


class CreateTitleTypeDTO(BaseModel):
    description: str


class UpdateTitleTypeDTO(BaseModel):
    description: str | None = None