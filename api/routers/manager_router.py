import asyncpg
from fastapi import APIRouter, Depends

from api.commons.api_response import ApiResponse
from api.schemas.manager_schema import ManagerSchema
from business.dtos.manager_dto import ManagerInputDTO, ManagerUpdateDTO
from business.manager_use_case import ManagerUseCase
from persistence.configs.database import get_db_connection
from persistence.repositories.manager_repository import ManagerRepository

router = APIRouter(prefix="/manager", tags=["Manager"])


def get_use_case(conn: asyncpg.Connection = Depends(get_db_connection)) -> ManagerUseCase:
    return ManagerUseCase(ManagerRepository(conn))


@router.get("/", response_model=ApiResponse[list[ManagerSchema]])
async def get_managers(usecase: ManagerUseCase = Depends(get_use_case)):
    data = await usecase.get_all_managers()
    return ApiResponse.success_response(data=data)


@router.post("/", response_model=ApiResponse[ManagerSchema], status_code=201)
async def create_manager(dto: ManagerInputDTO, usecase: ManagerUseCase = Depends(get_use_case)):
    data = await usecase.create_manager(dto)
    return ApiResponse.success_response(data=data)


@router.get("/{manager_id}", response_model=ApiResponse[ManagerSchema])
async def get_manager(manager_id: int, usecase: ManagerUseCase = Depends(get_use_case)):
    data = await usecase.get_manager(manager_id)
    return ApiResponse.success_response(data=data)


@router.patch("/{manager_id}", response_model=ApiResponse[ManagerSchema])
async def update_manager(manager_id: int, dto: ManagerUpdateDTO, usecase: ManagerUseCase = Depends(get_use_case)):
    data = await usecase.update_manager(manager_id, dto)
    return ApiResponse.success_response(data=data)


@router.delete("/{manager_id}", status_code=204)
async def delete_manager(manager_id: int, usecase: ManagerUseCase = Depends(get_use_case)):
    await usecase.delete_manager(manager_id)