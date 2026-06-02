import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.title_type_schema import TitleTypeSchema
from business.dtos.title_type_dto import CreateTitleTypeDTO, UpdateTitleTypeDTO
from business.title_type_use_case import TitleTypeUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.title_type_repository import TitleTypeRepository

router = APIRouter(prefix="/title-type", tags=["TitleType"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> TitleTypeUseCase:
    return TitleTypeUseCase(TitleTypeRepository(conn))


@router.get("/", response_model=ApiResponse[list[TitleTypeSchema]])
async def get_title_types(usecase: TitleTypeUseCase = Depends(get_use_case)):
    data = await usecase.get_all_title_types()
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[TitleTypeSchema], status_code=201)
async def create_title_type(dto: CreateTitleTypeDTO, usecase: TitleTypeUseCase = Depends(get_use_case)):
    data = await usecase.create_title_type(dto)
    return ApiResponse.success_response(data=data)


@router.get("/{title_type_id}", response_model=ApiResponse[TitleTypeSchema])
async def get_title_type(title_type_id: int, usecase: TitleTypeUseCase = Depends(get_use_case)):
    data = await usecase.get_title_type(title_type_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{title_type_id}", response_model=ApiResponse[TitleTypeSchema])
async def update_title_type(title_type_id: int, dto: UpdateTitleTypeDTO, usecase: TitleTypeUseCase = Depends(get_use_case)):
    data = await usecase.update_title_type(title_type_id, dto)
    return ApiResponse.success_response(data=data)


@router.delete("/{title_type_id}", status_code=204)
async def delete_title_type(title_type_id: int, usecase: TitleTypeUseCase = Depends(get_use_case)):
    await usecase.delete_title_type(title_type_id)