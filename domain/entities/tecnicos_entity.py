from dataclasses import dataclass
from datetime import date

@dataclass
class Manager:
    id: int
    manager_name: str
    birth_date: date
    nacionality: str