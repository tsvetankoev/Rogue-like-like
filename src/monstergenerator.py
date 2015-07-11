import random
from monster import Monster

def generate(map_level, player_level):
    min_stat = 1 + (map_level + player_level) / 2
    max_stat = 1 + (map_level + player_level * 5) / 2
    strength = random.randrange(min_stat, max_stat)
    dexterity = random.randrange(min_stat, max_stat)
    intelligence = random.randrange(min_stat, max_stat)
    hp = strength + 5 * dexterity
    mana = intelligence * 5

    names = ["Gnome", "Troll", "Orc", "Gnoll", "Ogre", "Goblin"]
    name = names[random.randrange(0, len(names))]
    return Monster(name, hp, mana, strength, dexterity, intelligence)
