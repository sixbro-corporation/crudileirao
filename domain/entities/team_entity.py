from dataclasses import dataclass
from datetime import date

@dataclass
class Team:
    id: int
    team_name: str
    state: str
    fundacao: date
    tecnico_id: int
    estadio_id: int