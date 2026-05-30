from dataclasses import dataclass

@dataclass
class TitleType:
    description: str
    id: int | None = None
