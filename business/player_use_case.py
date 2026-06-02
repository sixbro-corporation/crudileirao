from domain.entities.player_entity import Player
from domain.ports.player_repository_port import PlayerRepositoryPort
from .dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO


class PlayerUseCase:
    def __init__(self, repository: PlayerRepositoryPort) -> None:
        self.repository = repository

    async def get_all_players(self) -> list[Player]:
        return await self.repository.get_all()

    async def get_player(self, player_id: int) -> Player:
        existing = await self.repository.get_by_id(player_id)
        if not existing:
            raise ValueError("Jogador não encontrado")
        return existing

    async def create_player(self, dto: CreatePlayerDTO) -> Player:
        shirt_taken = await self.repository.exists_by_shirt_number_and_team(dto.shirt_number, dto.team_id)
        if shirt_taken:
            raise ValueError(f"O número {dto.shirt_number} já está em uso nesse time")

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
            raise ValueError("Jogador não encontrado")

        new_shirt = dto.shirt_number if dto.shirt_number is not None else existing.shirt_number
        new_team = dto.team_id if dto.team_id is not None else existing.team_id

        shirt_changed = new_shirt != existing.shirt_number or new_team != existing.team_id
        if shirt_changed:
            shirt_taken = await self.repository.exists_by_shirt_number_and_team(new_shirt, new_team)
            if shirt_taken:
                raise ValueError(f"O número {new_shirt} já está em uso nesse time")

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
        existing = await self.repository.get_by_id(player_id)
        if not existing:
            raise ValueError("Jogador não encontrado")
        await self.repository.delete(player_id)