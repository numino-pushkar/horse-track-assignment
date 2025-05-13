from app.interfaces.command import Command
from app.exceptions.exceptions import QuitException


class QuitCommand(Command):
    def execute(self, args: list[str]) -> str:
        raise QuitException("Quitting Teller Machine.")