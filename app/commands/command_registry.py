from commands.place_bet_command import PlaceBetCommand
from commands.set_winner_command import SetWinnerCommand
from commands.inventory_command import InventoryCommand
from commands.display_command import DisplayCommand
from commands.restock_command import RestockCommand
from commands.quit_command import QuitCommand
from core.horse_manager import HorseManager
from core.cash_inventory import CashInventory

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
            from exceptions import InvalidCommandException
            raise InvalidCommandException(name)
        return command
