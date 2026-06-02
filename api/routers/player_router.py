import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.player_schema import PlayerSchema
from business.dtos.player_dto import CreatePlayerDTO, UpdatePlayerDTO
from business.player_use_case import PlayerUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.player_repository import PlayerRepository

router = APIRouter(prefix="/player", tags=["Player"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> PlayerUseCase:
    return PlayerUseCase(PlayerRepository(conn))


@router.get("/", response_model=list[PlayerSchema])
async def get_players(usecase: PlayerUseCase = Depends(get_use_case)):
    return await usecase.get_all_players()


@router.post("/", response_model=PlayerSchema, status_code=201)
async def create_player(dto: CreatePlayerDTO, usecase: PlayerUseCase = Depends(get_use_case)):
    try:
        return await usecase.create_player(dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{player_id}", response_model=PlayerSchema)
async def get_player(player_id: int, usecase: PlayerUseCase = Depends(get_use_case)):
    try:
        return await usecase.get_player(player_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{player_id}", response_model=PlayerSchema)
async def update_player(player_id: int, dto: UpdatePlayerDTO, usecase: PlayerUseCase = Depends(get_use_case)):
    try:
        return await usecase.update_player(player_id, dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{player_id}", status_code=204)
async def delete_player(player_id: int, usecase: PlayerUseCase = Depends(get_use_case)):
    try:
        await usecase.delete_player(player_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))