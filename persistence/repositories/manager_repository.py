import asyncpg
from domain.entities.tecnicos_entity import Manager
from domain.ports.manager_repository_port import ManagerRepositoryPort


class ManagerRepository(ManagerRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Manager]:
        rows = await self.conn.fetch("SELECT * FROM tecnicos")
        return [Manager(**dict(row)) for row in rows]

    async def get_by_id(self, manager_id: int) -> Manager | None:
        row = await self.conn.fetchrow("SELECT * FROM tecnicos WHERE id = $1", manager_id)
        return Manager(**dict(row)) if row else None

    async def create(self, manager: Manager) -> Manager:
        row = await self.conn.fetchrow(
            "INSERT INTO tecnicos (nome_tecnico, data_nascimento, nacionalidade) VALUES ($1, $2, $3) RETURNING *",
            manager.manager_name, manager.birth_date, manager.nacionality
        )
        return Manager(**dict(row))

    async def update(self, manager_id: int, manager: Manager) -> Manager | None:
        row = await self.conn.fetchrow(
            "UPDATE tecnicos SET nome_tecnico=$1, data_nascimento=$2, nacionalidade=$3 WHERE id=$4 RETURNING *",
            manager.manager_name, manager.birth_date, manager.nacionality, manager_id
        )
        return Manager(**dict(row)) if row else None

    async def delete(self, manager_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM tecnicos WHERE id = $1", manager_id)
        return result == "DELETE 1"

    async def exists_by_name(self, manager_name: str) -> bool:
        row = await self.conn.fetchrow(""""
        SELECT 1 FROM tecnicos WHERE nome_tecnico = $1""", manager_name)
        return row is not None