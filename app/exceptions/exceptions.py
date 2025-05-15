# exceptions.py
from app.constants.constants import (
    INVALID_COMMAND_MESSAGE, INVALID_HORSE_MESSAGE, INSUFFICIENT_FUNDS_MESSAGE, INVALID_BET_MESSAGE, NO_PAYOUT_MESSAGE
)


class BettingTerminalException(Exception):
    """Base class for all betting terminal exceptions."""
    pass


class InvalidCommandException(BettingTerminalException):
    """Raised when an unknown or unsupported command is entered."""
    def __init__(self, command: str):
        super().__init__(INVALID_COMMAND_MESSAGE.format(command))


class InvalidHorseException(BettingTerminalException):
    """Raised when a horse number is not found."""
    def __init__(self, horse_number: str):
        super().__init__(INVALID_HORSE_MESSAGE.format(horse_number))


class InvalidBetAmountException(BettingTerminalException):
    """Raised when a bet command is malformed or has wrong data types."""
    def __init__(self, bet_amount: str):
        super().__init__(INVALID_BET_MESSAGE.format(bet_amount))


class NoPayoutException(BettingTerminalException):
    """Raised when the selected horse did not win."""
    def __init__(self, horse_name: str):
        super().__init__(NO_PAYOUT_MESSAGE.format(horse_name))


class InsufficientFundsException(BettingTerminalException):
    """Raised when the machine cannot dispense the payout amount."""
    def __init__(self, amount: int):
        super().__init__(INSUFFICIENT_FUNDS_MESSAGE.format(amount))


class QuitException(BettingTerminalException):
    """Raised to signal graceful shutdown of the application."""
    pass


