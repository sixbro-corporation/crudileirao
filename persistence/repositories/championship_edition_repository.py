import asyncpg
from domain.entities.championship_edition_entity import ChampionshipEdition
from domain.ports.championship_edition_repository_port import ChampionshipEditionRepositoryPort


class ChampionshipEditionRepository(ChampionshipEditionRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[ChampionshipEdition]:
        rows = await self.conn.fetch("SELECT * FROM edicoes_campeonato")
        return [ChampionshipEdition(**dict(row)) for row in rows]

    async def get_by_id(self, edition_id: int) -> ChampionshipEdition | None:
        row = await self.conn.fetchrow("SELECT * FROM edicoes_campeonato WHERE id = $1", edition_id)
        return ChampionshipEdition(**dict(row)) if row else None

    async def get_by_championship(self, championship_id: int) -> list[ChampionshipEdition]:
        rows = await self.conn.fetch(
            "SELECT * FROM edicoes_campeonato WHERE campeonato_id = $1 ORDER BY ano",
            championship_id
        )
        return [ChampionshipEdition(**dict(row)) for row in rows]

    async def create(self, edition: ChampionshipEdition) -> ChampionshipEdition:
        row = await self.conn.fetchrow(
            "INSERT INTO edicoes_campeonato (campeonato_id, ano) VALUES ($1, $2) RETURNING *",
            edition.championship_id, edition.year
        )
        return ChampionshipEdition(**dict(row))

    async def update(self, edition_id: int, edition: ChampionshipEdition) -> ChampionshipEdition | None:
        row = await self.conn.fetchrow(
            "UPDATE edicoes_campeonato SET campeonato_id = $1, ano = $2 WHERE id = $3 RETURNING *",
            edition.championship_id, edition.year, edition_id
        )
        return ChampionshipEdition(**dict(row)) if row else None

    async def delete(self, edition_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM edicoes_campeonato WHERE id = $1", edition_id)
        return result == "DELETE 1"