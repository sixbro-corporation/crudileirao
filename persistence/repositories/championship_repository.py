import asyncpg
from domain.entities.championship_entity import Championship
from domain.ports.championship_repository_port import ChampionshipRepositoryPort


def _map(row) -> Championship:
    return Championship(
        id=row["id"],
        championship_name=row["nome_campeonato"],
        title_type_id=row["tipo_titulo_id"],
    )


class ChampionshipRepository(ChampionshipRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Championship]:
        rows = await self.conn.fetch("SELECT * FROM campeonatos")
        return [_map(row) for row in rows]

    async def get_by_id(self, championship_id: int) -> Championship | None:
        row = await self.conn.fetchrow("SELECT * FROM campeonatos WHERE id = $1", championship_id)
        return _map(row) if row else None

    async def create(self, championship: Championship) -> Championship:
        row = await self.conn.fetchrow(
            "INSERT INTO campeonatos (nome_campeonato, tipo_titulo_id) VALUES ($1, $2) RETURNING *",
            championship.championship_name, championship.title_type_id
        )
        return _map(row)

    async def update(self, championship_id: int, championship: Championship) -> Championship | None:
        row = await self.conn.fetchrow(
            "UPDATE campeonatos SET nome_campeonato=$1, tipo_titulo_id=$2 WHERE id=$3 RETURNING *",
            championship.championship_name, championship.title_type_id, championship_id
        )
        return _map(row) if row else None

    async def delete(self, championship_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM campeonatos WHERE id = $1", championship_id)
        return result == "DELETE 1"

    async def exists_by_name(self, championship_name: str) -> bool:
        row = await self.conn.fetchrow(
            "SELECT 1 FROM campeonatos WHERE nome_campeonato = $1", championship_name
        )
        return row is not None