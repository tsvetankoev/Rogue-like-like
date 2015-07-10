from inputcontroller import InputController
from outputcontroller import OutputController


class Battle:

    def __init__(self, player, monster):
        self._player = player
        self._monster = monster

    def start(self):
        while (self._player.health() > 0 or self._monster.health() > 0):
            not_valid_attack = True
            while (not_valid_attack):
                attack = InputController.choose_attack()
                if ("weapon" in attack):
                    self._monster.take_damage(self._player.weapon_attack())
                    not_valid_attack = False
                elif ("spell" in attack):
                    self._monster.take_damage(self._player.spell_attack())
                    not_valid_attack = False
                else:
                    OutputController.not_valid_attack()
            self._player.take_damage(self._monster.weapon_attack())
        if self._player.is_alive():
            OutputController.battle_won()
            OutputController.items_found()

            # TODO
            self._monster.print_inventory()
            self._player.add_to_inventory(self._monster.inventory())
        return self._player
