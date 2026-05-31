from domain.entities.achievement_entity import Achievement
from domain.ports.achievement_repository_port import AchievementRepositoryPort
import asyncpg

class AchievementRepository(AchievementRepositoryPort):
    def __init__(self, conn: asyncpg.Connection) -> None:
        self.conn = conn

    async def get_all(self) -> list[Achievement]:
        rows = await self.conn.fetch("SELECT * FROM conquistas")
        return [Achievement(**dict(row)) for row in rows]

    async def get_by_id(self, achievement_id: int) -> Achievement | None:
        row = await self.conn.fetchrow("SELECT * FROM conquistas WHERE id = $1", achievement_id)
        return Achievement(**dict(row)) if row else None

    async def create(self, achievement: Achievement) -> Achievement:
        row = await self.conn.fetchrow(
            "INSERT INTO conquistas (time_id, edicao_id) VALUES ($1, $2) RETURNING *",
            achievement.team_id, achievement.edition_id
        )
        return Achievement(**dict(row))

    async def update(self, achievement_id: int, achievement: Achievement) -> Achievement | None:
        row = await self.conn.fetchrow(
            "UPDATE conquistas SET time_id = $1, edicao_id = $2 WHERE id = $3 RETURNING *",
            achievement.team_id, achievement.edition_id, achievement_id
        )
        return Achievement(**dict(row)) if row else None

    async def delete(self, achievement_id: int) -> bool:
        result = await self.conn.execute("DELETE FROM conquistas WHERE id = $1", achievement_id)
        return result == "DELETE 1"