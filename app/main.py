from app.services.teller_machine import TellerMachine
from app.config.horse_loader import load_horses_from_config
from app.config.inventory_loader import load_inventory_from_config

if __name__ == "__main__":
    print("Welcome to the Betting Teller Machine!")
    print("Type a command to begin (e.g., 'inventory', 'bet <horse_number> <amount>', 'quit'):")
    horses = load_horses_from_config()
    inventory = load_inventory_from_config()
    teller_machine = TellerMachine(horses, inventory)
    teller_machine.start()