from app.exceptions.exceptions import (
    InvalidHorseException,
    InvalidBetFormatException,
    NoPayoutException,
    InsufficientFundsException,
)
from app.interfaces.command import Command
from app.model.horse_manager import HorseManager
from app.model.cash_inventory import CashInventory


class BetCommand(Command):
    def __init__(self, horse_manager: HorseManager, cash_inventory: CashInventory):
        self.horse_manager = horse_manager
        self.cash_inventory = cash_inventory

    def execute(self, args: list[str]) -> str:
        if len(args) != 2 or not args[0].isdigit() or not args[1].isdigit():
            raise InvalidBetFormatException()

        horse_number = int(args[0])
        amount = int(args[1])
        horse = self.horse_manager.get_horse(horse_number)

        if horse is None:
            raise InvalidHorseException(horse_number)

        if not horse.won:
            raise NoPayoutException(horse.name)

        payout = horse.odds * amount
        bills = self.cash_inventory.dispense(payout)

        if bills is None:
            raise InsufficientFundsException(payout)

        breakdown = " ".join([f"${denom},{count}" for denom, count in sorted(bills.items(), reverse=True)])
        return f"Payout: {horse.name}, ${payout}\n{breakdown}"