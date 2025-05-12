from app.commands.command_registry import CommandRegistry
from app.exceptions.exceptions import BettingTerminalException, QuitException

class TellerMachine:
    def __init__(self):
        self.command_registry = CommandRegistry()

    def start(self):
        while True:
            try:
                user_input = input(">").strip()
                if not user_input:
                    continue

                tokens = user_input.split()
                command_name = tokens[0].lower()
                args = tokens[1:]

                command = self.command_registry.get_command(command_name)
                output = command.execute(args)
                print(output)

            except BettingTerminalException as e:
                print(f"Error: {str(e)}")
            except QuitException as qe:
                print(str(qe))
                break
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Unexpected error: {str(e)}")
