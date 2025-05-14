import pytest
from unittest.mock import MagicMock

from app.commands.place_bet_command import BetCommand as PlaceBetCommand
from app.commands.set_winner_command import WinningsCommand as SetWinnerCommand
# from app.commands.inventory_command import InventoryCommand
from app.commands.restock_command import RestockCommand
from app.commands.quit_command import QuitCommand
from app.exceptions.exceptions import InvalidCommandException

from app.commands.command_registry import CommandRegistry


@pytest.fixture
def mock_dependencies():
    horse_manager = MagicMock()
    cash_inventory = MagicMock()
    return horse_manager, cash_inventory


def test_registry_returns_place_command(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    registry = CommandRegistry(horse_manager, cash_inventory)

    command = registry.get_command("place")
    assert isinstance(command, PlaceBetCommand)


def test_registry_returns_bet_command_alias(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    registry = CommandRegistry(horse_manager, cash_inventory)

    command = registry.get_command("bet")
    assert isinstance(command, PlaceBetCommand)


def test_registry_returns_winner_command(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    registry = CommandRegistry(horse_manager, cash_inventory)

    command = registry.get_command("winner")
    assert isinstance(command, SetWinnerCommand)


# def test_registry_returns_inventory_command(mock_dependencies):
#     horse_manager, cash_inventory = mock_dependencies
#     registry = CommandRegistry(horse_manager, cash_inventory)
#
#     command = registry.get_command("inventory")
#     assert isinstance(command, InventoryCommand)


def test_registry_returns_restock_command(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    registry = CommandRegistry(horse_manager, cash_inventory)

    command = registry.get_command("restock")
    assert isinstance(command, RestockCommand)


def test_registry_returns_quit_command(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    registry = CommandRegistry(horse_manager, cash_inventory)

    command = registry.get_command("quit")
    assert isinstance(command, QuitCommand)


def test_registry_raises_invalid_command(mock_dependencies):
    horse_manager, cash_inventory = mock_dependencies
    registry = CommandRegistry(horse_manager, cash_inventory)

    with pytest.raises(InvalidCommandException) as exc_info:
        registry.get_command("invalid")

    assert "invalid" in str(exc_info.value).lower()