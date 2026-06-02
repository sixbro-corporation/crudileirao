import asyncpg
from domain.entities.team_entity import Team
from domain.ports.team_repository_port import TeamRepositoryPort


def _map(row) -> Team:
    return Team(
        id=row["id"],
        team_name=row["nome_time"],
        state=row["estado"],
        creation=row["fundacao"],
        manager_id=row["tecnico_id"],
        stadium_id=row["estadio_id"],
    )


class TeamRepository(TeamRepositoryPort):

    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Team]:
        rows = await self.conn.fetch("SELECT * FROM times")
        return [_map(row) for row in rows]

    async def get_by_id(self, team_id: int) -> Team | None:
        row = await self.conn.fetchrow("SELECT * FROM times WHERE id = $1", team_id)
        return _map(row) if row else None

    async def create(self, team: Team) -> Team:
        row = await self.conn.fetchrow(
            "INSERT INTO times (nome_time, estado, fundacao, tecnico_id, estadio_id) VALUES ($1, $2, $3, $4, $5) RETURNING *",
            team.team_name, team.state, team.creation, team.manager_id, team.stadium_id
        )
        return _map(row)

    async def update(self, team_id: int, team: Team) -> Team | None:
        row = await self.conn.fetchrow(
            "UPDATE times SET nome_time=$1, estado=$2, fundacao=$3, tecnico_id=$4, estadio_id=$5 WHERE id=$6 RETURNING *",
            team.team_name, team.state, team.creation, team.manager_id, team.stadium_id, team_id
        )
        return _map(row) if row else None

    async def delete(self, team_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM times WHERE id = $1", team_id)
        return result == "DELETE 1"

    async def exists_by_name(self, team_name: str) -> bool:
        row = await self.conn.fetchrow(
            "SELECT 1 FROM times WHERE nome_time = $1", team_name
        )
        return row is not None