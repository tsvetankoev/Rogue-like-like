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
        if not self._visible:
            return " "
        if self._entrance:
            return "X"
        if not self._passable:
            return "#"
        if self._player:
            return "@"
        if self._exit:
            return "X"
        if self._entrance:
            return "E"
        else:
            return "."

    def add_monster(self):
        self._has_monster = True

    def add_item(self):
        self._has_item = True

    def add_entrance(self):
        self._entrance = True

    def add_exit(self):
        self._exit = True

    def add_player(self):
        self._player = True

    def remove_player(self):
        self._player = False

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
