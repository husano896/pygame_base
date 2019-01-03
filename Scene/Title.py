from Game_System import *
from Scene.__Base__ import __Base__

class Scene_Title(__Base__):
    
    def __init__(self):

        img1 = pg.Sys.Font.render("Hello pygame!", 1, (255,255,255))
        
        self.image1 = img1

    def onChange(self):
        pass

    def onChangeDone(self):
        pass
    
    def update(self):
        pass

    def graphicsUpdate(self):
        pos = (pg.Sys.WINDOWWIDTH/2, pg.Sys.WINDOWHEIGHT/2)
        rect = self.image1.get_rect()
        rect.center = pos
        pg.Sys.Screen.blit(self.image1,rect)
