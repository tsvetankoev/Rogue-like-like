from item import Item


class Potion(Item):

    def __init__(self, name, value):
        Item.__init__(self, name)
        self._value = value

    def use(self):
        potion_name = self._name.replace("Potion of ", "")
        return (potion_name, self._value)
