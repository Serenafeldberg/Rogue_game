from typing import Union
import random
import math

import mapping
import player
import gnome
import human
import items


numeric = Union[int, float]

def possible_attack(x,z):
    '''
    It returns if an attack is possible depending on the distance

    -> x: Human location
    -> z: Gnome location
    '''
    if abs(x[0]-z[0]) <= 1 and abs(x[1]-z[1]) <= 1:
        return True
    else:
        return False

def attack(human: human.Human, gnome: gnome.Gnome):
    '''
    If the human has weapon, the gnome dies, else takes away hp from the gnome

    -> human: human player
    -> gnome: gnome player
    '''
    if human.get_sword() == True:
        gnome.hp = 0
        gnome.set_is_alive()
    else:
        gnome.hp -= 25
        gnome.set_is_alive()

def move (dungeon: mapping.Dungeon, player: player.Player, key, pickaxe_tool = False):
    '''
    Moves the player depending on the key pressed.

    -> dungeon: instance of a dungeon map
    -> player: player (it can be either the human or the gnome)
    -> key: key pressed (s: down, d: right, a: left, w: up)
    -> pickaxe_tool: True if the human has the pickaxe, else false.
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

def move_gnome_ (dungeon: mapping.Dungeon, gnome: gnome.Gnome):
    '''
    Moves the gnome randomly

    -> dungeon: instance of a dungeon map
    -> gnome: Gnome player
    '''
    dic = {'s': (0,1), 'w': (0,-1), 'a': (-1,0), 'd': (1,0)}
    directions = ['s','w','a','d']
    key = random.choice(directions)
    loc = gnome.loc()
    new_loc = (loc[0]+dic[key][0], loc[1]+dic[key][1])
    if (0<=new_loc[0]< dungeon.columns and 0<=new_loc[1]< dungeon.rows):
        if dungeon.is_walkable(new_loc):
            gnome.move_to(new_loc)

def move_gnome (dungeon: mapping.Dungeon, gnome: gnome.Gnome, player: player.Player):
    dic = {4: (0,1), 2: (0,-1), 3: (-1,0), 0: (1,0), 1: (1,0)}
    dire = [0, 90, 180, 270, 360]
    angle_list = []
    loc_g = gnome.loc()
    loc_p = player.loc()
    
    angle = math.atan2(loc_p[1]-loc_g[1] , loc_p[0] - loc_g[0]) * (180/3.14)

    print (angle)
    if angle < 0:
        angle += 360
    for ang in dire:
        angle_list.append(abs(angle-ang))

    print(angle_list)
    index_nearest_angle = angle_list.index(min(angle_list))
    print(index_nearest_angle)
    new_loc = (loc_g[0]+dic[index_nearest_angle][0], loc_g[1]+dic[index_nearest_angle][1])
    if (0<=new_loc[0]< dungeon.columns and 0<=new_loc[1]< dungeon.rows):
        if dungeon.is_walkable(new_loc):
            gnome.move_to(new_loc)
    

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    '''
    Changes de dungeon level. (level 1 is first, and level 3 is the lowest)

    -> dungeon: instance of a dungeon map
    -> player: player (it can be either the human or the gnome)
    '''
    if dungeon.loc(player.loc()) == mapping.STAIR_UP:
        dungeon.level -= 1
    loc = dungeon.index(mapping.STAIR_DOWN)
    player.move_to (loc)
    return dungeon

def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    '''
    Changes the dungeon level

    -> dungeon: instance of a dungeon map
    -> player: player (it can be either the human or the gnome)
    '''
    if dungeon.loc(player.loc()) == mapping.STAIR_DOWN:
        dungeon.level += 1
    loc = dungeon.index(mapping.STAIR_UP)
    player.move_to (loc)
    return dungeon

def pickup(dungeon: mapping.Dungeon, player: player.Player):
    '''
    Allows the player to pick up items

    -> dungeon: instance of a dungeon map
    -> player: player (it can be either the human or the gnome)
    '''
    xy = player.loc()
    item_list = dungeon.get_items(xy)
    return item_list
