from abc import ABC, abstractmethod

from domain.entities.championship_edition_entity import ChampionshipEdition


class ChampionshipEditionRepositoryPort(ABC):

    @abstractmethod
    async def get_all(self) -> list[ChampionshipEdition]: ...

    @abstractmethod
    async def get_by_id(self, edition_id: int) -> ChampionshipEdition | None: ...

    @abstractmethod
    async def get_by_championship(self, championship_id: int) -> list[ChampionshipEdition]: ...

    @abstractmethod
    async def create(self, edition: ChampionshipEdition) -> ChampionshipEdition: ...

    @abstractmethod
    async def update(self, edition_id: int, edition: ChampionshipEdition) -> ChampionshipEdition | None: ...

    @abstractmethod
    async def delete(self, edition_id: int) -> bool: ...