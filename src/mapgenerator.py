import random
from tile import Tile


class Room:

    def __init__(self, width, height, top_left_X, top_left_Y):
        self.width = width
        self.height = height
        self.top_left_X = top_left_X
        self.top_left_Y = top_left_Y
        self.bottom_right_X = top_left_X + width
        self.bottom_right_Y = top_left_Y + height

    def _overlap(self, a_min, a_max, b_min, b_max):
        return not(a_min > b_max or a_max < b_min)

    def intersect(self, other_room):
        return (self._overlap(self.top_left_X, self.bottom_right_X,
                              other_room.top_left_X, other_room.bottom_right_X)
                and
                self._overlap(self.top_left_X, self.bottom_right_X,
                              other_room.top_left_X,
                              other_room.bottom_right_X))

    def random_tile(self):
        x = random.randrange(self.top_left_X + 1, self.bottom_right_X)
        y = random.randrange(self.top_left_Y + 1, self.bottom_right_Y)
        return (x, y)


class MapGenerator:

    def __init__(self,):
        self._dungeon = []
        self._width = 100
        self._height = 30

    def create_horizontal_tunnel(self, start, end, y):
        for x in range(min(start, end), max(start, end) + 1):
            self._dungeon[y][x].make_passable()

    def create_vertical_tunnel(self, start, end, x):
        for y in range(min(start, end), max(start, end) + 1):
            self._dungeon[y][x].make_passable()

    def generate(self):
        self._dungeon = [[Tile() for x in range(self._width)]
                          for y in range(self._height)]

        number_of_rooms = random.randrange(4, 8)
        rooms = []

        while len(rooms) <= number_of_rooms:
            width = random.randrange(5, 10)
            height = random.randrange(5, 10)
            top_left_X = random.randrange(0, self._width - width)
            top_left_Y = random.randrange(0, self._height - height)
            newroom = Room(width, height, top_left_X, top_left_Y)
            room_is_new = True
            for room in rooms:
                if newroom.intersect(room):
                    room_is_new = False
            if room_is_new:
                if (len(rooms) > 0):
                    (old_x, old_y) = rooms[len(rooms)-1].random_tile()
                    (new_x, new_y) = newroom.random_tile()
                    dice = random.randrange(0, 2)
                    if dice == 0:
                        self.create_horizontal_tunnel(old_x, new_x, old_y)
                        self.create_vertical_tunnel(old_y, new_y, new_x)
                    else:
                        self.create_vertical_tunnel(old_y, new_y, old_x)
                        self.create_horizontal_tunnel(old_x, new_x, new_y)
                rooms.append(newroom)
                self.create_room(newroom)

        self._populate(self._dungeon)
        return self._dungeon

    def create_room(self, room):
        for x in range(room.top_left_X + 1, room.bottom_right_X):
            for y in range(room.top_left_Y + 1, room.bottom_right_Y):
                self._dungeon[y][x].make_passable()

    def _populate(self, dungeon):
        monsters = 15
        items = 20
        # add monsters
        while (monsters > 0):
            x = random.randrange(0, self._width - 1)
            y = random.randrange(0, self._height - 1)
            if (dungeon[y][x].is_passable()
                    and not dungeon[y][x].has_monster()
                    and not dungeon[y][x].has_item()
                    and not dungeon[y][x].is_exit()
                    and not dungeon[y][x].is_exit()):
                dungeon[y][x].add_monster()
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
                dungeon[y][x].add_item()
                items = items - 1
