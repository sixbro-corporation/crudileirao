from domain.entities.achievement_entity import Achievement
from domain.ports.achievement_repository_port import AchievementRepositoryPort
from .dtos.achievement_dto import CreateAchievementDTO, UpdateAchievementDTO


class AchievementUseCase:
    def __init__(self, repository: AchievementRepositoryPort) -> None:
        self.repository = repository

    async def create(self, dto: CreateAchievementDTO) -> Achievement:
        existing = await self.repository.exists_by_team_and_edition(dto.team_id, dto.edition_id)
        if existing:
            raise ValueError("Essa conquista já existe")

        achievement = Achievement(id=None, team_id=dto.team_id, edition_id=dto.edition_id)
        return await self.repository.create(achievement)

    async def get_all_achievements(self) -> list[Achievement]:
        return await self.repository.get_all()

    async def get_achievement(self, achievement_id: int) -> Achievement:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise ValueError("A conquista solicitada não existe")
        return existing

    async def update_achievement(self, achievement_id: int, dto: UpdateAchievementDTO) -> Achievement:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise ValueError("A conquista solicitada não existe")

        achievement = Achievement(
            id=achievement_id,
            team_id=dto.team_id if dto.team_id is not None else existing.team_id,
            edition_id=dto.edition_id if dto.edition_id is not None else existing.edition_id,
        )
        return await self.repository.update(achievement_id, achievement)

    async def delete(self, achievement_id: int) -> None:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise ValueError("Essa conquista não existe")
        await self.repository.delete(achievement_id)