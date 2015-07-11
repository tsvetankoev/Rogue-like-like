import os
import inputcontroller


def movement_impossible():
    print("Can't go that way.")


def not_a_valid_attack():
    print("You didn't choose a valid attack")


def battle_won():
    print("Congratulation. You won.")


def items_found(items):
    print("You have found the following items:")
    for item in items:
        print(item.name)


def unknown_direction():
    print("Unknown direction specified")


def leave_dungeon():
    print("There is no reason to leave the dungeon")


def help():
    print("Here is a list of command you can use:")
    print("- go north      : Move your character one block north")
    print("- go south      : Move your character one block south")
    print("- go west       : Move your character one block west")
    print("- go east       : Move your character one block east")
    print("- inventory     : "
          "List the items you have in your inventory")
    print("- stats     : "
          "List the player stats")
    print("- equip <item-name> : Equip the item specified. "
          "If the item slot is taken "
          "the currently equiped item will be replaced.")
    print("- use <item-name>   : Use the item specified. "
          "If you have reached you max stat, "
          "the item will be used anyway")
    print("- help          : List the commands you can use")


def item_not_found():
    print("No such item has been found")


def visualize_dungeon(dungeon):
    clear_console()
    for row in dungeon:
        for tile in row:
            if tile.player:
                print("@", end="")
            elif not tile.visible:
                print(" ", end="")
            elif tile.entrance:
                print("E", end="")
            elif tile.exit:
                print("X", end="")
            elif not tile.passable:
                print("#", end="")
            elif tile.has_monster:
                print("M", end="")
            elif tile.has_item:
                print("I", end="")
            else:
                print(".", end="")
        print()


def attacks(attacker, defender, damage, critical):
    if critical:
        print("{} attacked {} for {} damage.".format(attacker, defender,
                                                     damage))
    else:
        print("{} critically attacked {} for {} damage.".format(attacker,
                                                                defender,
                                                                damage))


def level_up():
    print("Congratulations. You leveled up.")


def game_over():
    print("Game over.")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_stats(name, hp, max_hp, xp, xp_for_next_level, strength, dexterity,
                intelligence):
    print("Hero {}".format(name))
    print("Health: {}/{}".format(hp, max_hp))
    print("XP: {}/{}".format(xp, xp_for_next_level))
    print("Strength: {}".format(strength))
    print("Dexterity: {}".format(dexterity))
    print("Intelligence: {}".format(intelligence))


def unknown_command():
    print("Unknown command.")
    print("Type \"help\" to see a list of commands.")


def inventory(items):
    for item in items:
        print(item.name)
