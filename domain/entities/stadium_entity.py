from dataclasses import dataclass

@dataclass
class Stadium:
    id: int
    stadium_name: str
    city: str
    capacity: int