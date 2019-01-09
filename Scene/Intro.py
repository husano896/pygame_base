from Game_System import *
from Scene.__Base__ import __Base__
from Scene.Title import Scene_Title

class Scene_Intro(__Base__):
    
    def __init__(self):
        Font = pg.font.SysFont("Arial", 32)
                
        img1 = Font.render("pygame presents", 1, (255,255,255))
            
        self.Image1 = pg.Sys.Texture(img1)
        self.Image1_rect = img1.get_rect()
        self.frame = 0
        
    def onChange(self):
        pass

    def onChangeDone(self):
        pass
    
    def update(self):
        
        self.frame += 1
        #Change scene after 384 frames
        if (self.frame > 384):
            pg.Sys.ChangeScene(Scene_Title())
            return

        #Here shows how a simple "anim like" text works
        if (self.frame > 255):
            alpha = max(0, 767-int(self.frame*2))
        else:
            alpha = min(int(self.frame*2), 255)

        self.Image1.alpha = alpha
        
    def graphicsUpdate(self):
        pos = self.Image1_rect
        pos.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)

        pg.Sys.Renderer.copy(self.Image1,None, pos)
