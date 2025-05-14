def extract_inputs(user_input):
    tokens = user_input.split()
    command_name = tokens[0].lower()
    args = tokens[0:]
    return args, command_name


def parse_bet_input(command_str: str) -> tuple[int, int]:
    try:
        _, horse_number, amount = command_str.split()
        return int(horse_number), int(amount)
    except ValueError:
        raise ValueError("Invalid bet command format. Use: Bet <horse_number> <amount>")