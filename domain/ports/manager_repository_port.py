from abc import ABC, abstractmethod
from domain.entities.tecnicos_entity import Manager


class ManagerRepositoryPort(ABC):

    @abstractmethod
    async def get_all(self) -> list[Manager]: ...

    @abstractmethod
    async def get_by_id(self, manager_id: int) -> Manager | None: ...

    @abstractmethod
    async def create(self, manager: Manager) -> Manager: ...

    @abstractmethod
    async def update(self, manager_id: int, manager: Manager) -> Manager | None: ...

    @abstractmethod
    async def delete(self, manager_id: int) -> bool: ...

    @abstractmethod
    async def exists_by_name(self, team_name: str) -> bool:
        pass