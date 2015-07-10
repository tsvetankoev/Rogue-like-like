class InputController:

    @staticmethod
    def choose_attack():
        input_text = "Choose type of attack(Weapon or Spell):"
        attack = input(input_text).lower()
        return attack

    @staticmethod
    def select_name():
        name = input("Select Your Name: ")
        return name

    @staticmethod
    def select_command():
        command = input("")
        return command

    @staticmethod
    def choose_stat():
        stat = input("Choose stat to level up (Strength, "
                     "Inteligence or Dexterity):").lower()
        return stat

    @staticmethod
    def wrong_input():
        new_input = input("Input is wrong. Please try again").lower()
        return new_input
