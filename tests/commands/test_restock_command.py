import pytest
from unittest.mock import MagicMock
from app.commands.restock_command import RestockCommand
from app.constants.constants import INVALID_COMMAND
from app.exceptions.exceptions import InvalidCommandException


@pytest.fixture
def mock_cash_inventory():
    return MagicMock()


def test_restock_command_executes_with_valid_command(mock_cash_inventory):
    command = RestockCommand(mock_cash_inventory)
    result = command.execute([])
    mock_cash_inventory.restock.assert_called_once()
    assert str(mock_cash_inventory) == result


def test_restock_command_validates_uppercase_r(mock_cash_inventory):
    input_command = "R"
    command = RestockCommand(mock_cash_inventory)
    try:
        command.validate(input_command)
    except InvalidCommandException:
        pytest.fail("validate() raised InvalidCommandException unexpectedly!")


def test_restock_command_validates_lowercase_r(mock_cash_inventory):
    input_command = "r"
    command = RestockCommand(mock_cash_inventory)
    try:
        command.validate(input_command)
    except InvalidCommandException:
        pytest.fail("validate() raised InvalidCommandException unexpectedly!")


def test_restock_command_raises_exception_for_invalid_arguments(mock_cash_inventory):
    input_command = "R 100"
    command = RestockCommand(mock_cash_inventory)
    with pytest.raises(InvalidCommandException, match=INVALID_COMMAND.format(input_command)):
        command.validate(input_command)