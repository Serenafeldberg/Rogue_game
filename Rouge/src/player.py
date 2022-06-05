from typing import Tuple

class Player:
    def __init__(self, name, xy, hit_points=50):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points

    def loc(self):
        return self.x, self.y

    def set_loc (self, xy: Tuple):
        self.x, self.y = xy

    def move_to(self, xy):
        self.x, self.y = xy

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"

    def get_hp (self):
        return self.hp
