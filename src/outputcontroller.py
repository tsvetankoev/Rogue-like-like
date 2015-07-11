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
    for row in dungeon:
        for tile in row:
            if not tile.visible:
                print ("", end="")
            elif tile.player:
                print ("@")
            elif tile.entrance:
                print ("E")
            elif tile.exit:
                print ("X")
            elif not tile.passable:
                print ("#")
            elif tile.has_monster:
                print ("M")
            elif tile.has_item:
                print ("I")
            else:
                print (".")

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
