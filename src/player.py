import creature

class Player(Creature):

    def __init__(self, name):
        super(name)
        self._inventory = {}
        self._equiped = {}
        self._experience = 0
        self._level = 1
        self._strength = 1
        self._inteligence = 1

