from domain.entities.championship_entity import Championship
from domain.exceptions.business_exception import BusinessException
from domain.ports.championship_repository_port import ChampionshipRepositoryPort
from domain.ports.title_type_repository_port import TitleTypeRepositoryPort
from .dtos.championship_dto import ChampionshipCreateDTO, ChampionshipUpdateDTO


class ChampionshipUseCase:
    def __init__(
        self,
        repository: ChampionshipRepositoryPort,
        title_type_repository: TitleTypeRepositoryPort,
    ) -> None:
        self.repository = repository
        self.title_type_repository = title_type_repository

    async def get_all_championships(self) -> list[Championship]:
        return await self.repository.get_all()

    async def get_championship(self, championship_id: int) -> Championship:
        existing = await self.repository.get_by_id(championship_id)
        if not existing:
            raise BusinessException("Campeonato não encontrado")
        return existing

    async def create_championship(self, dto: ChampionshipCreateDTO) -> Championship:
        if await self.repository.exists_by_name(dto.championship_name):
            raise BusinessException("Já existe um campeonato com esse nome")

        if not await self.title_type_repository.get_by_id(dto.title_type_id):
            raise BusinessException("O tipo de título informado não existe")

        championship = Championship(
            championship_name=dto.championship_name,
            title_type_id=dto.title_type_id,
            id=None,
        )
        return await self.repository.create(championship)

    async def update_championship(self, championship_id: int, dto: ChampionshipUpdateDTO) -> Championship:
        existing = await self.repository.get_by_id(championship_id)
        if not existing:
            raise BusinessException("Campeonato não encontrado")

        if dto.title_type_id is not None and not await self.title_type_repository.get_by_id(dto.title_type_id):
            raise BusinessException("O tipo de título informado não existe")

        championship = Championship(
            championship_name=dto.championship_name if dto.championship_name is not None else existing.championship_name,
            title_type_id=dto.title_type_id if dto.title_type_id is not None else existing.title_type_id,
            id=championship_id,
        )
        return await self.repository.update(championship_id, championship)

    async def delete_championship(self, championship_id: int) -> None:
        if not await self.repository.get_by_id(championship_id):
            raise BusinessException("Campeonato não encontrado")
        await self.repository.delete(championship_id)