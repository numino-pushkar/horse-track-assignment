import pytest
from unittest.mock import MagicMock
from app.commands.place_bet_command import BetCommand
from app.exceptions.exceptions import (
    InvalidHorseException,
    NoPayoutException,
    InsufficientFundsException,
    InvalidBetAmountException,
)


@pytest.fixture
def mock_dependencies():
    horse_manager = MagicMock()
    cash_inventory = MagicMock()
    return horse_manager, cash_inventory


def test_validate_valid_bet(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    horse_manager.is_valid_horse.return_value = True
    command = BetCommand(horse_manager, cash_inventory)

    # Valid command
    command.validate("1 100")
    horse_manager.is_valid_horse.assert_called_once_with(1)


def test_validate_invalid_bet_amount(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    command = BetCommand(horse_manager, cash_inventory)

    # Invalid bet amount
    with pytest.raises(InvalidBetAmountException):
        command.validate("1 -100")

    with pytest.raises(InvalidBetAmountException):
        command.validate("1 abc")

    with pytest.raises(InvalidBetAmountException):
        command.validate("1 10.24")


def test_validate_invalid_horse_number(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    horse_manager.is_valid_horse.return_value = False
    command = BetCommand(horse_manager, cash_inventory)

    # Invalid horse number
    with pytest.raises(InvalidHorseException):
        command.validate("8 100")


def test_execute_no_payout(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    horse_manager.get_horse.return_value.won = False
    command = BetCommand(horse_manager, cash_inventory)

    # No payout scenario
    with pytest.raises(NoPayoutException):
        command.execute(["1", "100"])


def test_execute_insufficient_funds(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    horse_manager.get_horse.return_value = MagicMock(won=True, odds=2, name="Horse 1")
    cash_inventory.dispense.return_value = None
    command = BetCommand(horse_manager, cash_inventory)

    # Insufficient funds scenario
    with pytest.raises(InsufficientFundsException):
        command.execute(["1", "100"])


def test_execute_successful_payout(mock_dependencies, capsys):
    horse_manager, cash_inventory = mock_dependencies

    # Properly mock the horse
    mock_horse = MagicMock()
    mock_horse.won = True
    mock_horse.odds = 2
    mock_horse.name = "Horse 1"
    horse_manager.get_horse.return_value = mock_horse

    # Mock cash dispense
    cash_inventory.dispense.return_value = {100: 2, 50: 1}

    command = BetCommand(horse_manager, cash_inventory)

    # Execute command
    command.execute(["1", "100"])
    captured = capsys.readouterr()

    # Assertions
    assert "Payout: Horse 1, $200" in captured.out
    assert "$100,2" in captured.out
    assert "$50,1" in captured.out
