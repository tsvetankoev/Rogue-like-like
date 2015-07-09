from item import Item


class Equipment(Item):

    def __init__(self, name, strength, dexterity, inteligence):
        Item.__init__(self, name)
        self.strength = strength
        self.dexterity = dexterity
        self.inteligence = inteligence

    def type(self):
        return self._name.split()[0]
