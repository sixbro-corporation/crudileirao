import asyncpg
from domain.entities.title_type import TitleType
from domain.ports.title_type_repository_port import TitleTypeRepositoryPort


class TitleTypeRepository(TitleTypeRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[TitleType]:
        rows = await self.conn.fetch("SELECT * FROM tipo_titulo")
        return [TitleType(**dict(row)) for row in rows]

    async def get_by_id(self, title_type_id: int) -> TitleType | None:
        row = await self.conn.fetchrow("SELECT * FROM tipo_titulo WHERE id = $1", title_type_id)
        return TitleType(**dict(row)) if row else None

    async def create(self, title_type: TitleType) -> TitleType:
        row = await self.conn.fetchrow(
            "INSERT INTO tipo_titulo (descricao) VALUES ($1) RETURNING *",
            title_type.description
        )
        return TitleType(**dict(row))

    async def update(self, title_type_id: int, title_type: TitleType) -> TitleType | None:
        row = await self.conn.fetchrow(
            "UPDATE tipo_titulo SET descricao = $1 WHERE id = $2 RETURNING *",
            title_type.description, title_type_id
        )
        return TitleType(**dict(row)) if row else None

    async def delete(self, title_type_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM tipo_titulo WHERE id = $1", title_type_id)
        return result == "DELETE 1"