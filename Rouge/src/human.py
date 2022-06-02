import random
from player import Player


class Human(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.weapon = False
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):
        self.hp = 0
        self.alive = False

    def has_sword(self):
        self.weapon = True

    def get_sword (self):
        return self.weapon

    def set_hp (self):
        self.hp -= 25
