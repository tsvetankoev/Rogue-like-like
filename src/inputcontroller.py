def choose_attack():
    input_text = "Choose type of attack(Weapon or Spell):"
    attack = input(input_text).lower()
    return attack

def select_name():
    name = input("Select Your Name: ")
    return name

def select_command():
    command = input("")
    return command

def choose_stat():
    stat = input("Choose stat to level up (Strength, "
                 "Inteligence or Dexterity):").lower()
    return stat

def wrong_input():
    new_input = input("Input is wrong. Please try again").lower()
    return new_input

def command_interpretator(command):
    command = command.lower()
    if "go" in command:
        return command.split(" ", 1)
    if "help" == command:
        return command
    if "stats" == command:
        return command
    if "inventory" == command:
        return command
    if "use" in command:
        return command.split(" ", 1)
    if "equip" in command:
        return command.split(" ", 1)
    else:
        return False
    
def press_enter_to_continue():
    dump_var = input("Press Enter to continue.")