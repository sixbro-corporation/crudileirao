from datetime import date

from pydantic import BaseModel


class ManagerInputDTO(BaseModel):
    manager_name: str
    birth_date: date
    nacionality: str


class ManagerUpdateDTO(BaseModel):
    manager_name: str | None = None
    birth_date: date | None = None
    nacionality: str | None = None
