class Battle:

    def __init__(self, player, monster):
        self._player = player
        self._monster = monster

    def start(self):
        while (self._player.health() > 0 or self._monster.health() > 0):
            not_valid_attack = True
            input_text = "Choose type of attack(Weapon or Spell):"
            while (not_valid_attack):
                attack = input(input_text).lower()
                if ("weapon" in attack):
                    self._monster.take_damage(self._player.weapon_attack())
                    not_valid_attack = False
                elif ("spell" in attack):
                    self._monster.take_damage(self._player.spell_attack())
                    not_valid_attack = False
                else:
                    print("You didn't choose a valid attack")
            self._player.take_damage(self._monster.weapon_attack())
        if self._player.is_alive():
            print("Congratulation. You won.")
            print("You have found the following items:")
            self._monster.print_inventory()
            self._player.add_to_inventory(self._monster.inventory())
        return self._player
