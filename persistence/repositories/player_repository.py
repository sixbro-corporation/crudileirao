import asyncpg
from domain.entities.player_entity import Player
from domain.ports.player_repository_port import PlayerRepositoryPort


class PlayerRepository(PlayerRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Player]:
        rows = await self.conn.fetch("SELECT * FROM jogadores")
        return [Player(**dict(row)) for row in rows]

    async def get_by_id(self, player_id: int) -> Player | None:
        row = await self.conn.fetchrow("SELECT * FROM jogadores WHERE id = $1", player_id)
        return Player(**dict(row)) if row else None

    async def create(self, player: Player) -> Player:
        row = await self.conn.fetchrow(
            "INSERT INTO jogadores (nome_jogador, data_nascimento, posicao, numero_camisa, time_id) VALUES ($1, $2, $3, $4, $5) RETURNING *",
            player.player_name, player.birth_date, player.posicao, player.shirt_number, player.team_id
        )
        return Player(**dict(row))

    async def update(self, player_id: int, player: Player) -> Player | None:
        row = await self.conn.fetchrow(
            "UPDATE jogadores SET nome_jogador=$1, data_nascimento=$2, posicao=$3, numero_camisa=$4, time_id=$5 WHERE id=$6 RETURNING *",
            player.player_name, player.birth_date, player.posicao, player.shirt_number, player.team_id, player_id
        )
        return Player(**dict(row)) if row else None

    async def delete(self, player_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM jogadores WHERE id = $1", player_id)
        return result == "DELETE 1"

    async def exists_by_shirt_number_and_team(self, shirt_number: int, team_id: int) -> bool:
        row = await self.conn.fetchrow(
            "SELECT 1 FROM jogadores WHERE numero_camisa = $1 AND time_id = $2",
            shirt_number, team_id
        )
        return row is not None