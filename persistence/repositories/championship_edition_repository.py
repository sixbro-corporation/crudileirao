import asyncpg
from domain.entities.championship_edition_entity import ChampionshipEdition
from domain.ports.championship_edition_repository_port import ChampionshipEditionRepositoryPort


def _map(row) -> ChampionshipEdition:
    return ChampionshipEdition(
        id=row["id"],
        championship_id=row["campeonato_id"],
        year=row["ano"],
    )


class ChampionshipEditionRepository(ChampionshipEditionRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[ChampionshipEdition]:
        rows = await self.conn.fetch("SELECT * FROM edicoes_campeonato")
        return [_map(row) for row in rows]

    async def get_by_id(self, edition_id: int) -> ChampionshipEdition | None:
        row = await self.conn.fetchrow("SELECT * FROM edicoes_campeonato WHERE id = $1", edition_id)
        return _map(row) if row else None

    async def get_by_championship(self, championship_id: int) -> list[ChampionshipEdition]:
        rows = await self.conn.fetch(
            "SELECT * FROM edicoes_campeonato WHERE campeonato_id = $1 ORDER BY ano",
            championship_id
        )
        return [_map(row) for row in rows]

    async def create(self, edition: ChampionshipEdition) -> ChampionshipEdition:
        row = await self.conn.fetchrow(
            "INSERT INTO edicoes_campeonato (campeonato_id, ano) VALUES ($1, $2) RETURNING *",
            edition.championship_id, edition.year
        )
        return _map(row)

    async def update(self, edition_id: int, edition: ChampionshipEdition) -> ChampionshipEdition | None:
        row = await self.conn.fetchrow(
            "UPDATE edicoes_campeonato SET campeonato_id=$1, ano=$2 WHERE id=$3 RETURNING *",
            edition.championship_id, edition.year, edition_id
        )
        return _map(row) if row else None

    async def delete(self, edition_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM edicoes_campeonato WHERE id = $1", edition_id)
        return result == "DELETE 1"

    async def exists_by_championship_and_year(self, championship_id: int, year: int) -> bool:
        row = await self.conn.fetchrow(
            "SELECT 1 FROM edicoes_campeonato WHERE campeonato_id = $1 AND ano = $2",
            championship_id, year
        )
        return row is not None