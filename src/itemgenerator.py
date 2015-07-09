import random
from equipment import *
from potion import *


class ItemGenerator:

    number_of_weapons = 1
    number_of_shields = 1

    @staticmethod
    def generate(player_level, map_level):
        items = []
        potion_points = player_level * 10 + map_level * 2
        stat_points = 1 + player_level / 10
        min_equipment_points = (player_level * 2 + map_level)
        max_equipment_points = (player_level * 5 + map_level)
        if random.randrange(0, 2) == 0:
            item = Potion("Potion of Health", potion_points)
            items.append(item)
        if random.randrange(0, 2) == 0:
            item = Potion("Potion of Mana", potion_points)
            items.append(item)
        if random.randrange(0, 10) == 0:
            item = Potion("Potion of Strength", stat_points)
            items.append(item)
        if random.randrange(0, 10) == 0:
            item = Potion("Potion of Dexterity", stat_points)
            items.append(item)
        if random.randrange(0, 10) == 0:
            item = Potion("Potion of Inteligence", stat_points)
            items.append(item)
        if random.randrange(0, 5) == 0:
            strength = random.randrange(min_equipment_points,
                                        max_equipment_points)
            dexterity = random.randrange(min_equipment_points,
                                         max_equipment_points)
            inteligence = random.randrange(min_equipment_points,
                                           max_equipment_points)
            item = Equipment("Sword #" + str(ItemGenerator.number_of_weapons),
                             strength, dexterity, inteligence)
            ItemGenerator.number_of_weapons += 1
            items.append(item)
        if random.randrange(0, 5) == 0:
            strength = random.randrange(min_equipment_points,
                                        max_equipment_points)
            dexterity = random.randrange(min_equipment_points,
                                         max_equipment_points)
            inteligence = random.randrange(min_equipment_points,
                                           max_equipment_points)
            item = Equipment("Shield #" + str(ItemGenerator.number_of_shields),
                             strength, dexterity, inteligence)
            ItemGenerator.number_of_shields += 1
            items.append(item)
        return items
