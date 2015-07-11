# Rogue-like-like
Rogue-like-like is a console roguelike game written in Python 3.4 for the purposes of the Programming with Python course at the Faculty of Mathematics and Informatics of the Sofia Univercity "St. Kliment Ohridski"

## How to Play the game
Download the source code and start the game from the play.py file. The game needs to have the console be able to display at least 100 symbols per row.

##Features
* The game has infinite maps, each of which is randomly generated.
* People die if they are killed. There are no saves.
* The game is played in console with text commands. No fancy UIs here.
* Monsters will be randomly generated. *Hopefully* their stats will be optimized correctly to your own stats. Expect to die a lot.
* Items will be randomly generated.


###Hero
* Has different stats increased by every level, by equiping items, and by using potions.
* Has health bar.
* Has mana bar.
* Has inventory with items.
* Has equiped items.
* Can attack either with weapon or with magic.

###Monster
* Has randomly generated stats.
* Can attack either with weapon or magic.
* Very wooden *AI*.

###Fights
* Random encounter system.
* Finishes when one of the opponents dies.
* If player dies, GAME OVER.
* If monster dies, players gets XP and a random generated chance of getting an item.


###Map
* Randomly generated
* Player class has functions to traverse the map.
* Map gets revealed as player traverses it.
* Entrances to previous dungeon and to next dungeon.
