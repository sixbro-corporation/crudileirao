import asyncpg
from domain.entities.stadium_entity import Stadium
from domain.ports.stadium_repository_port import StadiumRepositoryPort


class StadiumRepository(StadiumRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Stadium]:
        rows = await self.conn.fetch("SELECT * FROM estadios")
        return [Stadium(**dict(row)) for row in rows]

    async def get_by_id(self, stadium_id: int) -> Stadium | None:
        row = await self.conn.fetchrow("SELECT * FROM estadios WHERE id = $1", stadium_id)
        return Stadium(**dict(row)) if row else None

    async def create(self, stadium: Stadium) -> Stadium:
        row = await self.conn.fetchrow(
            "INSERT INTO estadios (id, nome_estadio, cidade, capacidade) VALUES ($1, $2, $3, $4) RETURNING *",
            stadium.id, stadium.stadium_name, stadium.city, stadium.capacity
        )
        return Stadium(**dict(row))

    async def update(self, stadium_id: int, stadium: Stadium) -> Stadium | None:
        row = await self.conn.fetchrow(
            "UPDATE estadios SET nome_estadio=$1, cidade=$2, capacidade=$3 WHERE id=$4 RETURNING *",
            stadium.stadium_name, stadium.city, stadium.capacity, stadium_id
        )
        return Stadium(**dict(row)) if row else None

    async def delete(self, stadium_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM estadios WHERE id = $1", stadium_id)
        return result == "DELETE 1"