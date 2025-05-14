# from app.interfaces.command import Command
# from app.model.cash_inventory import CashInventory
#
#
# class InventoryCommand(Command):
#     def __init__(self, cash_inventory: CashInventory):
#         self.cash_inventory = cash_inventory
#
#     def execute(self, args: list[str]) -> str:
#         return str(self.cash_inventory)