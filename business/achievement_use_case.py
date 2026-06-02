from domain.entities.achievement_entity import Achievement
from domain.exceptions.business_exception import BusinessException
from domain.ports.achievement_repository_port import AchievementRepositoryPort
from domain.ports.championship_edition_repository_port import ChampionshipEditionRepositoryPort
from domain.ports.team_repository_port import TeamRepositoryPort
from .dtos.achievement_dto import CreateAchievementDTO, UpdateAchievementDTO


class AchievementUseCase:
    def __init__(
        self,
        repository: AchievementRepositoryPort,
        team_repository: TeamRepositoryPort,
        edition_repository: ChampionshipEditionRepositoryPort,
    ) -> None:
        self.repository = repository
        self.team_repository = team_repository
        self.edition_repository = edition_repository

    async def create(self, dto: CreateAchievementDTO) -> Achievement:
        if not await self.team_repository.get_by_id(dto.team_id):
            raise BusinessException("O time informado não existe")

        if not await self.edition_repository.get_by_id(dto.edition_id):
            raise BusinessException("A edição de campeonato informada não existe")

        if await self.repository.exists_by_team_and_edition(dto.team_id, dto.edition_id):
            raise BusinessException("Este time já possui essa conquista registrada")

        achievement = Achievement(id=None, team_id=dto.team_id, edition_id=dto.edition_id)
        return await self.repository.create(achievement)

    async def get_all_achievements(self) -> list[Achievement]:
        return await self.repository.get_all()

    async def get_achievement(self, achievement_id: int) -> Achievement:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise BusinessException("Conquista não encontrada")
        return existing

    async def update_achievement(self, achievement_id: int, dto: UpdateAchievementDTO) -> Achievement:
        existing = await self.repository.get_by_id(achievement_id)
        if not existing:
            raise BusinessException("Conquista não encontrada")

        new_team_id = dto.team_id if dto.team_id is not None else existing.team_id
        new_edition_id = dto.edition_id if dto.edition_id is not None else existing.edition_id

        if dto.team_id is not None and not await self.team_repository.get_by_id(dto.team_id):
            raise BusinessException("O time informado não existe")

        if dto.edition_id is not None and not await self.edition_repository.get_by_id(dto.edition_id):
            raise BusinessException("A edição de campeonato informada não existe")

        achievement = Achievement(id=achievement_id, team_id=new_team_id, edition_id=new_edition_id)
        return await self.repository.update(achievement_id, achievement)

    async def delete(self, achievement_id: int) -> None:
        if not await self.repository.get_by_id(achievement_id):
            raise BusinessException("Conquista não encontrada")
        await self.repository.delete(achievement_id)