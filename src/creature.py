import random
import outputcontroller


class Creature:

    def __init__(self, name, hp, mana, strength, dexterity, intelligence):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def attack(self, target):
        raise NotImplementedError
    
    def resistance(self, stat):
        return self.dexterity - stat
    
    def weapon_attack(self, target):
        resistance = self.resistance(target.strength)
        damage = self.strength*5 - resistance * 2
        self._attack_helper(target, damage)
    
    def spell_attack(self, target):
        self.mana -= 10
        resistance = self.resistance(target.intelligence)
        damage = self.intelligence*5 - resistance * 2
        self._attack_helper(target, damage)

    def _attack_helper(self, target, damage):
        critical = False
        if random.randint(0, 9) == 0:
            damage *= 2
            critical = True
        outputcontroller.attacks(self.name, target.name, damage, critical)
        target.hp -= damage
        
