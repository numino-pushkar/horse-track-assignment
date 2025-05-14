def extract_inputs(user_input):
    tokens = user_input.split()
    command_name = tokens[0].lower()
    args = tokens[0:]
    return args, command_name