from domain.entities.championship_entity import Championship
from domain.ports.championship_repository_port import ChampionshipRepositoryPort
import asyncpg

class ChampionshipRepository(ChampionshipRepositoryPort):
    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Championship]:
        rows = await self.conn.fetch("SELECT * FROM campeonatos")
        return [Championship(**dict(row)) for row in rows]

    async def get_by_id(self, championship_id: int) -> Championship | None:
        row = await self.conn.fetchrow("SELECT * FROM campeonatos WHERE id = $1", championship_id)
        return Championship(**dict(row)) if row else None

    async def create(self, championship: Championship) -> Championship:
        row = await self.conn.fetchrow(
            "INSERT INTO campeonatos (nome_campeonato, tipo_titulo_id) VALUES ($1, $2) RETURNING *",
            championship.championship_name, championship.title_type_id
        )
        return Championship(**dict(row))

    async def update(self, championship_id: int, championship: Championship) -> Championship | None:
        row = await self.conn.fetchrow(
            "UPDATE campeonatos SET nome_campeonato = $1, tipo_titulo_id = $2 WHERE id = $3 RETURNING *",
            championship.championship_name, championship.title_type_id, championship_id
        )
        return Championship(**dict(row)) if row else None

    async def delete(self, championship_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM campeonatos WHERE id = $1", championship_id)
        return result == "DELETE 1"