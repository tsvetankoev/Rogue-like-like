class Potion:

    def __init__(self, name, value):
        self.name = name
        self._value = value

    def use(self):
        stat = self.name.replace("Potion of ", "")
        stat = stat.lower()
        return (stat, self._value)
