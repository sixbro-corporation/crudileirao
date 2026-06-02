from abc import ABC, abstractmethod

from domain.entities.team_entity import Team


class TeamRepositoryPort(ABC):

    @abstractmethod
    async def get_all(self) -> list[Team]: ...

    @abstractmethod
    async def get_by_id(self, team_id: int) -> Team | None: ...

    @abstractmethod
    async def create(self, team: Team) -> Team: ...

    @abstractmethod
    async def update(self, team_id: int, team: Team) -> Team | None: ...

    @abstractmethod
    async def delete(self, team_id: int) -> bool: ...

    @abstractmethod
    async def exists_by_name(self, team_name: str) -> bool: ...

    @abstractmethod
    async def exists_by_manager(self, manager_id: int) -> bool: ...