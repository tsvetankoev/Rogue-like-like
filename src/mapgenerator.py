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
        '''Check if two rooms intersect'''
        return (self._overlap(self.top_left_X, self.bottom_right_X,
                              other_room.top_left_X, other_room.bottom_right_X)
                and
                self._overlap(self.top_left_X, self.bottom_right_X,
                              other_room.top_left_X,
                              other_room.bottom_right_X))

    def random_tile(self):
        '''Return the coordinates of a random tile from the room'''
        x = random.randrange(self.top_left_X + 1, self.bottom_right_X)
        y = random.randrange(self.top_left_Y + 1, self.bottom_right_Y)
        return (x, y)


class MapGenerator:

    def __init__(self,):
        self._dungeon = []
        self._width = 100
        self._height = 30

    def _create_horizontal_tunnel(self, start, end, y):
        for x in range(min(start, end), max(start, end) + 1):
            self._dungeon[y][x].passable = True

    def _create_vertical_tunnel(self, start, end, x):
        for y in range(min(start, end), max(start, end) + 1):
            self._dungeon[y][x].passable = True

    def _random_tile(self):
        x = random.randrange(0, self._width)
        y = random.randrange(0, self._height)
        return (x, y)

    def generate(self):
        '''Generate a new map'''
        self._dungeon = [[Tile() for x in range(self._width)]
                         for y in range(self._height)]

        number_of_rooms = random.randrange(4, 8)
        rooms = []

        entrance_x = None
        entrance_y = None
        exit_x = None
        exit_y = None

        while len(rooms) <= number_of_rooms:
            # generate new room
            width = random.randrange(5, 10)
            height = random.randrange(5, 10)
            top_left_X = random.randrange(0, self._width - width)
            top_left_Y = random.randrange(0, self._height - height)
            newroom = Room(width, height, top_left_X, top_left_Y)

            # check if room overlaps with previosly generated rooms
            room_is_new = True
            for room in rooms:
                if newroom.intersect(room):
                    room_is_new = False

            if room_is_new:
                # add hallways
                if (len(rooms) > 0):
                    (old_x, old_y) = rooms[len(rooms)-1].random_tile()
                    (new_x, new_y) = newroom.random_tile()
                    dice = random.randrange(0, 2)
                    if dice == 0:
                        self._create_horizontal_tunnel(old_x, new_x, old_y)
                        self._create_vertical_tunnel(old_y, new_y, new_x)
                    else:
                        self._create_vertical_tunnel(old_y, new_y, old_x)
                        self._create_horizontal_tunnel(old_x, new_x, new_y)
                # add new room
                rooms.append(newroom)
                self._create_room(newroom)

                # add entrance in first room
                if len(rooms) == 1:
                    (entrance_x, entrance_y) = newroom.random_tile()
                    self._dungeon[entrance_y][entrance_x].entrance = True
                    self._dungeon[entrance_y][entrance_x].player = True
                    self._dungeon[entrance_y][entrance_x - 1].visible = True
                    self._dungeon[entrance_y][entrance_x + 1].visible = True
                    self._dungeon[entrance_y + 1][entrance_x].visible = True
                    self._dungeon[entrance_y - 1][entrance_x].visible = True
                    self._dungeon[entrance_y][entrance_x].visible = True

                # add exit in last room
                elif len(rooms) == number_of_rooms:
                    (exit_x, exit_y) = newroom.random_tile()
                    self._dungeon[exit_y][exit_x].exit = True

        self._populate(self._dungeon)
        return (self._dungeon, entrance_x, entrance_y, exit_x, exit_y)

    def _create_room(self, room):
        for x in range(room.top_left_X + 1, room.bottom_right_X):
            for y in range(room.top_left_Y + 1, room.bottom_right_Y):
                self._dungeon[y][x].passable = True

    def _populate(self, dungeon):
        monsters = 15
        items = 20
        # add monsters
        while (monsters > 0):
            x = random.randrange(0, self._width - 1)
            y = random.randrange(0, self._height - 1)
            if (dungeon[y][x].passable
                    and not dungeon[y][x].has_monster
                    and not dungeon[y][x].has_item
                    and not dungeon[y][x].entrance
                    and not dungeon[y][x].exit):
                dungeon[y][x].has_monster = True
                monsters = monsters - 1

        # add items
        while (items > 0):
            x = random.randrange(0, self._width)
            y = random.randrange(0, self._height)
            if (dungeon[y][x].passable
                    and not dungeon[y][x].has_monster
                    and not dungeon[y][x].has_item
                    and not dungeon[y][x].entrance
                    and not dungeon[y][x].exit):
                dungeon[y][x].has_item = True
                items = items - 1
