class Tile:

    def __init__(self):
        self._passable = False
        self._visible = False
        self._entrance = False
        self._exit = False
        self._player = False
        self._contents = None
        self._has_item = False
        self._has_monster = False
        self._is_visited = False

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

    def add_monster(self):
        self._has_monster = True

    def add_item(self):
        self._has_item = True

    def is_visited(self):
        return self._is_visited

    def is_entrance(self):
        return self._entrance

    def is_exit(self):
        return self._exit

    def is_passable(self):
        return self._passable

    def has_monster(self):
        return self._has_monster

    def has_item(self):
        return self._has_item

    def contents(self):
        return self._contents

    def remove_contents(self):
        self._contents = None
