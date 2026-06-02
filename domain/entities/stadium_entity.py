from dataclasses import dataclass

@dataclass
class Stadium:
    stadium_name: str
    city: str
    capacity: int
    id: int | None = None