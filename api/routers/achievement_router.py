import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.achievement_schema import AchievementSchema
from business.achievement_use_case import AchievementUseCase
from business.dtos.achievement_dto import CreateAchievementDTO, UpdateAchievementDTO
from persistence.configs.database import get_db_connection
from persistence.repositories.achievement_repository import AchievementRepository

router = APIRouter(prefix="/achievement", tags=["Achievement"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> AchievementUseCase:
    return AchievementUseCase(AchievementRepository(conn))


@router.get("/", response_model=ApiResponse[list[AchievementSchema]])
async def get_achievements(usecase: AchievementUseCase = Depends(get_use_case)):
    data = await usecase.get_all_achievements()
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[AchievementSchema], status_code=201)
async def create_achievement(dto: CreateAchievementDTO, usecase: AchievementUseCase = Depends(get_use_case)):
    data = await usecase.create(dto)
    return ApiResponse.success_response(data=data)


@router.get("/{achievement_id}", response_model=ApiResponse[AchievementSchema])
async def get_achievement(achievement_id: int, usecase: AchievementUseCase = Depends(get_use_case)):
    data = await usecase.get_achievement(achievement_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{achievement_id}", response_model=ApiResponse[AchievementSchema])
async def update_achievement(achievement_id: int, dto: UpdateAchievementDTO, usecase: AchievementUseCase = Depends(get_use_case)):
    data = await usecase.update_achievement(achievement_id, dto)
    return ApiResponse.success_response(data=data)


@router.delete("/{achievement_id}", status_code=204)
async def delete_achievement(achievement_id: int, usecase: AchievementUseCase = Depends(get_use_case)):
    await usecase.delete(achievement_id)