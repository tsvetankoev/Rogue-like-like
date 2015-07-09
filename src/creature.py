class Creature:

    def __init__(self, name, hp, mana, strength, dexterity, inteligence):
        self._name = name
        self._hp = hp
        self._mana = mana
        self._core_strength = strength
        self._core_dexterity = dexterity
        self._core_inteligence = inteligence

    def print_invetory(self):
        for item in self._inventory:
                print(item.name())

    def name(self):
        return self._name
