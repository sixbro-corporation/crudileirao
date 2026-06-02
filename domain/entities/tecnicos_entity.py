from dataclasses import dataclass
from datetime import date

@dataclass
class Manager:
    manager_name: str
    birth_date: date
    nacionality: str
    id: int | None = None