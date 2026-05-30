from datetime import date

from pydantic import BaseModel


class ManagerSchema(BaseModel):
    manager_name: str
    birth_date: date
    nacionality: str

    model_config = {"from_attributes": True}
