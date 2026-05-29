from dataclasses import dataclass
from datetime import date


@dataclass
class Player:
    id: int
    player_name: str
    birth_date: date
    posicao: str
    shirt_number: int
    team_id: int