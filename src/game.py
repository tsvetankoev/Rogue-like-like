import Map
import Player
import Battle
import MonsterGenerator


class Game:

    def __init__(self):
        self._maps = []
        self._player = Player()
        self._currentlevel = 1

    @classmethod
    def start(self):
        while (self._player._is_alive):
            self._maps[self._currentlevel - 1].print_map()
            command_text = input("")
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
                print("Unknown direction specified")
                return

            # handle tile contents
            player_tile = self._map().player_tile()
            contents = player_tile.get_contents()
            if (player_tile.is_entrance()):
                self._currentlevel -= 1
            elif (player_tile.is_exit()):
                self._currentlevel += 1
            if (player_tile.has_item() and not player_tile.is_visited()):
                print("Item found: " + contents.name())
                self._player.add_to_inventory(contents)
            elif (player_tile.has_monster() and not player_tile.is_visited()):
                monster = MonsterGenerator.generate(self._currentlevel, self._player.level())
                battle = Battle(self._player, monster)
                self._player = battle.start()


        # method for using items
        def _use_item(self, itemname):
            for item in self._player.inventory:
                if (item.name() == itemname):
                    self._player.use_item(item)
                    self._player.inventory.remove(item)
                    return
            print("No such item has been found")

        # method for listing inventory
        def _print_inventory(self):
            for item in self._player.inventory:
                print(item.name())

        # method for printing help
        def _help(self):
            print("Here is a list of command you can use:")
            print("- go north          : Move your character one block north")
            print("- go south          : Move your character one block south")
            print("- go west           : Move your character one block west")
            print("- go east           : Move your character one block east")
            print("- inventory         : "
                  "List the items you have in your inventory")
            print("- equip <item-name> : Equip the item specified. "
                  "If the item slot is taken "
                  "the currently equiped item will be replaced.")
            print("- use <item-name>   : Use the item specified. "
                  "If you have reached you max stat, "
                  "the item will be used anyway")
            print("- help              : List the commands you can use")

        # method for equping items
        def _equip(self, itemname):
            pass

        # TODO: handle the string evaluation
