from domain.entities.team_entity import Team
from domain.ports.team_repository_port import TeamRepositoryPort
from .dtos.team_dto import CreateTeamDTO


class TeamUseCase:
    def __init__(self, team_repository: TeamRepositoryPort) -> None:
        self.repository = team_repository

    async def create_team(self, dto: CreateTeamDTO) -> Team:
        existing = await self.repository.exists_by_name(dto.team_name)
        if existing:
            raise ValueError(f"Já existe um time com o nome '{dto.team_name}'")

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
        return await self.repository.get_by_id(team_id)

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
            raise ValueError("Não existe nenhum time com esse id")

        team = Team(
            team_name=team_name if team_name is not None else existing.team_name,
            state=state if state is not None else existing.state,
            creation=creation if creation is not None else existing.creation,
            manager_id=manager_id if manager_id is not None else existing.manager_id,
            stadium_id=stadium_id if stadium_id is not None else existing.stadium_id,
        )

        return await self.repository.update(team_id, team)

    async def delete_team(self, team_id: int) -> None:
        existing = await self.repository.get_by_id(team_id)
        if not existing:
            raise ValueError("Não foi possível encontrar esse time")
        await self.repository.delete(team_id)
