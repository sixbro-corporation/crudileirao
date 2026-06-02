from domain.entities.championship_edition_entity import ChampionshipEdition
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
        championship = await self.championship_repository.get_by_id(championship_id)
        if not championship:
            raise ValueError("Campeonato não encontrado")
        return await self.edition_repository.get_by_championship(championship_id)

    async def get_edition(self, championship_id: int, edition_id: int) -> ChampionshipEdition:
        championship = await self.championship_repository.get_by_id(championship_id)
        if not championship:
            raise ValueError("Campeonato não encontrado")
        existing = await self.edition_repository.get_by_id(edition_id)
        if not existing or existing.championship_id != championship_id:
            raise ValueError("Edição não encontrada")
        return existing

    async def create_edition(self, championship_id: int, dto: CreateChampionshipEditionDTO) -> ChampionshipEdition:
        championship = await self.championship_repository.get_by_id(championship_id)
        if not championship:
            raise ValueError("Campeonato não encontrado")

        already_exists = await self.edition_repository.exists_by_championship_and_year(championship_id, dto.year)
        if already_exists:
            raise ValueError(f"Já existe uma edição de {dto.year} para esse campeonato")

        edition = ChampionshipEdition(championship_id=championship_id, year=dto.year, id=None)
        return await self.edition_repository.create(edition)

    async def update_edition(self, championship_id: int, edition_id: int, dto: UpdateChampionshipEditionDTO) -> ChampionshipEdition:
        championship = await self.championship_repository.get_by_id(championship_id)
        if not championship:
            raise ValueError("Campeonato não encontrado")

        existing = await self.edition_repository.get_by_id(edition_id)
        if not existing or existing.championship_id != championship_id:
            raise ValueError("Edição não encontrada")

        new_year = dto.year if dto.year is not None else existing.year
        if new_year != existing.year:
            already_exists = await self.edition_repository.exists_by_championship_and_year(championship_id, new_year)
            if already_exists:
                raise ValueError(f"Já existe uma edição de {new_year} para esse campeonato")

        edition = ChampionshipEdition(championship_id=championship_id, year=new_year, id=edition_id)
        return await self.edition_repository.update(edition_id, edition)

    async def delete_edition(self, championship_id: int, edition_id: int) -> None:
        championship = await self.championship_repository.get_by_id(championship_id)
        if not championship:
            raise ValueError("Campeonato não encontrado")

        existing = await self.edition_repository.get_by_id(edition_id)
        if not existing or existing.championship_id != championship_id:
            raise ValueError("Edição não encontrada")

        await self.edition_repository.delete(edition_id)