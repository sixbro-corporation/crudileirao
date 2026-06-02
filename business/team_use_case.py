from domain.entities.team_entity import Team
from domain.exceptions.business_exception import BusinessException
from domain.ports.manager_repository_port import ManagerRepositoryPort
from domain.ports.stadium_repository_port import StadiumRepositoryPort
from domain.ports.team_repository_port import TeamRepositoryPort
from .dtos.team_dto import CreateTeamDTO


class TeamUseCase:
    def __init__(
        self,
        team_repository: TeamRepositoryPort,
        manager_repository: ManagerRepositoryPort,
        stadium_repository: StadiumRepositoryPort,
    ) -> None:
        self.repository = team_repository
        self.manager_repository = manager_repository
        self.stadium_repository = stadium_repository

    async def create_team(self, dto: CreateTeamDTO) -> Team:
        if await self.repository.exists_by_name(dto.team_name):
            raise BusinessException(f"Já existe um time com o nome '{dto.team_name}'")

        if not await self.manager_repository.get_by_id(dto.manager_id):
            raise BusinessException("O técnico informado não existe")

        if not await self.stadium_repository.get_by_id(dto.estadio_id):
            raise BusinessException("O estádio informado não existe")

        if await self.repository.exists_by_manager(dto.manager_id):
            raise BusinessException("Este técnico já está associado a outro time")

        team = Team(
            team_name=dto.team_name,
            state=dto.state,
            creation=dto.creation,
            manager_id=dto.manager_id,
            stadium_id=dto.estadio_id,
        )
        return await self.repository.create(team)

    async def get_all_teams(self) -> list[Team]:
        return await self.repository.get_all()

    async def get_team(self, team_id: int) -> Team:
        existing = await self.repository.get_by_id(team_id)
        if not existing:
            raise BusinessException("Time não encontrado")
        return existing

    async def update_team(
        self,
        team_id: int,
        team_name: str | None = None,
        state: str | None = None,
        creation=None,
        manager_id: int | None = None,
        stadium_id: int | None = None,
    ) -> Team:
        existing = await self.repository.get_by_id(team_id)
        if not existing:
            raise BusinessException("Time não encontrado")

        new_manager_id = manager_id if manager_id is not None else existing.manager_id
        new_stadium_id = stadium_id if stadium_id is not None else existing.stadium_id

        if manager_id is not None and manager_id != existing.manager_id:
            if not await self.manager_repository.get_by_id(manager_id):
                raise BusinessException("O técnico informado não existe")
            if await self.repository.exists_by_manager(manager_id):
                raise BusinessException("Este técnico já está associado a outro time")

        if stadium_id is not None and not await self.stadium_repository.get_by_id(stadium_id):
            raise BusinessException("O estádio informado não existe")

        team = Team(
            team_name=team_name if team_name is not None else existing.team_name,
            state=state if state is not None else existing.state,
            creation=creation if creation is not None else existing.creation,
            manager_id=new_manager_id,
            stadium_id=new_stadium_id,
        )
        return await self.repository.update(team_id, team)

    async def delete_team(self, team_id: int) -> None:
        if not await self.repository.get_by_id(team_id):
            raise BusinessException("Time não encontrado")
        await self.repository.delete(team_id)