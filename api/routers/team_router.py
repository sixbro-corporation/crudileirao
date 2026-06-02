import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.team_schema import TeamSchema
from business.dtos.team_dto import CreateTeamDTO, UpdateTeamDTO
from business.team_use_case import TeamUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.team_repository import TeamRepository

router = APIRouter(prefix="/team", tags=["Team"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> TeamUseCase:
    return TeamUseCase(TeamRepository(conn))


@router.get("/", response_model=ApiResponse[list[TeamSchema]])
async def get_teams(usecase: TeamUseCase = Depends(get_use_case)):
    data = await usecase.get_all_teams()
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[TeamSchema], status_code=201)
async def create_team(dto: CreateTeamDTO, usecase: TeamUseCase = Depends(get_use_case)):
    data = await usecase.create_team(dto)
    return ApiResponse.success_response(data=data)


@router.get("/{team_id}", response_model=ApiResponse[TeamSchema])
async def get_team(team_id: int, usecase: TeamUseCase = Depends(get_use_case)):
    data = await usecase.get_team(team_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{team_id}", response_model=ApiResponse[TeamSchema])
async def update_team(team_id: int, dto: UpdateTeamDTO, usecase: TeamUseCase = Depends(get_use_case)):
    data = await usecase.update_team(
        team_id=team_id,
        team_name=dto.team_name,
        state=dto.state,
        creation=dto.creation,
        manager_id=dto.manager_id,
        stadium_id=dto.estadio_id,
    )
    return ApiResponse.success_response(data=data)


@router.delete("/{team_id}", status_code=204)
async def delete_team(team_id: int, usecase: TeamUseCase = Depends(get_use_case)):
    await usecase.delete_team(team_id)