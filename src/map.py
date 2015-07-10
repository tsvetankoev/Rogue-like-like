import outputcontroller
from mapgenerator import MapGenerator

class Map:

    def __init__(self, level, temp_map, startX, startY, endX, endY):
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
        return self._map[y][x]

    def player_tile(self):
        self._get_tile(self._playerX, self._playerY)


    def _see_neighbours(self):
        for x in range(self._playerX - 1, self._playerX + 2):
            for y in range(self._playerY - 1, self._playerY + 2):
                if (self._valid_position(x, y)):
                    self._map[y][x].visible = True

    def go_north(self):
        if not(self._valid_position(self._playerX, self._playerY-1)):
            outputcontroller.movement_impossible()
        elif not(self._map[self._playerY-1][self._playerX].is_passable()):
            outputcontroller.movement_impossible()
        else:
            self._map[self._playerY][self._playerX].player = False
            self._playerY = self._playerY - 1
            self._map[self._playerY][self._playerX].player = True
            self._see_neighbours()

    def go_south(self):
        if not(self._valid_position(self._playerX, self._playerY+1)):
            outputcontroller.movement_impossible()
        elif not(self._map[self._playerY+1][self._playerX].is_passable()):
            outputcontroller.movement_impossible()
        else:
            self._map[self._playerY][self._playerX].remove_player()
            self._playerY = self._playerY + 1
            self._map[self._playerY][self._playerX].add_player()
            self._see_neighbours()

    def go_west(self):
        if not(self._valid_position(self._playerX-1, self._playerY)):
            outputcontroller.movement_impossible()
        elif not(self._map[self._playerY][self._playerX-1].is_passable()):
            outputcontroller.movement_impossible()
        else:
            self._map[self._playerY][self._playerX].remove_player()
            self._playerX = self._playerX - 1
            self._map[self._playerY][self._playerX].add_player()
            self._see_neighbours()

    def go_east(self):
        if not(self._valid_position(self._playerX+1, self._playerY)):
            outputcontroller.movement_impossible()
        elif not(self._map[self._playerY][self._playerX+1].is_passable()):
            outputcontroller.movement_impossible()
        else:
            self._map[self._playerY][self._playerX].remove_player()
            self._playerX = self._playerX + 1
            self._map[self._playerY][self._playerX].add_player()
            self._see_neighbours()

    def draw_map(self):
        outputcontroller.visualize_dungeon(self._map)
