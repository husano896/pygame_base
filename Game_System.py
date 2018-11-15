SDL2 = True
RenderEnabled = True
if (SDL2):
    try:
        import pygame_sdl2
        pygame_sdl2.import_as_pygame()
        import pygame.render
    except ImportError:
        print("pygame_sdl2 importing failed! Disabled SDL2")
        SDL2 = False

import pygame
import System.Audio
from Scene.__Changer__ import Scene_Changer
#### Initalize

#Framerate
FPS = 60

#Resolution
WINDOWWIDTH,WINDOWHEIGHT = 800, 600

class Game_System():
    def __init__(self):
        global SDL2, RenderEnabled
        pygame.init()
        
        self.WINDOWWIDTH, self.WINDOWHEIGHT = WINDOWWIDTH, WINDOWHEIGHT
        self.BGColor = (127, 127, 127)
        self.Screen = pygame.display.set_mode((self.WINDOWWIDTH,self.WINDOWHEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
        
        self.Scene = None
        self.Audio = System.Audio
        self.Audio.init()
        self.SDL2 = SDL2

        self.Font = pygame.font.Font("Fonts/NotoSansCJKtc-Regular.otf", 14)

        self.RenderEnabled = RenderEnabled
        self.Handle_Events_InMain = True
        
        if (SDL2):
            try:
                self.Renderer = pygame.render.Renderer(vsync=True)
            except ImportError:
                print("render importing failed!")
                self.RenderEnabled = False
                
    def ChangeScene(self, nextScene):
        self.Scene = Scene_Changer(nextScene)
        
#Inject into pygame
pygame.pgSys = Game_System()
