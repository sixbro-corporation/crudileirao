from domain.entities.title_type import TitleType
from domain.ports.title_type_repository_port import TitleTypeRepositoryPort
from .dtos.title_type_dto import CreateTitleTypeDTO, UpdateTitleTypeDTO


class TitleTypeUseCase:
    def __init__(self, repository: TitleTypeRepositoryPort) -> None:
        self.repository = repository

    async def get_all_title_types(self) -> list[TitleType]:
        return await self.repository.get_all()

    async def get_title_type(self, title_type_id: int) -> TitleType:
        existing = await self.repository.get_by_id(title_type_id)
        if not existing:
            raise ValueError("Tipo de título não encontrado")
        return existing

    async def create_title_type(self, dto: CreateTitleTypeDTO) -> TitleType:
        title_type = TitleType(description=dto.description)
        return await self.repository.create(title_type)

    async def update_title_type(self, title_type_id: int, dto: UpdateTitleTypeDTO) -> TitleType:
        existing = await self.repository.get_by_id(title_type_id)
        if not existing:
            raise ValueError("Tipo de título não encontrado")

        title_type = TitleType(
            description=dto.description if dto.description is not None else existing.description,
            id=title_type_id,
        )
        return await self.repository.update(title_type_id, title_type)

    async def delete_title_type(self, title_type_id: int) -> None:
        existing = await self.repository.get_by_id(title_type_id)
        if not existing:
            raise ValueError("Tipo de título não encontrado")
        await self.repository.delete(title_type_id)