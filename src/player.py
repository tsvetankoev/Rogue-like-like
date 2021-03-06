import inputcontroller
import outputcontroller
import random
from creature import Creature
from potion import Potion
from equipment import Equipment


class Player(Creature):

    def __init__(self, name):
        Creature.__init__(self, name, 11, 20, 1, 1, 1)
        self.inventory = []
        self._equipped = {"Sword": None, "Shield": None}
        self.xp = 0
        self.max_hp = 11
        self.level = 1
        self._core_strength = 1
        self._core_intelligence = 1
        self._core_dexterity = 1

    def attack(self, target):
        "Attacks target variable based on user input"
        while (True):
            attack = inputcontroller.choose_attack()
            if ("weapon" in attack):
                return self.weapon_attack(target)
            elif ("spell" in attack):
                return self.spell_attack(target)
            else:
                outputcontroller.not_a_valid_attack()

    def _level_up(self):
        outputcontroller.level_up()
        self.xp -= self.xp_for_next_level()
        self.level = self.level + 1
        points = 5
        while(points > 0):
            stat = inputcontroller.choose_stat()
            if (stat == "strength"):
                self._core_strength += 1
                points -= 1
            elif (stat == "inteligence"):
                self._core_intelligence += 1
                points -= 1
            elif (stat == "dexterity"):
                self._core_dexterity += 1
                points -= 1
            else:
                stat = inputcontroller.wrong_input()
        self._recalculate_stats()

    def add_to_inventory(self, items):
        self.inventory += items

    def use_item(self, itemname):
        for item in self.inventory:
            if item.name.lower() == itemname.lower() and type(item) is Potion:
                (stat, value) = item.use()
                if (stat == "health"):
                    self.hp += value
                    if (self.hp > self.max_hp):
                        self.hp = self.max_hp
                elif stat == "mana":
                    self.mana += value
                elif stat == "strength":
                    self._corestrength += value
                elif stat == "dexterity":
                    self._coredexterity += value
                elif stat == "intelligence":
                    self._coreintelligence += value
                self.inventory.remove(item)
                self._recalculate_stats()
                return
        outputcontroller.item_not_found()

    def equip_item(self, itemname):
        item_to_equip = None
        for item in self.inventory:
            if item.name == itemname.lower() and type(item) is Equipment:
                item_to_equip = item
        if item_to_equip is None:
            outputcontroller.item_not_found()
        else:
            self._equipped[item_to_equip.type()] = item_to_equip
            self._recalculate_stats()

    def _recalculate_stats(self):
        self.strength = self._core_strength
        self.dexterity = self._core_dexterity
        self.intelligence = self._core_intelligence
        items = list(self._equipped.values())
        for item in items:
            if item is not None:
                self.strength += item.strength
                self.dexterity += item.dexterity
                self.intelligence += item.intelligence
        self.max_hp = self.dexterity * 10 + self.strength
        self.mana = self.intelligence * 20

    def gain_XP(self):
        base_xp = random.randint(5, 10)
        multiplier = random.randint(10, 30) / 10
        self.xp += base_xp + base_xp * multiplier
        if self.xp_for_next_level() <= self.xp:
            self._level_up()

    def xp_for_next_level(self):
        return self.level * 1

    def stats(self):
        outputcontroller.print_stats(self.name, self.hp,
                                     self.max_hp, self.xp,
                                     self.xp_for_next_level(), self.strength,
                                     self.dexterity, self.intelligence)

    def print_inventory(self):
        outputcontroller.inventory(self.inventory)
