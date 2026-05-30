from abc import ABC, abstractmethod
from domain.entities.player_entity import Player


class PlayerRepositoryPort(ABC):

    @abstractmethod
    async def get_all(self) -> list[Player]: ...

    @abstractmethod
    async def get_by_id(self, player_id: int) -> Player | None: ...

    @abstractmethod
    async def create(self, player: Player) -> Player: ...

    @abstractmethod
    async def update(self, player_id: int, player: Player) -> Player | None: ...

    @abstractmethod
    async def delete(self, player_id: int) -> bool: ...