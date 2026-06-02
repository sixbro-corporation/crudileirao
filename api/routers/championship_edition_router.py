import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.championship_edition_schema import ChampionshipEditionSchema
from business.championship_edition_use_case import ChampionshipEditionUseCase
from business.dtos.championship_edition_dto import CreateChampionshipEditionDTO, UpdateChampionshipEditionDTO
from persistence.configs.database import get_db_connection
from persistence.repositories.championship_edition_repository import ChampionshipEditionRepository
from persistence.repositories.championship_repository import ChampionshipRepository

router = APIRouter(prefix="/championship/{championship_id}/edition", tags=["ChampionshipEdition"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> ChampionshipEditionUseCase:
    return ChampionshipEditionUseCase(
        ChampionshipEditionRepository(conn),
        ChampionshipRepository(conn),
    )


@router.get("/", response_model=list[ChampionshipEditionSchema])
async def get_editions(championship_id: int, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    try:
        return await usecase.get_editions_by_championship(championship_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=ChampionshipEditionSchema, status_code=201)
async def create_edition(championship_id: int, dto: CreateChampionshipEditionDTO, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    try:
        return await usecase.create_edition(championship_id, dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{edition_id}", response_model=ChampionshipEditionSchema)
async def get_edition(championship_id: int, edition_id: int, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    try:
        return await usecase.get_edition(championship_id, edition_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{edition_id}", response_model=ChampionshipEditionSchema)
async def update_edition(championship_id: int, edition_id: int, dto: UpdateChampionshipEditionDTO, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    try:
        return await usecase.update_edition(championship_id, edition_id, dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{edition_id}", status_code=204)
async def delete_edition(championship_id: int, edition_id: int, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    try:
        await usecase.delete_edition(championship_id, edition_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))