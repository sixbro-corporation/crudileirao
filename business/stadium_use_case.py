from domain.entities.stadium_entity import Stadium
from domain.ports.stadium_repository_port import StadiumRepositoryPort
from .dtos.stadium_dto import CreateStadiumDTO, UpdateStadiumDTO


class StadiumUseCase:
    def __init__(self, repository: StadiumRepositoryPort) -> None:
        self.repository = repository

    async def get_all_stadiums(self) -> list[Stadium]:
        return await self.repository.get_all()

    async def get_stadium(self, stadium_id: int) -> Stadium:
        existing = await self.repository.get_by_id(stadium_id)
        if not existing:
            raise ValueError("Estádio não encontrado")
        return existing

    async def create_stadium(self, dto: CreateStadiumDTO) -> Stadium:
        stadium = Stadium(
            stadium_name=dto.stadium_name,
            city=dto.city,
            capacity=dto.capacity,
        )
        return await self.repository.create(stadium)

    async def update_stadium(self, stadium_id: int, dto: UpdateStadiumDTO) -> Stadium:
        existing = await self.repository.get_by_id(stadium_id)
        if not existing:
            raise ValueError("Estádio não encontrado")

        stadium = Stadium(
            stadium_name=dto.stadium_name if dto.stadium_name is not None else existing.stadium_name,
            city=dto.city if dto.city is not None else existing.city,
            capacity=dto.capacity if dto.capacity is not None else existing.capacity,
            id=stadium_id,
        )
        return await self.repository.update(stadium_id, stadium)

    async def delete_stadium(self, stadium_id: int) -> None:
        existing = await self.repository.get_by_id(stadium_id)
        if not existing:
            raise ValueError("Estádio não encontrado")
        await self.repository.delete(stadium_id)