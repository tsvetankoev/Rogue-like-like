class Equipment:

    def __init__(self, name, strength, dexterity, inteligence):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.inteligence = inteligence

    def type(self):
        return self._name.split()[0]
