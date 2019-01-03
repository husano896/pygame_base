from Scene.__Base__ import __Base__
from Game_System import *
class Scene_Changer(__Base__):

    def __init__(self, newscene, speed = 8):
        self.frame = 0
        self.speed = speed
        self.Img_LastScene = pg.Sys.Screen.copy()
        
        newscene.update()
        self.Img_NewScene = pg.Sys.Screen.copy()
        
        self.new_scene = newscene

        self.new_scene.onChange()
        
        pg.Sys.Scene = self
        
    def update(self):
        
        self.Img_NewScene.set_alpha(self.frame)

        pg.Sys.Screen.blit(self.Img_LastScene, (0,0))
        pg.Sys.Screen.blit(self.Img_NewScene, (0,0))
        self.frame+=self.speed
        
        if (self.frame >= 256):
            self.new_scene.onChangeDone()
            pg.Sys.Scene = self.new_scene
