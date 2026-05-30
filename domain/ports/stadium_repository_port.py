from abc import ABC, abstractmethod
from domain.entities.stadium_entity import Stadium


class StadiumRepositoryPort(ABC):

    @abstractmethod
    async def get_all(self) -> list[Stadium]: ...

    @abstractmethod
    async def get_by_id(self, stadium_id: int) -> Stadium | None: ...

    @abstractmethod
    async def create(self, stadium: Stadium) -> Stadium: ...

    @abstractmethod
    async def update(self, stadium_id: int, stadium: Stadium) -> Stadium | None: ...

    @abstractmethod
    async def delete(self, stadium_id: int) -> bool: ...