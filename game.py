from direct.showbase.ShowBase import ShowBase
from map import Mapmanager
class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.land = Mapmanager()
        self.land.loadland("land.txt")
        


game = Game()
game.run()
        