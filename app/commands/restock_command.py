from app.interfaces.command import Command
from app.model.cash_inventory import CashInventory


class RestockCommand(Command):
    def __init__(self, cash_inventory: CashInventory):
        self.cash_inventory = cash_inventory

    def execute(self, args: list[str]) -> str:
        self.cash_inventory.restock()
        return str(self.cash_inventory)
