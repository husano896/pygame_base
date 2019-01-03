import sys
sys.path.insert(0,'./System')
sys.path.insert(0,'./Scene')

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

from Game_System import *
from pygame.locals import *
from Scene.Intro import Scene_Intro

#Game name
GAMENAME = "Hello pygame"

startup_Scene = Scene_Intro()
frame = 0

#Add support for console if needed (experiment)
#import Game_Debug

"""
def showFPS():
    global FPSCLOCK, frame

    if (SDL2):
        ##Old Font
        img_FPS = pg.Sys.Font.render("%.2f (%d)" % (FPSCLOCK.get_fps(), frame) , 1, (255,255,255))
    else:
        ##Freetype
        img_FPS = pg.Sys.Font.render("%.2f (%d)" % (FPSCLOCK.get_fps(), frame) , (255,255,255))[0]
    if (pg.Sys.RenderEnabled):
        pg.render.Sprite(pg.Sys.Renderer.load_texture(img_FPS)).render((0,0))
    else:
        pg.Sys.Screen.blit(img_FPS,(0,0))

    frame+=1
    pg.display.set_caption("%s %.2f" % (GAMENAME, FPSCLOCK.get_fps()))
"""

def main():
    global FPSCLOCK, sleeping
    FPSCLOCK = pg.time.Clock()

    pg.Sys.ChangeScene(startup_Scene)
    
    while True:
        
        pg.Sys.Update()
        for event in pg.Sys.Events:
            #Mouse event example
            if event.type in (MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP):
                cur_x, cur_y = event.pos
                    

        pg.Sys.Screen.fill(pg.Sys.BGCOLOR)

        if (pg.Sys.Scene):
            pg.Sys.Scene.update()
            pg.Sys.Scene.graphicsUpdate()

        pg.display.flip()
        
        FPSCLOCK.tick(FPS)
        
if __name__ == '__main__':
    main()
