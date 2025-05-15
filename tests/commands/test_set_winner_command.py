import pytest
from unittest.mock import MagicMock
from app.commands.set_winner_command import WinningsCommand
from app.exceptions.exceptions import InvalidHorseException, InvalidCommandException


@pytest.fixture
def mock_horse_manager():
    horse_manager = MagicMock()
    horse_manager.is_valid_horse.side_effect = lambda horse_number: 1 <= horse_number <= 7

    def get_mock_horse(horse_number):
        horse = MagicMock()
        horse.name = f"Horse {horse_number}"
        return horse

    horse_manager.get_horse.side_effect = get_mock_horse
    return horse_manager


def test_execute_valid_command(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    result = command.execute(["W", "3"])
    assert result == "Winner: Horse 3"
    mock_horse_manager.set_winner.assert_called_once_with(3)


def test_execute_valid_command_lowercase(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    result = command.execute(["w", "5"])
    assert result == "Winner: Horse 5"
    mock_horse_manager.set_winner.assert_called_once_with(5)


def test_validate_valid_command(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    command.validate("W 4")  # Should not raise any exception


def test_validate_invalid_command_format(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    with pytest.raises(InvalidCommandException):
        command.validate("W")  # Missing horse number


def test_validate_invalid_horse_number_non_digit(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    with pytest.raises(InvalidHorseException):
        command.validate("W X")  # Non-digit horse number


def test_validate_invalid_horse_number_out_of_range(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    with pytest.raises(InvalidHorseException):
        command.validate("W 8")  # Horse number out of range


def test_validate_invalid_horse_number_negative(mock_horse_manager):
    command = WinningsCommand(mock_horse_manager)
    with pytest.raises(InvalidHorseException):
        command.validate("W -1")  # Horse number out of range