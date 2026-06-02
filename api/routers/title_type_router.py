import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.title_type_schema import TitleTypeSchema
from business.dtos.title_type_dto import CreateTitleTypeDTO, UpdateTitleTypeDTO
from business.title_type_use_case import TitleTypeUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.title_type_repository import TitleTypeRepository

router = APIRouter(prefix="/title-type", tags=["TitleType"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> TitleTypeUseCase:
    return TitleTypeUseCase(TitleTypeRepository(conn))


@router.get("/", response_model=list[TitleTypeSchema])
async def get_title_types(usecase: TitleTypeUseCase = Depends(get_use_case)):
    return await usecase.get_all_title_types()


@router.post("/", response_model=TitleTypeSchema, status_code=201)
async def create_title_type(dto: CreateTitleTypeDTO, usecase: TitleTypeUseCase = Depends(get_use_case)):
    try:
        return await usecase.create_title_type(dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{title_type_id}", response_model=TitleTypeSchema)
async def get_title_type(title_type_id: int, usecase: TitleTypeUseCase = Depends(get_use_case)):
    try:
        return await usecase.get_title_type(title_type_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{title_type_id}", response_model=TitleTypeSchema)
async def update_title_type(title_type_id: int, dto: UpdateTitleTypeDTO, usecase: TitleTypeUseCase = Depends(get_use_case)):
    try:
        return await usecase.update_title_type(title_type_id, dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{title_type_id}", status_code=204)
async def delete_title_type(title_type_id: int, usecase: TitleTypeUseCase = Depends(get_use_case)):
    try:
        await usecase.delete_title_type(title_type_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))