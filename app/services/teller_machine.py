from app.commands.command_registry import CommandRegistry
from app.exceptions.exceptions import BettingTerminalException, QuitException
from app.model.horse import Horse
from app.model.cash_inventory import CashInventory
from app.model.horse_manager import HorseManager
from app.constants.constants import INITIAL_HORSE_WINNER
from app.utils.string_util import extract_inputs


class TellerMachine:
    def __init__(self, horses: list[Horse], inventory: CashInventory):
        self.cash_inventory = CashInventory(inventory)
        self.horse_manager = HorseManager(horses)
        self.horse_manager.set_winner(INITIAL_HORSE_WINNER)
        print(self.cash_inventory)
        print(self.horse_manager)

        self.command_registry = CommandRegistry(self.horse_manager, self.cash_inventory)

    def start(self):
        while True:
            try:
                user_input = input(">").strip()
                if not user_input:
                    continue

                args, command_name = extract_inputs(user_input)

                command = self.command_registry.get_command(command_name)
                command.validate(user_input)
                command.execute(args)
                print(self.cash_inventory)
                print(self.horse_manager)

            except QuitException as qe:
                print(str(qe))
                break
            except BettingTerminalException as e:
                print(str(e))
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Unexpected error: {str(e)}")


