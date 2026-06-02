from domain.entities.player_entity import Player
from domain.exceptions.business_exception import BusinessException
from domain.ports.player_repository_port import PlayerRepositoryPort
from domain.ports.team_repository_port import TeamRepositoryPort
from .dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO


class PlayerUseCase:
    def __init__(
        self,
        repository: PlayerRepositoryPort,
        team_repository: TeamRepositoryPort,
    ) -> None:
        self.repository = repository
        self.team_repository = team_repository

    async def get_all_players(self) -> list[Player]:
        return await self.repository.get_all()

    async def get_player(self, player_id: int) -> Player:
        existing = await self.repository.get_by_id(player_id)
        if not existing:
            raise BusinessException("Jogador não encontrado")
        return existing

    async def create_player(self, dto: CreatePlayerDTO) -> Player:
        if not await self.team_repository.get_by_id(dto.team_id):
            raise BusinessException("O time informado não existe")

        if await self.repository.exists_by_shirt_number_and_team(dto.shirt_number, dto.team_id):
            raise BusinessException(f"O número {dto.shirt_number} já está em uso nesse time")

        player = Player(
            player_name=dto.player_name,
            birth_date=dto.birth_date,
            posicao=dto.posicao,
            shirt_number=dto.shirt_number,
            team_id=dto.team_id,
        )
        return await self.repository.create(player)

    async def update_player(self, player_id: int, dto: UpdatePlayerDTO) -> Player:
        existing = await self.repository.get_by_id(player_id)
        if not existing:
            raise BusinessException("Jogador não encontrado")

        new_shirt = dto.shirt_number if dto.shirt_number is not None else existing.shirt_number
        new_team = dto.team_id if dto.team_id is not None else existing.team_id

        if dto.team_id is not None and not await self.team_repository.get_by_id(dto.team_id):
            raise BusinessException("O time informado não existe")

        if new_shirt != existing.shirt_number or new_team != existing.team_id:
            if await self.repository.exists_by_shirt_number_and_team(new_shirt, new_team):
                raise BusinessException(f"O número {new_shirt} já está em uso nesse time")

        player = Player(
            player_name=dto.player_name if dto.player_name is not None else existing.player_name,
            birth_date=dto.birth_date if dto.birth_date is not None else existing.birth_date,
            posicao=dto.posicao if dto.posicao is not None else existing.posicao,
            shirt_number=new_shirt,
            team_id=new_team,
            id=player_id,
        )
        return await self.repository.update(player_id, player)

    async def delete_player(self, player_id: int) -> None:
        if not await self.repository.get_by_id(player_id):
            raise BusinessException("Jogador não encontrado")
        await self.repository.delete(player_id)