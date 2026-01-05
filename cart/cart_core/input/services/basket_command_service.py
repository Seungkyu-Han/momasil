from abc import ABC, abstractmethod


class BasketCommandService(ABC):

    @abstractmethod
    async def create_basket(
            self,
            name: str,
    ):
        ...