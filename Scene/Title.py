from Game_System import *
from Scene.__Base__ import __Base__

class Scene_Title(__Base__):
    
    def __init__(self):

        img1, rect = pg.Sys.Font.render("Hello pygame!", (255,255,255))
        
        self.image1 = pg.Sys.Texture(img1)
        self.image1_rect = rect
        self.image1_rect.center = (pg.Sys.WINDOWWIDTH/2, pg.Sys.WINDOWHEIGHT/2)

    def onChange(self):
        pass

    def onChangeDone(self):
        pass
    
    def update(self):
        pass

    def graphicsUpdate(self):
        pg.Sys.Renderer.copy(self.image1,None, self.image1_rect)
