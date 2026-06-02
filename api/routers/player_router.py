import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.player_schema import PlayerSchema
from business.dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO
from business.player_use_case import PlayerUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.player_repository import PlayerRepository
from persistence.repositories.team_repository import TeamRepository

router = APIRouter(prefix="/player", tags=["Player"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> PlayerUseCase:
    return PlayerUseCase(
        repository=PlayerRepository(conn),
        team_repository=TeamRepository(conn),
    )


@router.get("/", response_model=ApiResponse[list[PlayerSchema]])
async def get_players(usecase: PlayerUseCase = Depends(get_use_case)):
    data = await usecase.get_all_players()
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[PlayerSchema], status_code=201)
async def create_player(dto: CreatePlayerDTO, usecase: PlayerUseCase = Depends(get_use_case)):
    data = await usecase.create_player(dto)
    return ApiResponse.success_response(data=data)


@router.get("/{player_id}", response_model=ApiResponse[PlayerSchema])
async def get_player(player_id: int, usecase: PlayerUseCase = Depends(get_use_case)):
    data = await usecase.get_player(player_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{player_id}", response_model=ApiResponse[PlayerSchema])
async def update_player(player_id: int, dto: UpdatePlayerDTO, usecase: PlayerUseCase = Depends(get_use_case)):
    data = await usecase.update_player(player_id, dto)
    return ApiResponse.success_response(data=data)


@router.delete("/{player_id}", status_code=204)
async def delete_player(player_id: int, usecase: PlayerUseCase = Depends(get_use_case)):
    await usecase.delete_player(player_id)