import outputcontroller
from itemgenerator import ItemGenerator


def start(player, monster, level):
    while (player.hp > 0 and monster.hp > 0):
        player.attack(monster)
        if(monster.hp > 0):
            monster.attack(player)
    if player.hp > 0:
        outputcontroller.battle_won()
        items = ItemGenerator.generate(player.level, level)
        outputcontroller.items_found(items)
        player.add_to_inventory(items)
        player.gain_XP()
