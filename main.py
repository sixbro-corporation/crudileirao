from fastapi import FastAPI

from api.routers.achievement_router import router as achievement_router
from api.routers.championship_router import router as championship_router
from api.routers.manager_router import router as manager_router
from api.routers.team_router import router as team_router
from api.routers.player_router import router as player_router
from api.routers.stadium_router import router as stadium_router
from api.routers.title_type_router import router as title_type_router
from api.routers.championship_edition_router import router as championship_edition_router

app = FastAPI()

app.include_router(team_router)
app.include_router(achievement_router)
app.include_router(championship_router)
app.include_router(manager_router)
app.include_router(player_router)
app.include_router(stadium_router)
app.include_router(title_type_router)
app.include_router(championship_edition_router)