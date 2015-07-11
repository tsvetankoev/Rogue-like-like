from creature import *


class Monster(Creature):

    def __init__(self, name, hp, mana, strength, dexterity, intelligence):
        Creature.__init__(self, name, hp, mana, strength,
                          dexterity, intelligence)

    def attack(self, target):
        if random.randint(1, 5) == 1:
            return self.spell_attack(target)
        return self.weapon_attack(target)
