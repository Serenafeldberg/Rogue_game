#!/usr/bin/env python3
from curses.ascii import SO
import time
from tkinter import SW
import mapping
import magic

import random
from human import Human
from gnome import Gnome
from items import Item, PickAxe, Amulet, Sword
import actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0
    name = input("Enter name: ")
    pickaxe = PickAxe ('pickaxe', ')')
    sword = Sword("Sword", '/', 10, 50)

    # initial locations may be random generated

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    player = Human (name, dungeon.find_free_tile())
    gnomes = Gnome ('Gnome', dungeon.find_free_tile())
    amulet = Amulet ("Amulet", '"')
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    dungeon.add_item(pickaxe, 1)
    dungeon.add_item (amulet, 3)
    dungeon.add_item(sword , random.randint(1,3))

    turns = 0
    key = ''
    pickaxe_tool = False
    amulet_treasure = False
    sword_weapon = False
    while dungeon.level >= 0 and key != 'q':
        turns += 1
        # render map
        dungeon.render(player, gnomes)
         x = Human.loc()
         z = Gnome.loc()

        # read key
        key = magic.read_single_keypress()[0]
<<<<<<< HEAD
=======
        if key == 'b' and actions.possible_attack(x,z) == True:
            actions.attack()
            if Gnome.set_is_alive() == False:
                Gnome.gnome_dies()
        '''
        if key == 'b':
            #si el gnomo esta lo suficientemente cerca, que el humano pueda atacar
        '''
        '''
        if actions.possible_attack(x,z) == True:
            actions.attack()
        '''
>>>>>>> 5965b1968a2b9cf66a4f1c38fb1ccb6bd79576cc
        if key == 'p':
            item_list = actions.pickup(dungeon, player)
            for it in item_list:
                if isinstance(it, PickAxe):
                    pickaxe_tool = True
                if isinstance(it, Amulet):
                    amulet_treasure = True
                if isinstance (it, Sword):
                    sword_weapon = True
        
        #si el gnomo esta lo suficientemente cerca, que el humano pueda atacar
        x = player.loc()
        z = gnomes.loc()
        if key == 'b' and actions.possible_attack(x,z) == True:
                actions.attack(dungeon, gnomes)
                if gnomes.set_is_alive() == False:
                    gnomes.gnome_dies()
        if key == 'w' or key == 's' or key == 'a' or key == 'd':
            actions.move(dungeon, player, key, pickaxe_tool)
        
        if dungeon.loc(player.loc()) == mapping.STAIR_UP:
            if dungeon.level > 0:
                actions.climb_stair(dungeon, player)
        elif dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
            actions.descend_stair(dungeon, player)


        if actions.possible_attack(x,z) == True:
            #si el gnomo mata al humano, se termina el juego
            player.kill()
            print("The gnome has killed you")
            break
        else:
            actions.move_gnome(dungeon, gnomes)
        
        if amulet_treasure and dungeon.level == 0 and dungeon.loc(player.loc()) == mapping.STAIR_UP:
            print("Congratulations! you won")
            #Gano el juego porque subio al nivel 1 con el amuleto
            break
          
        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
