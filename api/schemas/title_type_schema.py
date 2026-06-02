from pydantic import BaseModel


class TitleTypeSchema(BaseModel):
    description: str

    model_config = {"from_attributes": True}