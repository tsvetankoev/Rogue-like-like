import Tile


class Map:

    def __init__(self, temp_map, level, startX, startY, endX, endY):
        self._map = temp_map
        self._width = len(self._map[0])
        self._heigth = len(self._map)
        self._level = level
        self._startX = startX
        self._endX = endX
        self._startY = startY
        self._endY = endY
        self._playerX = startX
        self._playerY = startY

    def _valid_position(self, x, y):
        return x in range(0, self._width) and y in range(0, self._heigth)

    def _get_tile(self, x, y):
        return self._map[x, y]

    def clear_current_field(self):
        self.map[self._playerX, self._playerY].contents = None

    def _see_neighbours(self):
        for x in range(self._playerX - 1, self._playerX + 2):
            for y in range(self._playerY - 1, self._playerY + 2):
                if (self._valid_position(x, y)):
                    self._map[x, y].seen()

    def go_north(self):
        if (self._valid_position(self._playerX, self._playerY-1)):
            print("Can't go that way.")
        elif (self._map[self._playerX, self._playerY-1].is_passable):
            print("Can't go that way.")
        else:
            self._playerY = self._playerY - 1
            self._see_neighbours()

    def go_south(self):
        if (self._valid_position(self._playerX, self._playerY+1)):
            print("Can't go that way.")
        elif (self._map[self._playerX, self._playerY+1].is_passable):
            print("Can't go that way.")
        else:
            self._playerY = self._playerY + 1
            self._see_neighbours()

    def go_west(self):
        if (self._valid_position(self._playerX-1, self._playerY)):
            print("Can't go that way.")
        elif (self._map[self._playerX-1, self._playerY].is_passable):
            print("Can't go that way.")
        else:
            self._playerX = self._playerX - 1
            self._see_neighbours()

    def draw_map(self):
        for row in self._map:
            for cell in row:
                print(cell.draw(), "")
            print
