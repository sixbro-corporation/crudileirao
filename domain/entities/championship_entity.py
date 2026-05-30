from dataclasses import dataclass

@dataclass
class Championship:
    championship_name: str
    title_type_id: int
    year: int
    id: int | None = None