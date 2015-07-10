class Tile:

    def __init__(self):
        self.passable = False
        self.visible = False
        self.entrance = False
        self.exit = False
        self.player = False
        self.has_item = False
        self.has_monster = False
        self.is_visited = False
