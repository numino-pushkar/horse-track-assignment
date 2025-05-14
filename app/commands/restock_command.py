from app.exceptions.exceptions import InvalidCommandException
from app.interfaces.command import Command
from app.model.cash_inventory import CashInventory
from app.utils.string_util import extract_inputs


class RestockCommand(Command):
    def __init__(self, cash_inventory: CashInventory):
        self.cash_inventory = cash_inventory

    def execute(self, args: list[str]) -> str:
        self.cash_inventory.restock()
        return str(self.cash_inventory)

    def validate(self, command: str) -> None:
        args, restock_command = extract_inputs(command)
        if len(args) > 1:
            raise InvalidCommandException(command)
