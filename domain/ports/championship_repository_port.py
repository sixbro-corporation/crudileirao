from abc import ABC, abstractmethod
from domain.entities.championship_entity import Championship

class ChampionshipRepositoryPort(ABC):
    @abstractmethod
    async def get_all(self) -> list[Championship]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Championship:
        pass

    @abstractmethod
    async def create(self, championship: Championship) -> Championship:
        pass

    @abstractmethod
    async def update(self, id: int, championship: Championship) -> Championship:
        pass

    @abstractmethod
    async def delete(self, id: int) -> Championship:
        pass