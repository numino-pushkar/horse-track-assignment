from app.interfaces.command import Command
from app.exceptions.exceptions import QuitException
from app.utils.string_util import extract_inputs


class QuitCommand(Command):
    def execute(self, args: list[str]) -> str:
        raise QuitException("Quitting Teller Machine.")

    def validate(self, command: str) -> None:
        args, command = extract_inputs(command)
        if len(args) > 1:
            raise ValueError("QuitCommand does not accept any arguments.")
