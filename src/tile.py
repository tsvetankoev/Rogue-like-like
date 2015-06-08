class Tile:

    def __init__(self):
        self._passable = False
        self._visible = False
        self._entrance = False
        self._exit = False
        self._player = False

    def make_passable(self):
        self._passable = True

    def seen(self):
        self._visible = True

    def draw(self):
        if not self._passable:
            return "#"
        if self._player:
            return "@"
        if not self._visible:
            return " "
        if self._entrance or self._exit:
            return "X"
        if self._visible:
            return "."
