from typing import Union
import random

import mapping
import player
import gnome
from human import Human
import items


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def possible_attack(x,z):
    #it returns if an attack is possible
    #x:Human loc, z:Gnome loc
    if abs(x[0]-z[0]) <= 1 and abs(x[1]-z[1]) <= 1:
        return True
    else:
        return False

def attack(dungeon: mapping.Dungeon, player: player.Player, gnome: gnome.Gnome): # completar
    #if the human has weapon gnome dies, else takes away hp from gnome
    if Human.weapon == True:
        gnome.hp = 0
        gnome.set_is_alive()
    else:
        gnome.hp -= 25
        gnome.set_is_alive()


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric]):
    # completar
    raise NotImplementedError

def move (dungeon: mapping.Dungeon, player: player.Player, key, pickaxe_tool = False):
    '''
    Moves the player depending on the key pressed.

    -> s: down
    -> d: right
    -> a: left
    -> w: up
    '''
    dic = {'s': (0,1), 'w': (0,-1), 'a': (-1,0), 'd': (1,0)}
    loc = player.loc()
    new_loc = (loc[0]+dic[key][0], loc[1]+dic[key][1])
    if (0<=new_loc[0]< dungeon.columns and 0<=new_loc[1]< dungeon.rows):
        if dungeon.is_walkable(new_loc):
            player.move_to(new_loc)
        if pickaxe_tool and dungeon.loc(new_loc) == mapping.WALL:
            dungeon.dig(new_loc)
            player.move_to(new_loc)

def move_gnome (dungeon: mapping.Dungeon, gnome: gnome.Gnome):
    '''
    Moves the gnome randomly
    '''
    dic = {'s': (0,1), 'w': (0,-1), 'a': (-1,0), 'd': (1,0)}
    directions = ['s','w','a','d']
    key = random.choice(directions)
    loc = gnome.loc()
    new_loc = (loc[0]+dic[key][0], loc[1]+dic[key][1])
    if (0<=new_loc[0]< dungeon.columns and 0<=new_loc[1]< dungeon.rows):
        if dungeon.is_walkable(new_loc):
            gnome.move_to(new_loc)

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    '''
    Changes de dungeon level. (level 1 is first, and level 3 is the lowest)
    '''
    if dungeon.loc(player.loc()) == mapping.STAIR_UP:
        dungeon.level -= 1
    loc = dungeon.index(mapping.STAIR_DOWN)
    player.move_to (loc)
    return dungeon

def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    if dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
        dungeon.level += 1
    loc = dungeon.index(mapping.STAIR_UP)
    player.move_to (loc)
    return dungeon

def pickup(dungeon: mapping.Dungeon, player: player.Player):
    xy = player.loc()
    item_list = dungeon.get_items(xy)
    return item_list