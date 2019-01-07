import sys, os
sys.path.insert(0,'./System')
sys.path.insert(0,'./Scene')

os.environ['SDL_VIDEO_CENTERED'] = '1'

from Game_System import *
from Scene.Intro import Scene_Intro

startup_Scene = Scene_Intro()

def main():
    global FPSCLOCK
    FPSCLOCK = pg.time.Clock()

    pg.Sys.ChangeScene(startup_Scene)
    
    while True:
        pg.Sys.Update()
        for event in pg.Sys.Events:
            pass
        
        pg.Sys.Screen.fill(pg.Sys.BGCOLOR)

        if (pg.Sys.Scene):
            pg.Sys.Scene.update()
            pg.Sys.Scene.graphicsUpdate()

        pg.display.flip()
        
        FPSCLOCK.tick(FPS)
        
if __name__ == '__main__':
    main()
