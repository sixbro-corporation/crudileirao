import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from api.schemas.team_schema import TeamSchema
from business.dtos.team_dto import CreateTeamDTO, UpdateTeamDTO
from business.team_use_case import TeamUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.team_repository import TeamRepository

router = APIRouter(prefix="/team", tags=["Team"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> TeamUseCase:
    return TeamUseCase(TeamRepository(conn))


@router.get("/", response_model=list[TeamSchema])
async def get_teams(usecase: TeamUseCase = Depends(get_use_case)):
    teams = await usecase.get_all_teams()
    return teams


@router.post("/", response_model=TeamSchema, status_code=201)
async def create_team(dto: CreateTeamDTO, usecase: TeamUseCase = Depends(get_use_case)):
    try:
        team = await usecase.create_team(dto)
        return team
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{team_id}", response_model=TeamSchema)
async def get_team(team_id: int, usecase: TeamUseCase = Depends(get_use_case)):
    try:
        team = await usecase.get_team(team_id)
        return team
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{team_id}", response_model=TeamSchema)
async def update_team(team_id: int, dto: UpdateTeamDTO, usecase: TeamUseCase = Depends(get_use_case)):
    try:
        team = await usecase.update_team(
            team_id=team_id,
            team_name=dto.team_name,
            state=dto.state,
            creation=dto.creation,
            manager_id=dto.manager_id,
            stadium_id=dto.estadio_id,
        )
        return team
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{team_id}", status_code=204)
async def delete_team(team_id: int, usecase: TeamUseCase = Depends(get_use_case)):
    try:
        await usecase.delete_team(team_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

