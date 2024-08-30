class Mapmanager():
    def __init__(self):
        self.grass_block = 'grass-block.glb'
        self.dirt_block  = "dirt-block.glb"
        self.stone_block = "stone-block.glb"
        self.startNew()
    
    def add_block(self,position,model):
        self.model = loader.loadModel(model)
        self.model.setPos(position)
        self.model.setScale(1,1,1)
        self.model.setHpr(0,180,0)
        self.model.reparentTo(render)
        
    def startNew(self):
        self.land = render.attachNewNode("Land")
        
    
    def clear(self):
        self.land.removeNode()
        self.startNew()
        
