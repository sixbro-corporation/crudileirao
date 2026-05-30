import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.achievement_schema import AchievementSchema
from business.achievement_use_case import AchievementUseCase
from business.dtos.achievement_dto import CreateAchievementDTO, UpdateAchievementDTO
from persistence.configs.database import get_db_connection
from persistence.repositories.achievement_repository import AchievementRepository

router = APIRouter(prefix="/achievement", tags=["Achievement"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> AchievementUseCase:
    return AchievementUseCase(AchievementRepository(conn))


@router.get("/", response_model=list[AchievementSchema])
async def get_achievements(usecase: AchievementUseCase = Depends(get_use_case)):
    achievements = await usecase.get_all_achievements()
    return achievements


@router.post("/", response_model=AchievementSchema, status_code=201)
async def create_achievement(dto: CreateAchievementDTO, usecase: AchievementUseCase = Depends(get_use_case)):
    try:
        achievement = await usecase.create(dto)
        return achievement
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{achievement_id}", response_model=AchievementSchema)
async def get_achievement(achievement_id: int, usecase: AchievementUseCase = Depends(get_use_case)):
    try:
        achievement = await usecase.get_achievement(achievement_id)
        return achievement
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{achievement_id}", response_model=AchievementSchema)
async def update_achievement(achievement_id: int, dto: UpdateAchievementDTO, usecase: AchievementUseCase = Depends(get_use_case)):
    try:
        achievement = await usecase.update_achievement(achievement_id, dto)
        return achievement
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{achievement_id}", status_code=204)
async def delete_achievement(achievement_id: int, usecase: AchievementUseCase = Depends(get_use_case)):
    try:
        await usecase.delete(achievement_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
