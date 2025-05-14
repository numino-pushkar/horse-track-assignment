import pytest
from app.commands.quit_command import QuitCommand
from app.constants.constants import INVALID_COMMAND
from app.exceptions.exceptions import InvalidCommandException


def test_quit_command_validate_uppercase_q_does_not_raise_exception():
    input_command = "Q"
    command = QuitCommand()
    try:
        command.validate(input_command)
    except Exception as e:
        pytest.fail(f"validate() raised an exception unexpectedly: {e}")


def test_quit_command_validate_lowercase_q_does_not_raise_exception():
    input_command = "q"
    command = QuitCommand()
    try:
        command.validate(input_command)
    except Exception as e:
        pytest.fail(f"validate() raised an exception unexpectedly: {e}")


def test_quit_command_validate_invalid_command_raises_invalid_command_exception():
    input_command = "quit"
    command = QuitCommand()
    with pytest.raises(InvalidCommandException) as exc_info:
        command.validate(input_command)
    assert INVALID_COMMAND.format(input_command) in str(exc_info.value)


def test_quit_command_validate_q_with_extra_arguments_raises_invalid_command_exception():
    input_command = "q extra_argument"
    command = QuitCommand()
    with pytest.raises(InvalidCommandException) as exc_info:
        command.validate(input_command)
    assert INVALID_COMMAND.format(input_command) in str(exc_info.value)


def test_quit_command_validate_q_with_whitespace_does_not_raise_exception():
    input_command = "q "
    command = QuitCommand()
    try:
        command.validate(input_command)
    except Exception as e:
        pytest.fail(f"validate() raised an exception unexpectedly: {e}")


if __name__ == "__main__":
    print("Running tests...")