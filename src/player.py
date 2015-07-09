from creature import *


class Player(Creature):

    def __init__(self, name):
        Creature.__init__(self, name, 11, 20, 1, 1, 1)
        self.inventory = []
        self._equipped = {"Sword": None, "Shield": None}
        self._shield = None
        self._experience = 0
        self._level = 1
        self._strength = self._core_strength
        self._inteligence = self._core_inteligence
        self._dexterity = self._core_dexterity

    def level_up(self):
        self._level = self._level + 1
        stat = input("Choose stat to level up (Strength, "
                     "Inteligence or Dexterity):").lower()
        leveled = False
        while(not leveled):
            if (stat == "strength"):
                self._corestrength = self._corestrength + 1
                leveled = True
            elif (stat == "inteligence"):
                self._coreinteligence += 1
                leveled = True
            elif (stat == "dexterity"):
                self._coredexterity += 1
                leveled = True
            else:
                stat = input("Input is wrong. Please try again").lower()

    def health(self):
        return self._health

    def level(self):
        return self._level

    def set_name(self, name):
        self._name = name

    def is_alive(self):
        return self._health > 0

    def add_to_invetory(self, items):
        self.inventory.append(items)

    def use_item(self, itemname):
        for item in self._inventory:
            if item.name() == itemname:
                (stat, value) = item.use()
                if (stat == "Health"):
                    self._hp += value
                elif stat == "Mana":
                    self._mana += value
                elif stat == "Strength":
                    self._corestrength += value
                elif stat == "Dexterity":
                    self._coredexterity += value
                elif stat == "Inteligence":
                    self._coreinteligence += value
                self._inventory.remove(item)
                self._recalculate_stats()
                return

        print("No such item has been found")

    def equip_item(self, itemname):
        item_to_equip = None
        for item in self._inventory:
            if item.name() == itemname:
                item_to_equip = item
        if item_to_equip is None:
            print("No such item has been found")
        else:
            self._equipped[item_to_equip.type()] = item_to_equip
            self._recalculate_stats()

    def _recalculate_stats(self):
        self._strength = self._corestrength
        self._dexterity = self._coredexterity
        self._inteligence = self._coreinteligence
        items = list(self._equipped.values())
        for item in items:
            self._strength += item.strength
            self._dexterity += item.dexterity
            self._inteligence += item.inteligence
        self._hp = self._dexterity * 10 + self._strength
        self._mana = self._inteligence * 20
