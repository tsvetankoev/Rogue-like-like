import random
import Tile


class MapGenerator:

    def __init__(self,):
        self._dungeon = []
        self._width = 50
        self._height = 30

    def generate(self):
        self.dungeon = [[Tile() for x in range(self._width)]
                        for y in range(self._height)]
        # generate map here
        # make random rooms (4-6)
        # make halways

        # populate dungeon
        self._populate(self._dungeon)
        return self._dungeon

    def populate(self, dungeon):
        monsters = 30
        items = 20
        # add monsters
        while (monsters > 0):
            x = random.randrange(0, self._width)
            y = random.randrange(0, self._height)
            if (dungeon[y][x].is_passable()
                    and not dungeon[y][x].has_monster()
                    and not dungeon[y][x].has_item()
                    and not dungeon[y][x].is_exit()
                    and not dungeon[y][x].is_exit()):
                dungeon[x][y].add_monster()
                monsters = monsters - 1

        # add items
        while (items > 0):
            x = random.randrange(0, self._width)
            y = random.randrange(0, self._height)
            if (dungeon[y][x].is_passable()
                    and not dungeon[y][x].has_monster()
                    and not dungeon[y][x].has_item()
                    and not dungeon[y][x].is_exit()
                    and not dungeon[y][x].is_exit()):
                dungeon[x][y].add_item()
                items = items - 1
