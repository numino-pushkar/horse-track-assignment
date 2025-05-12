class WinningsCommand(Command):
    def __init__(self, horse_manager: HorseManager):
        self.horse_manager = horse_manager

    def execute(self, args: list[str]) -> str:
        if len(args) != 1 or not args[0].isdigit():
            raise InvalidHorseException("Invalid input. Usage: <HorseNumber>")
        horse_number = int(args[0])
        if not self.horse_manager.set_winner(horse_number):
            raise InvalidHorseException(horse_number)

        horse = self.horse_manager.get_horse(horse_number)
        return f"Winner: {horse.name}"
