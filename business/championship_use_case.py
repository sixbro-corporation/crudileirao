from domain.entities.championship_entity import Championship
from domain.ports.championship_repository_port import ChampionshipRepositoryPort
from .dtos.championship_dto import ChampionshipCreateDTO, ChampionshipUpdateDTO


class ChampionshipUseCase:
    def __init__(self, repository: ChampionshipRepositoryPort):
        self.repository = repository

    async def get_all_championships(self) -> list[Championship]:
        return await self.repository.get_all()

    async def get_championship(self, championship_id: int) -> Championship:
        return await self.repository.get_by_id(championship_id)

    async def create_championship(self, dto: ChampionshipCreateDTO) -> Championship:
        existing = await self.repository.exists_by_name(dto.championship_name)
        if existing:
            raise ValueError("Já existe um campeonato com esse nome")

        championship = Championship(
            championship_name=dto.championship_name,
            title_type_id=dto.title_type_id,
            year=dto.year,
        )
        return await self.repository.create(championship)

    async def update_championship(self, championship_id: int, dto: ChampionshipUpdateDTO) -> Championship:
        existing = await self.repository.get_by_id(championship_id)
        if not existing:
            raise ValueError("Esse campeonato não existe")

        championship = Championship(
            championship_name=dto.championship_name if dto.championship_name is not None else existing.championship_name,
            title_type_id=dto.title_type_id if dto.title_type_id is not None else existing.title_type_id,
            year=dto.year if dto.year is not None else existing.year,
            id=championship_id,
        )
        return await self.repository.update(championship, championship_id)

    async def delete_championship(self, championship_id: int) -> None:
        existing = await self.repository.get_by_id(championship_id)
        if not existing:
            raise ValueError("Esse campeonato não existe")
        await self.repository.delete(championship_id)
