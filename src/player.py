import creature

class Player(Creature):

    def __init__(self, name):
        super(name)
        self._inventory = []
        self._equiped = []
        self._health = 10
        self._experience = 0
        self._level = 1
        self._core_strength = 1
        self._core_inteligence = 1
        self._core_dexterity = 1
        self._strength = 1
        self._inteligence = 1
        self._dexterity = 1

    def level_up(self):
        self._level = self._level + 1
        stat = input("Choose stat to level up (Strength, Inteligence or Dexterity):").lower()
        leveled = False
        while(not leveled):
            if (stat == "strength"):
                self._strength = self._strength + 1
                leveled = True
            elif (stat == "inteligence"):
                self._inteligence += 1
                leveled = True
            elif (stat == "dexterity"):
                self._dexterity += 1
                leveled = True
            else:
                stat = input("Input is wrong. Please try again").lower()

    def list_inventory(self):
        for item in self._inventory:
            print(item.get_name())

    def health(self):
        return self._health

    def level(self):
        return self._level
