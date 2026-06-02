import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
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


@router.get("/", response_model=ApiResponse[list[ChampionshipEditionSchema]])
async def get_editions(championship_id: int, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    data = await usecase.get_editions_by_championship(championship_id)
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[ChampionshipEditionSchema], status_code=201)
async def create_edition(championship_id: int, dto: CreateChampionshipEditionDTO, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    data = await usecase.create_edition(championship_id, dto)
    return ApiResponse.success_response(data=data)


@router.get("/{edition_id}", response_model=ApiResponse[ChampionshipEditionSchema])
async def get_edition(championship_id: int, edition_id: int, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    data = await usecase.get_edition(championship_id, edition_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{edition_id}", response_model=ApiResponse[ChampionshipEditionSchema])
async def update_edition(championship_id: int, edition_id: int, dto: UpdateChampionshipEditionDTO, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    data = await usecase.update_edition(championship_id, edition_id, dto)
    return ApiResponse.success_response(data=data)


@router.delete("/{edition_id}", status_code=204)
async def delete_edition(championship_id: int, edition_id: int, usecase: ChampionshipEditionUseCase = Depends(get_use_case)):
    await usecase.delete_edition(championship_id, edition_id)