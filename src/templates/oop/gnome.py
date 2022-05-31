from player import Player

class Gnome (Player):
    def __init__ (self, name, xy):
        super().__init__(name, xy)

        self.alive = True
        self.face = 'G'
        def set_is_alive(self):
        if self.hp == 0:
            return False
        else:
            return True
