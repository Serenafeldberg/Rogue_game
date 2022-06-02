from player import Player

class Gnome (Player):
    def __init__ (self, name, xy):
        super().__init__(name, xy)

        self.alive = True
        self.face = 'G'
    def set_is_alive(self):
        if self.hp == 0:
            self.alive = False
    def get_alive(self):
        return self.alive
          
