from app.interfaces.command import Command
from app.services.teller_machine import TellerMachine


class DisplayCommand(Command):
    def __init__(self, teller_machine: TellerMachine):
        self.teller_machine = teller_machine

    def execute(self):
        self.teller_machine.display_inventory()
        self.teller_machine.display_horses()