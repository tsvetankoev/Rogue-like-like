import Map
import Player
import Battle
import MonsterGenerator
import MapGenerator
import ItemGenerator
from inputcontroller import InputController
from outputcontroller import OutputController


class Game:

    def __init__(self):
        self._maps = []
        self._player = Player("")
        self._currentlevel = 1

    @classmethod
    def start(self):
        char_name = InputController.select_name()
        self._player.set_name(char_name)

        while (self._player._is_alive):
            self._maps[self._currentlevel - 1].print_map()
            command_text = InputController.select_command()
            command = self._interpate(command_text)
            command(self)

    def _map(self):
        return self._maps[self._currentlevel - 1]

    def _interprate(self, command_text):
        # method for map navigation
        def _move(self, direction):
            # move in a direction
            if (direction == "north"):
                self._maps[self._currentlevel - 1].go_north()
            elif (direction == "south"):
                self._maps[self._currentlevel - 1].go_south()
            elif (direction == "west"):
                self._maps[self._currentlevel - 1].go_west()
            elif (direction == "east"):
                self._maps[self._currentlevel - 1].go_east()
            else:
                OutputController.unknown_direction()
                return

            # handle tile contents
            player_tile = self._maps[self._currentlevel - 1].player_tile()
            if (player_tile.is_entrance()):
                if (self._currentlevel == 1):
                    OutputController.leave_dungeon()
                else:
                    self._currentlevel -= 1
            elif (player_tile.is_exit()):
                if (len(self._maps) == self._currentlevel):
                    new_map = Map(self._currentlevel, *(MapGenerator().generate()))
                    self._maps.append(new_map)
                self._currentlevel += 1
            elif (player_tile.has_item() and not player_tile.is_visited()):
                items = ItemGenerator.generate()
                OutputController.items_found(items)
                self._player.add_to_inventory(items)
            elif (player_tile.has_monster() and not player_tile.is_visited()):
                monster = MonsterGenerator.generate(self._currentlevel,
                                                    self._player.level())
                battle = Battle(self._player, monster)
                self._player = battle.start()

        # method for using items
        def _use_item(self, itemname):
            self._player.use_item(itemname)

        # method for listing inventory
        def _print_inventory(self):
            self._player.print_inventory()

        # method for printing help
        def _help(self):
            OutputController.help()

        # method for equping items
        def _equip(self, itemname):
            self._player.equip_item(itemname)

        # TODO: handle the string evaluation
