from contextlib import asynccontextmanager

import uvicorn
import logging
from fastapi import FastAPI

from api.commons.exception_handler import register_exception_handler
from api.routers.achievement_router import router as achievement_router
from api.routers.championship_router import router as championship_router
from api.routers.manager_router import router as manager_router
from api.routers.team_router import router as team_router
from api.routers.championship_edition_router import router as championship_edition_router
from api.routers.title_type_router import router as title_type_router
from api.routers.stadium_router import router as stadium_router
from api.routers.player_router import router as player_router
from persistence.configs.database import init_db, close_pool

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting API")
    await init_db()
    logger.info("Database initialized")

    yield

    logger.info("Shutting down API")
    await close_pool()
app = FastAPI(
    title="CRUDileirão API",
    lifespan=lifespan
)

app.include_router(team_router)
app.include_router(achievement_router)
app.include_router(championship_router)
app.include_router(manager_router)
app.include_router(player_router)
app.include_router(championship_edition_router)
app.include_router(stadium_router)
app.include_router(title_type_router)

register_exception_handler(app)

if __name__ == "__main__":
    uvicorn.run(
        "web.main:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
    )
