from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, args: list[str]) -> str:
        pass

    @abstractmethod
    def validate(self, args: list[str]) -> None:
        pass
