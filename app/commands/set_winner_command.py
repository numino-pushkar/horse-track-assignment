from app.interfaces.command import Command
from app.model.horse_manager import HorseManager
from app.exceptions.exceptions import InvalidHorseException, InvalidCommandException
from app.utils.string_util import extract_inputs


class WinningsCommand(Command):

    def __init__(self, horse_manager: HorseManager):
        self.horse_manager = horse_manager

    def execute(self, args: list[str]) -> str:
        horse_number = int(args[1])
        self.horse_manager.set_winner(horse_number)

        horse = self.horse_manager.get_horse(horse_number)
        return f"Winner: {horse.name}"

    def validate(self, command: str) -> None:
        args, command = extract_inputs(command)
        if len(args) != 2:
            raise InvalidCommandException("Invalid number of arguments. Expected 1 argument.")
        horse_number = args[1]
        if not horse_number.isdigit():
            raise InvalidHorseException(f"Invalid horse number: {horse_number}")
        elif not self.horse_manager.is_valid_horse(int(horse_number)):
            raise InvalidHorseException(str(horse_number))

