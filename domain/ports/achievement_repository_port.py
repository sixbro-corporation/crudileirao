from abc import ABC, abstractmethod


from domain.entities.achievement_entity import Achievement

class AchievementRepositoryPort(ABC):
    @abstractmethod
    async def get_all(self) -> list[Achievement]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Achievement:
        pass

    @abstractmethod
    async def create(self, achievement: Achievement) -> Achievement:
        pass

    @abstractmethod
    async def update(self, id: int, achievement: Achievement) -> Achievement:
        pass

    @abstractmethod
    async def delete(self, id: int) -> Achievement:
        pass

    @abstractmethod
    async def exists_by_team_and_edition(self, team_id: int, edition_id: int) -> bool:
        pass