from app.services.teller_machine import TellerMachine

if __name__ == "__main__":
    teller_machine = TellerMachine()
    print("Welcome to the Betting Teller Machine!")
    print("Type a command to begin (e.g., 'inventory', 'bet <horse_number> <amount>', 'quit'):")
    teller_machine.start()