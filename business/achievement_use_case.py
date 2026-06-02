from domain.entities.achievement_entity import Achievement
from domain.ports.achievement_repository_port import AchievementRepositoryPort
from .dtos.achievement_dto import CreateAchievementDTO, UpdateAchievementDTO


class AchievementUseCase:
    def __init__(self, repository: AchievementRepositoryPort) -> None:
        self.repository = repository

    async def create(self, dto: CreateAchievementDTO) -> Achievement:
        existing = await self.repository.exists_by_team_and_championship(dto.team_id, dto.championship_id)
        if existing:
            raise ValueError("Essa conquista já existe")

        achievement = Achievement(team_id=dto.team_id, championship_id=dto.championship_id)
        return await self.repository.create(achievement)

    async def get_all_achievements(self) -> list[Achievement]:
        return await self.repository.get_all()

    async def update_achievement(self, achievement_id: int, dto: UpdateAchievementDTO) -> Achievement:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise ValueError("A conquista solicitada não existe")

        achievement = Achievement(
            team_id=dto.team_id if dto.team_id is not None else existing.team_id,
            championship_id=dto.championship_id if dto.championship_id is not None else existing.championship_id,
            id=achievement_id,
        )
        return await self.repository.update(achievement, achievement_id)

    async def get_achievement(self, achievement_id: int) -> Achievement:
        return await self.repository.get_by_id(achievement_id)

    async def delete(self, achievement_id: int) -> None:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise ValueError("Essa conquista não existe")
        await self.repository.delete(achievement_id)
