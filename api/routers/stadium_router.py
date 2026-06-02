import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.stadium_schema import StadiumSchema
from business.dtos.stadium_dto import CreateStadiumDTO, UpdateStadiumDTO
from business.stadium_use_case import StadiumUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.stadium_repository import StadiumRepository

router = APIRouter(prefix="/stadium", tags=["Stadium"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> StadiumUseCase:
    return StadiumUseCase(StadiumRepository(conn))


@router.get("/", response_model=ApiResponse[list[StadiumSchema]])
async def get_stadiums(usecase: StadiumUseCase = Depends(get_use_case)):
    data = await usecase.get_all_stadiums()
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[StadiumSchema], status_code=201)
async def create_stadium(dto: CreateStadiumDTO, usecase: StadiumUseCase = Depends(get_use_case)):
    data = await usecase.create_stadium(dto)
    return ApiResponse.success_response(data=data)


@router.get("/{stadium_id}", response_model=ApiResponse[StadiumSchema])
async def get_stadium(stadium_id: int, usecase: StadiumUseCase = Depends(get_use_case)):
    data = await usecase.get_stadium(stadium_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{stadium_id}", response_model=ApiResponse[StadiumSchema])
async def update_stadium(stadium_id: int, dto: UpdateStadiumDTO, usecase: StadiumUseCase = Depends(get_use_case)):
    data = await usecase.update_stadium(stadium_id, dto)
    return ApiResponse.success_response(data=data)


@router.delete("/{stadium_id}", status_code=204)
async def delete_stadium(stadium_id: int, usecase: StadiumUseCase = Depends(get_use_case)):
    await usecase.delete_stadium(stadium_id)