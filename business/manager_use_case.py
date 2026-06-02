from domain.entities.tecnicos_entity import Manager
from domain.exceptions.business_exception import BusinessException
from domain.ports.manager_repository_port import ManagerRepositoryPort
from .dtos.manager_dto import ManagerInputDTO, ManagerUpdateDTO


class ManagerUseCase:
    def __init__(self, repository: ManagerRepositoryPort):
        self.repository = repository

    async def get_manager(self, manager_id: int) -> Manager:
        existing = await self.repository.get_by_id(manager_id)
        if not existing:
            raise BusinessException("Técnico não encontrado")
        return existing

    async def get_all_managers(self) -> list[Manager]:
        return await self.repository.get_all()

    async def create_manager(self, manager: ManagerInputDTO) -> Manager:
        if await self.repository.exists_by_name(manager.manager_name):
            raise BusinessException("Já existe um técnico com esse nome")

        manager_entity = Manager(
            manager_name=manager.manager_name,
            birth_date=manager.birth_date,
            nacionality=manager.nacionality,
        )
        return await self.repository.create(manager_entity)

    async def update_manager(self, manager_id: int, manager: ManagerUpdateDTO) -> Manager:
        existing = await self.repository.get_by_id(manager_id)
        if not existing:
            raise BusinessException("Técnico não encontrado")

        manager_entity = Manager(
            manager_name=manager.manager_name if manager.manager_name is not None else existing.manager_name,
            birth_date=manager.birth_date if manager.birth_date is not None else existing.birth_date,
            nacionality=manager.nacionality if manager.nacionality is not None else existing.nacionality,
            id=manager_id,
        )
        return await self.repository.update(manager_id, manager_entity)

    async def delete_manager(self, manager_id: int) -> None:
        if not await self.repository.get_by_id(manager_id):
            raise BusinessException("Técnico não encontrado")
        await self.repository.delete(manager_id)