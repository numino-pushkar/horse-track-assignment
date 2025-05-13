from app.commands.place_bet_command import BetCommand as PlaceBetCommand
from app.commands.set_winner_command import WinningsCommand as SetWinnerCommand
from app.commands.inventory_command import InventoryCommand
from app.commands.display_command import DisplayCommand
from app.commands.restock_command import RestockCommand
from app.commands.quit_command import QuitCommand
from app.model.horse_manager import HorseManager
from app.model.cash_inventory import CashInventory
from app.exceptions.exceptions import InvalidCommandException


class CommandRegistry:
    def __init__(self):
        self.horse_manager = HorseManager()
        self.cash_inventory = CashInventory()
        self.commands = {
            "place": PlaceBetCommand(self.horse_manager, self.cash_inventory),
            "bet": PlaceBetCommand(self.horse_manager, self.cash_inventory),  # alias
            "winner": SetWinnerCommand(self.horse_manager),
            "inventory": InventoryCommand(self.cash_inventory),
            "display": DisplayCommand(self.horse_manager),
            "restock": RestockCommand(self.cash_inventory),
            "quit": QuitCommand()
        }

    def get_command(self, name: str):
        command = self.commands.get(name.lower())
        if not command:
            raise InvalidCommandException(name)
        return command
