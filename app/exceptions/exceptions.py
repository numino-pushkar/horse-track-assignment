# exceptions.py

class BettingTerminalException(Exception):
    """Base class for all betting terminal exceptions."""
    pass


class InvalidCommandException(BettingTerminalException):
    """Raised when an unknown or unsupported command is entered."""
    def __init__(self, command: str):
        super().__init__(f"Invalid Command: {command}")


class InvalidHorseException(BettingTerminalException):
    """Raised when a horse number is not found."""
    def __init__(self, horse_number: str):
        super().__init__(f"Invalid Horse Number: {horse_number}")


class InvalidBetFormatException(BettingTerminalException):
    """Raised when a bet command is malformed or has wrong data types."""
    def __init__(self, message="Invalid Bet: Usage <HorseNumber> <Amount>"):
        super().__init__(message)


class NoPayoutException(BettingTerminalException):
    """Raised when the selected horse did not win."""
    def __init__(self, horse_name: str):
        super().__init__(f"No Payout: {horse_name}")


class InsufficientFundsException(BettingTerminalException):
    """Raised when the machine cannot dispense the payout amount."""
    def __init__(self, amount: int):
        super().__init__(f"Insufficient Funds: {amount}")


class QuitException(BettingTerminalException):
    """Raised to signal graceful shutdown of the application."""
    pass


