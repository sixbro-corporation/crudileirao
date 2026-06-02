from domain.entities.championship_edition_entity import ChampionshipEdition
from domain.exceptions.business_exception import BusinessException
from domain.ports.championship_edition_repository_port import ChampionshipEditionRepositoryPort
from domain.ports.championship_repository_port import ChampionshipRepositoryPort
from .dtos.championship_edition_dto import CreateChampionshipEditionDTO, UpdateChampionshipEditionDTO


class ChampionshipEditionUseCase:
    def __init__(
        self,
        edition_repository: ChampionshipEditionRepositoryPort,
        championship_repository: ChampionshipRepositoryPort,
    ) -> None:
        self.edition_repository = edition_repository
        self.championship_repository = championship_repository

    async def get_editions_by_championship(self, championship_id: int) -> list[ChampionshipEdition]:
        if not await self.championship_repository.get_by_id(championship_id):
            raise BusinessException("Campeonato não encontrado")
        return await self.edition_repository.get_by_championship(championship_id)

    async def get_edition(self, championship_id: int, edition_id: int) -> ChampionshipEdition:
        if not await self.championship_repository.get_by_id(championship_id):
            raise BusinessException("Campeonato não encontrado")
        existing = await self.edition_repository.get_by_id(edition_id)
        if not existing or existing.championship_id != championship_id:
            raise BusinessException("Edição não encontrada")
        return existing

    async def create_edition(self, championship_id: int, dto: CreateChampionshipEditionDTO) -> ChampionshipEdition:
        if not await self.championship_repository.get_by_id(championship_id):
            raise BusinessException("Campeonato não encontrado")

        if await self.edition_repository.exists_by_championship_and_year(championship_id, dto.year):
            raise BusinessException(f"Já existe uma edição de {dto.year} para esse campeonato")

        edition = ChampionshipEdition(championship_id=championship_id, year=dto.year, id=None)
        return await self.edition_repository.create(edition)

    async def update_edition(self, championship_id: int, edition_id: int, dto: UpdateChampionshipEditionDTO) -> ChampionshipEdition:
        if not await self.championship_repository.get_by_id(championship_id):
            raise BusinessException("Campeonato não encontrado")

        existing = await self.edition_repository.get_by_id(edition_id)
        if not existing or existing.championship_id != championship_id:
            raise BusinessException("Edição não encontrada")

        new_year = dto.year if dto.year is not None else existing.year
        if new_year != existing.year:
            if await self.edition_repository.exists_by_championship_and_year(championship_id, new_year):
                raise BusinessException(f"Já existe uma edição de {new_year} para esse campeonato")

        edition = ChampionshipEdition(championship_id=championship_id, year=new_year, id=edition_id)
        return await self.edition_repository.update(edition_id, edition)

    async def delete_edition(self, championship_id: int, edition_id: int) -> None:
        if not await self.championship_repository.get_by_id(championship_id):
            raise BusinessException("Campeonato não encontrado")

        existing = await self.edition_repository.get_by_id(edition_id)
        if not existing or existing.championship_id != championship_id:
            raise BusinessException("Edição não encontrada")

        await self.edition_repository.delete(edition_id)