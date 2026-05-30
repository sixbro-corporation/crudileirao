from dataclasses import dataclass

@dataclass
class Championship:
    id: int
    championship_name: str
    title_type_id: int
    year: int