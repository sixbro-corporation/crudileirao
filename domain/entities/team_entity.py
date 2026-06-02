from dataclasses import dataclass
from datetime import date

@dataclass
class Team:
    team_name: str
    state: str
    creation: int
    manager_id: int
    stadium_id: int
    id: int | None = None