from domain.entities.championship_entity import Championship
from domain.ports.championship_repository_port import ChampionshipRepositoryPort
import asyncpg

class ChampionshipRepository(ChampionshipRepositoryPort):
    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Championship]:
        rows = await self.conn.fetch("SELECT * FROM ")
        return [Championship(**dict(row)) for row in rows]

    async def get_by_id(self, championship_id: int) -> Championship:
        row = await self.conn.fetchrow("SELECT * FROM conquistas WHERE id = $1", championship_id)
        return Championship(**dict(row)) if row else None

    async def create(self, championship: Championship) -> Championship:
        row = await (self.conn.fetchrow
                     ("INSERT INTO conquistas(nome_campeonato, tipo_titulo_id, ano) VALUES ($1, $2, $3) RETURNING *",
                      championship.championship_name, championship.title_type_id, championship.year))
        return Championship(**dict(row)) if row else None

    async def update(self, championship: Championship, championship_id: int) -> Championship:
        row = await self.conn.fetchrow("""UPDATE conquistas SET nome_campeonato = $1, tipo_titulo_id = $2, ano = $3 WHERE id = $4 RETURNING *""",
            championship.championship_name, championship.title_type_id, championship.year)

        return Championship(**dict(row)) if row else None

    async def delete(self, championship_id: int) -> bool:
        result = await self.conn.execute("""
        DELETE FROM conquistas WHERE id = $1""", championship_id)
        return result == "DELETE 1"


