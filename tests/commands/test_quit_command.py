import pytest
from app.commands.quit_command import QuitCommand
from app.exceptions.exceptions import InvalidCommandException


def test_quit_command_validate_uppercase_q_does_not_raise_exception():
    command = QuitCommand()
    try:
        command.validate("Q")
    except Exception as e:
        pytest.fail(f"validate() raised an exception unexpectedly: {e}")


def test_quit_command_validate_lowercase_q_does_not_raise_exception():
    command = QuitCommand()
    try:
        command.validate("q")
    except Exception as e:
        pytest.fail(f"validate() raised an exception unexpectedly: {e}")


def test_quit_command_validate_invalid_command_raises_invalid_command_exception():
    command = QuitCommand()
    with pytest.raises(InvalidCommandException) as exc_info:
        command.validate("quit")
    assert "Invalid Command: quit" in str(exc_info.value)


def test_quit_command_validate_q_with_extra_arguments_raises_invalid_command_exception():
    command = QuitCommand()
    with pytest.raises(InvalidCommandException) as exc_info:
        command.validate("q extra_argument")
    assert "Invalid Command: q extra_argument" in str(exc_info.value)


def test_quit_command_validate_q_with_whitespace_raises_invalid_command_exception():
    command = QuitCommand()
    with pytest.raises(InvalidCommandException) as exc_info:
        command.validate("q ")
    assert "Invalid Command: q " in str(exc_info.value)


if __name__ == "__main__":
    print("Running tests...")