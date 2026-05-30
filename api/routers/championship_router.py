import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.championship_schema import ChampionshipSchema
from business.championship_use_case import ChampionshipUseCase
from business.dtos.championship_dto import ChampionshipCreateDTO, ChampionshipUpdateDTO
from persistence.configs.database import get_db_connection
from persistence.repositories.championship_repository import ChampionshipRepository

router = APIRouter(prefix="/championship", tags=["Championship"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> ChampionshipUseCase:
    return ChampionshipUseCase(ChampionshipRepository(conn))


@router.get("/", response_model=list[ChampionshipSchema])
async def get_championships(usecase: ChampionshipUseCase = Depends(get_use_case)):
    championships = await usecase.get_all_championships()
    return championships


@router.post("/", response_model=ChampionshipSchema, status_code=201)
async def create_championship(dto: ChampionshipCreateDTO, usecase: ChampionshipUseCase = Depends(get_use_case)):
    try:
        championship = await usecase.create_championship(dto)
        return championship
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{championship_id}", response_model=ChampionshipSchema)
async def get_championship(championship_id: int, usecase: ChampionshipUseCase = Depends(get_use_case)):
    try:
        championship = await usecase.get_championship(championship_id)
        return championship
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{championship_id}", response_model=ChampionshipSchema)
async def update_championship(championship_id: int, dto: ChampionshipUpdateDTO, usecase: ChampionshipUseCase = Depends(get_use_case)):
    try:
        championship = await usecase.update_championship(championship_id, dto)
        return championship
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{championship_id}", status_code=204)
async def delete_championship(championship_id: int, usecase: ChampionshipUseCase = Depends(get_use_case)):
    try:
        await usecase.delete_championship(championship_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
