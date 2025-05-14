from app.commands.place_bet_command import BetCommand as PlaceBetCommand
from app.commands.set_winner_command import WinningsCommand as SetWinnerCommand
# from app.commands.inventory_command import InventoryCommand
# from app.commands.display_command import DisplayCommand
from app.commands.restock_command import RestockCommand
from app.commands.quit_command import QuitCommand
from app.exceptions.exceptions import InvalidCommandException
from app.constants.constants import *


class CommandRegistry:
    def __init__(self, horse_manager, cash_inventory):
        self.horse_manager = horse_manager
        self.cash_inventory = cash_inventory
        self.commands = {
            WINNER_COMMAND: SetWinnerCommand(self.horse_manager),
            QUIT_COMMAND: QuitCommand(),
            RESTOCK_COMMAND: RestockCommand(self.cash_inventory),
            BET: PlaceBetCommand(self.horse_manager, self.cash_inventory),
            # INVENTORY: InventoryCommand(self.cash_inventory)
            # "display": DisplayCommand(self.horse_manager),
        }

    def get_command(self, name: str):
        command = self.commands.get(name.lower())
        if not command:
            raise InvalidCommandException(name)
        return command
