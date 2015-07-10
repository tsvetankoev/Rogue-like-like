class OutputController:

    @staticmethod
    def movement_impossible():
        print("Can't go that way.")

    @staticmethod
    def not_a_valid_attack():
        print("You didn't choose a valid attack")

    @staticmethod
    def battle_won():
        print("Congratulation. You won.")

    @staticmethod
    def items_found(items):
        print("You have found the following items:")
        for item in items:
            print(item.name)

    @staticmethod
    def unknown_direction():
        print("Unknown direction specified")

    @staticmethod
    def leave_dungeon():
        print("There is no reason to leave the dungeon")

    @staticmethod
    def help():
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

    @staticmethod
    def item_not_found():
        print("No such item has been found")
