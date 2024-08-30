class Mapmanager():
    def __init__(self):
        self.grass_block = "block/grass-block.glb"
        self.dirt_block = "block/dirt-block.glb"
        self.stone_block = "block/stone-block.glb"
        
        self.startNew()

    def add_block(self, position, model):
        self.model = loader.loadModel(model)
        self.model.reparentTo(render)
        self.model.setScale(1, 1, 1)
        self.model.setPos(position)
        self.model.setHpr(0, 90, 0)
    
    def startNew(self):
        self.land = render.attachNewNode("Land")
    
    def clear(self):
        self.land.removeNode()
        self.startNew()
    
    def loadland(self,file):
        self.clear()
        with open(file) as f:
            y = 0
            for line in f:
                x = 0 
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        model = self.add_block((x,y,z0), self.select_block(int(z),z0))
                    x += 1
                y += 1
        return x,y
    def select_block(self,z,z0):
        if z0 < z//3:
            return self.stone_block
        elif z//3 < z0 < z:
            return self.dirt_block
        else:
            return self.grass_block

