from dataclasses import dataclass
@dataclass

class Achievement:
    team_id: int
    championship_id: int
    id: int | None = None