from abc import ABC, abstractmethod
from domain.entities.title_type import TitleType


class TitleTypeRepositoryPort(ABC):

    @abstractmethod
    async def get_all(self) -> list[TitleType]: ...

    @abstractmethod
    async def get_by_id(self, title_type_id: int) -> TitleType | None: ...

    @abstractmethod
    async def create(self, title_type: TitleType) -> TitleType: ...

    @abstractmethod
    async def update(self, title_type_id: int, title_type: TitleType) -> TitleType | None: ...

    @abstractmethod
    async def delete(self, title_type_id: int) -> bool: ...