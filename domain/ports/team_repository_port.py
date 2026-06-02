from abc import ABC, abstractmethod


from domain.entities.team_entity import Team

class TeamRepositoryPort(ABC):
    @abstractmethod
    async def get_all(self) -> list[Team]:
        pass

    @abstractmethod
    async def get_by_id(self, team_id: int) -> Team:
        pass

    @abstractmethod
    async def create(self, team: Team) -> Team:
        pass

    @abstractmethod
    async def update(self, team_id: int, team: Team) -> Team:
        pass

    @abstractmethod
    async def delete(self, team_id: int) -> Team:
        pass

    @abstractmethod
    async def exists_by_name(self, team_name: str) -> bool:
        pass