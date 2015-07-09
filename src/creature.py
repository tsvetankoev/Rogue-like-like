class Creature:

    def __init__(self, name):
        self._name = name
        self._inventory = []

    def print_invetory(self):
        for item in self._inventory:
                print(item.name())

    def name(self):
        return self._name
