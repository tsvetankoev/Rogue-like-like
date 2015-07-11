from player import Player
import inputcontroller
import outputcontroller
from mapgenerator import MapGenerator
from itemgenerator import ItemGenerator
from dungeon import Map
import monstergenerator
import battle


class Game:

    def __init__(self):
        self._maps = []
        self._player = Player("")
        self.currentlevel = 1
        self._ghost_mode = False
        self._game_commands = {"go": self._move,
                               "use": self._use_item,
                               "equip": self._equip,
                               "inventory": self._inventory,
                               "stats": self._stats,
                               "help": self._help,
                               "godmode": self._god_mode}

    def start(self):
        char_name = inputcontroller.select_name()
        self._player.name = char_name
        new_map = Map(self.currentlevel, *(MapGenerator().generate()))
        self._maps.append(new_map)

        while (self._player.hp > 0):
            outputcontroller.clear_console()
            outputcontroller.visualize_dungeon(
                self._maps[self.currentlevel - 1].get_map())
            command_text = inputcontroller.select_command()
            command = inputcontroller.command_interpretator(command_text)

            if command is False:
                outputcontroller.unknown_command()
            elif type(command) is list:
                argument = command[1]
                command = command[0]
                self._game_commands[command](argument)
            else:
                print(command)
                func = self._game_commands[command]
                func()
            outputcontroller.clear_console()
        outputcontroller.game_over()

    def _map(self):
        return self._maps[self.currentlevel - 1]

    def _move(self, direction):
        # move in a direction
        if (direction == "north"):
            self._maps[self.currentlevel - 1].go_north()
        elif (direction == "south"):
            self._maps[self.currentlevel - 1].go_south()
        elif (direction == "west"):
            self._maps[self.currentlevel - 1].go_west()
        elif (direction == "east"):
            self._maps[self.currentlevel - 1].go_east()
        else:
            outputcontroller.unknown_direction()
            return

        # handle tile contents
        player_tile = self._maps[self.currentlevel - 1].player_tile()

        # if player goes to entrance go to previous level
        # if he is on level one, give coresponing output
        if (player_tile.entrance):
            if (self.currentlevel == 1):
                outputcontroller.leave_dungeon()
            else:
                self.currentlevel -= 1

        # if player go to the exit, go to the next level
        # generate next map if needed
        elif (player_tile.exit):
            if (len(self._maps) == self.currentlevel):
                new_map = Map(self.currentlevel, *(MapGenerator().generate()))
                self._maps.append(new_map)
            self.currentlevel += 1

        # if tile has items, add them to inventory
        elif(player_tile.has_item and not player_tile.is_visited):
            items = ItemGenerator.generate(self._player.level,
                                           self.currentlevel)
            outputcontroller.items_found(items)
            self._player.add_to_inventory(items)
            inputcontroller.press_enter_to_continue()

        # if tile has a monster, generate monster and start battle
        elif(player_tile.has_monster and not player_tile.is_visited):
            monster = monstergenerator.generate(self.currentlevel,
                                                self._player.level)
            battle.start(self._player, monster, self.currentlevel)
            inputcontroller.press_enter_to_continue()

    # method for using items
    def _use_item(self, itemname):
        self._player.use_item(itemname)
        inputcontroller.press_enter_to_continue()

    # method for listing inventory
    def _inventory(self):
        self._player.print_inventory()
        inputcontroller.press_enter_to_continue()

    # method for printing help
    def _help(self):
        outputcontroller.help()
        inputcontroller.press_enter_to_continue()

    # method for equping items
    def _equip(self, itemname):
        self._player.equip_item(itemname)
        inputcontroller.press_enter_to_continue()

    def _stats(self):
        self._player.stats()
        inputcontroller.press_enter_to_continue()

    def _god_mode(self):
        self._player.hp = 999999999
