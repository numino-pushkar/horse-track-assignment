from app.interfaces.command import Command
from app.exceptions.exceptions import QuitException, InvalidCommandException
from app.utils.string_util import extract_inputs


class QuitCommand(Command):
    def execute(self, args: list[str]) -> str:
        raise QuitException("Quitting Teller Machine.")

    def validate(self, command: str) -> None:
        args, quit_command = extract_inputs(command)
        if len(args) > 1:
            raise InvalidCommandException(command)
