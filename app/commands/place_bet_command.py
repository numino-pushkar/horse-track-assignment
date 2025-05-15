from app.constants.constants import PAYOUT_MESSAGE
from app.exceptions.exceptions import (
    InvalidHorseException,
    NoPayoutException,
    InsufficientFundsException, InvalidBetAmountException,
)
from app.interfaces.command import Command
from app.model.horse_manager import HorseManager
from app.model.cash_inventory import CashInventory
from app.utils.string_util import extract_inputs


class BetCommand(Command):
    def __init__(self, horse_manager: HorseManager, cash_inventory: CashInventory):
        self.horse_manager = horse_manager
        self.cash_inventory = cash_inventory

    def validate(self, command: str) -> None:
        bet, horse_number = extract_inputs(command)
        bet_amount: str = bet[1]

        if not bet_amount.isdigit() or int(bet_amount) <= 0:
            raise InvalidBetAmountException(str(bet_amount))

        if not horse_number.isdigit() or not self.horse_manager.is_valid_horse(int(horse_number)):
            raise InvalidHorseException(horse_number)

    def execute(self, args: list[str]) -> None:

        horse_number = int(args[0])
        amount = int(args[1])
        horse = self.horse_manager.get_horse(horse_number)

        if not horse.won:
            raise NoPayoutException(horse.name)

        payout = horse.odds * amount
        bills = self.cash_inventory.dispense(payout)

        if bills is None:
            raise InsufficientFundsException(payout)

        breakdown = "\n".join([f"${denom},{count}" for denom, count in sorted(bills.items())])
        print(PAYOUT_MESSAGE.format(horse_name=horse.name, payout=payout, breakdown=breakdown))