import pygame as pg
import pygame.freetype as ft
import System.Audio
import System.Localization
from Scene.__Changer__ import Scene_Changer

#### Initalize

#Framerate
FPS = 60

#Resolution
WINDOWWIDTH,WINDOWHEIGHT = 800, 600

class Game_System():
    
    def __init__(self):
        pg.init()
        
        self.WINDOWWIDTH, self.WINDOWHEIGHT = WINDOWWIDTH, WINDOWHEIGHT
        self.BGCOLOR = (0, 0, 0)
        self.Screen = pg.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT), pg.HWSURFACE | pg.DOUBLEBUF)
        
        self.Scene = None
        self.Audio = System.Audio
        self.Audio.init()
        self.Events = []
        self.Font = ft.Font("Fonts/NotoSansCJKtc-Regular.otf", 14)
        self.FontLarge = ft.Font("Fonts/NotoSansCJKtc-Regular.otf", 32)
        
    def ChangeScene(self, nextScene):
        self.Scene = Scene_Changer(nextScene)

    def InitDisplay(self):
        self.Screen = pg.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT), pg.HWSURFACE | pg.DOUBLEBUF)

    def Update(self):
        self.Events = pg.event.get()
        for ev in self.Events:
            if ev.type == pg.QUIT:
                pg.quit()
                exit()
                return
        
#Inject into pygame
pg.Sys = Game_System()
#for i18n
pg.l = System.Localization.l
