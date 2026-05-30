from dataclasses import dataclass
from datetime import date

@dataclass
class Team:
    id: int
    team_name: str
    state: str
    creation: date
    manager_id: int
    stadium_id: int