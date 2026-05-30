from fastapi import FastAPI

from api.routers.achievement_router import router as achievement_router
from api.routers.championship_router import router as championship_router
from api.routers.manager_router import router as manager_router
from api.routers.team_router import router as team_router

app = FastAPI()

app.include_router(team_router)
app.include_router(achievement_router)
app.include_router(championship_router)
app.include_router(manager_router)
