import random


class MonsterGenerator:

    @staticmethod
    def generate(map_level, player_level):
        min_stat = 1 + (map_level + player_level) / 2
        max_stat = 1 + (map_level + player_level * 5) / 2
        strength = random.randrange(min_stat, max_stat)
        dexterity = random.randrange(min_stat, max_stat)
        inteligence = random.randrange(min_stat, max_stat)

        names = ["Gnome", ["Troll"], ["Orc"], ["Gnoll"], ["Ogre"], ["Goblin"]]
        name = names[random.randrange(0, len(names))]
        return Monster(name, strength, dexterity, inteligence)
