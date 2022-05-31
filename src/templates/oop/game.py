#!/usr/bin/env python3
import time
import mapping
import magic

import random
from human import Human
from gnome import Gnome
from items import Item, PickAxe, Amulet
import actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0
    name = input("Enter name: ")
    pickaxe = PickAxe ('pickaxe', ')')

    # initial locations may be random generated

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    player = Human (name, dungeon.find_free_tile())
    gnomes = Gnome ('Gnome', dungeon.find_free_tile())
    amulet = Amulet ("Amulet", '"')
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    dungeon.add_item(pickaxe, 1)
    dungeon.add_item (amulet, 3)

    turns = 0
    key = ''
    pickaxe_tool = False
    amulet_tool = False
    while dungeon.level >= 0 and key != 'q':
        turns += 1
        # render map
        dungeon.render(player, gnomes)

        # read key
        key = magic.read_single_keypress()[0]
        if key == 'p':
            item_list = actions.pickup(dungeon, player)
            for it in item_list:
                if isinstance(it, PickAxe):
                    pickaxe_tool = True
                if isinstance(it, Amulet):
                    amulet_tool = True
        if key == 'w' or key == 's' or key == 'a' or key == 'd':
            actions.move(dungeon, player, key, pickaxe_tool)
        
        if dungeon.loc(player.loc()) == mapping.STAIR_UP:
            actions.climb_stair(dungeon, player)
        if dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
            actions.descend_stair(dungeon, player)

        actions.move_gnome(dungeon, gnomes)

        if amulet_tool and dungeon.level == 1:
            #Gano el juego porque subio al nivel 1 con el amuleto
            break
          
        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
