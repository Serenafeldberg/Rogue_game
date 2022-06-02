from player import Player

class Gnome (Player):
    def __init__ (self, name, xy):
        super().__init__(name, xy)

        self.alive = True
        self.face = 'G'
    def set_is_alive(self):
        if self.hp == 0:
            self.alive = False
<<<<<<< HEAD

=======
>>>>>>> 5965b1968a2b9cf66a4f1c38fb1ccb6bd79576cc
    def get_alive(self):
        return self.alive
    def gnome_dies(self):
        self.face = None
        self.x,self.y = None
          
