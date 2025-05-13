from app.commands.command_registry import CommandRegistry
from app.exceptions.exceptions import BettingTerminalException, QuitException
from app.model.horse import Horse
from app.model.cash_inventory import CashInventory
from app.model.horse_manager import HorseManager


class TellerMachine:
    def __init__(self, horses: list[Horse], inventory: CashInventory):
        self.cash_inventory = CashInventory(inventory)
        self.horse_manager = HorseManager(horses)
        self.command_registry = CommandRegistry(self.horse_manager,self.cash_inventory)

    def start(self):
        while True:
            try:
                user_input = input(">").strip()
                if not user_input:
                    continue

                tokens = user_input.split()
                command_name = tokens[0].lower()
                args = tokens[1:]

                command = self.command_registry.get_command(command_name)
                output = command.execute(args)
                print(output)

            except QuitException as qe:
                print(str(qe))
                break
            except BettingTerminalException as e:
                print(f"Error: {str(e)}")
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Unexpected error: {str(e)}")
